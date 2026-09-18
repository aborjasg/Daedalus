-- Populate user tables with a small amount of deterministic mock data.
--
-- Usage:
--   PGPASSWORD='...' psql \
--     'host=10.0.0.86 port=5432 user=postgres dbname=daedalus_controlpanel_db' \
--     -v ON_ERROR_STOP=1 -f database/seed_mock_data.sql
--
-- This script does not drop or truncate data. It skips identity/generated
-- columns and columns with defaults, and reports tables whose constraints
-- prevent a generated row from being inserted.

BEGIN;

CREATE TEMP TABLE seed_results (
    schema_name text NOT NULL,
    table_name text NOT NULL,
    inserted_rows integer NOT NULL DEFAULT 0,
    status text NOT NULL,
    detail text
) ON COMMIT DROP;

DO $seed$
DECLARE
    table_record record;
    column_record record;
    column_names text;
    value_expressions text;
    insert_sql text;
    inserted integer;
    affected_rows integer;
    row_number integer;
    enum_value text;
BEGIN
    FOR table_record IN
        SELECT n.nspname AS schema_name, c.relname AS table_name
        FROM pg_class c
        JOIN pg_namespace n ON n.oid = c.relnamespace
        WHERE c.relkind IN ('r', 'p')
          AND n.nspname NOT IN ('pg_catalog', 'information_schema')
          AND n.nspname NOT LIKE 'pg_%'
        ORDER BY n.nspname, c.relname
    LOOP
        inserted := 0;

        BEGIN
            FOR row_number IN 1..3 LOOP
                column_names := '';
                value_expressions := '';

                FOR column_record IN
                    SELECT
                        a.attname,
                        format_type(a.atttypid, a.atttypmod) AS formatted_type,
                        t.typname,
                        t.typtype,
                        a.attnotnull,
                        a.atthasdef,
                        a.attidentity,
                        a.attgenerated,
                        lower(coalesce(col_description(a.attrelid, a.attnum), '')) AS description
                    FROM pg_attribute a
                    JOIN pg_type t ON t.oid = a.atttypid
                    WHERE a.attrelid = format('%I.%I', table_record.schema_name, table_record.table_name)::regclass
                      AND a.attnum > 0
                      AND NOT a.attisdropped
                      AND a.attidentity = ''
                      AND a.attgenerated = ''
                      AND NOT a.atthasdef
                    ORDER BY a.attnum
                LOOP
                    IF column_names <> '' THEN
                        column_names := column_names || ', ';
                        value_expressions := value_expressions || ', ';
                    END IF;

                    column_names := column_names || format('%I', column_record.attname);

                    IF column_record.typtype = 'e' THEN
                        SELECT e.enumlabel
                        INTO enum_value
                        FROM pg_enum e
                        JOIN pg_type et ON et.oid = e.enumtypid
                        WHERE et.typname = column_record.typname
                        ORDER BY e.enumsortorder
                        LIMIT 1;
                        value_expressions := value_expressions || quote_literal(enum_value);
                    ELSIF column_record.typname = 'bool' THEN
                        value_expressions := value_expressions || CASE WHEN row_number % 2 = 1 THEN 'true' ELSE 'false' END;
                    ELSIF column_record.typname IN ('int2', 'int4', 'int8', 'numeric', 'float4', 'float8') THEN
                        value_expressions := value_expressions || row_number::text;
                    ELSIF column_record.typname = 'uuid' THEN
                        value_expressions := value_expressions ||
                            format('(md5(%L)::uuid)', table_record.schema_name || '.' || table_record.table_name || ':' || column_record.attname || ':' || row_number);
                    ELSIF column_record.typname IN ('date') THEN
                        value_expressions := value_expressions || format('(CURRENT_DATE - %s)', row_number - 1);
                    ELSIF column_record.typname IN ('timestamp', 'timestamptz') THEN
                        value_expressions := value_expressions || format('(CURRENT_TIMESTAMP - interval %L)', (row_number - 1) || ' days');
                    ELSIF column_record.typname = 'time' THEN
                        value_expressions := value_expressions || quote_literal('09:00:00');
                    ELSIF column_record.typname IN ('json', 'jsonb') THEN
                        value_expressions := value_expressions || quote_literal(
                            format('{"mock":true,"row":%s,"source":"daedalus"}', row_number)
                        ) || CASE WHEN column_record.typname = 'jsonb' THEN '::jsonb' ELSE '::json' END;
                    ELSIF column_record.typname = 'text'
                       OR column_record.formatted_type LIKE 'character varying%'
                       OR column_record.formatted_type LIKE 'character%'
                    THEN
                        value_expressions := value_expressions || quote_literal(
                            CASE
                                WHEN column_record.attname ILIKE '%email%' THEN format('mock.user.%s@example.test', row_number)
                                WHEN column_record.attname ILIKE '%phone%' THEN format('+1555000%s', lpad(row_number::text, 4, '0'))
                                WHEN column_record.attname ILIKE '%name%' THEN format('Mock User %s', row_number)
                                WHEN column_record.attname ILIKE '%status%' THEN 'active'
                                WHEN column_record.attname ILIKE '%description%' THEN format('Mock description %s', row_number)
                                ELSE format('mock_%s_%s', column_record.attname, row_number)
                            END
                        );
                    ELSIF column_record.typname = 'bytea' THEN
                        value_expressions := value_expressions || quote_literal('mock') || '::bytea';
                    ELSIF column_record.typname = 'inet' THEN
                        value_expressions := value_expressions || format('%L::inet', format('192.0.2.%s', row_number));
                    ELSIF column_record.typname = 'ARRAY' OR column_record.formatted_type LIKE '%[]' THEN
                        value_expressions := value_expressions || format('ARRAY[]::%s', column_record.formatted_type);
                    ELSE
                        -- Unsupported nullable columns may be left empty.
                        value_expressions := value_expressions || 'NULL';
                    END IF;
                END LOOP;

                IF column_names = '' THEN
                    insert_sql := format(
                        'INSERT INTO %I.%I DEFAULT VALUES',
                        table_record.schema_name,
                        table_record.table_name
                    );
                ELSE
                    insert_sql := format(
                        'INSERT INTO %I.%I (%s) VALUES (%s) ON CONFLICT DO NOTHING',
                        table_record.schema_name,
                        table_record.table_name,
                        column_names,
                        value_expressions
                    );
                END IF;

                EXECUTE insert_sql;
                GET DIAGNOSTICS affected_rows = ROW_COUNT;
                inserted := inserted + affected_rows;
            END LOOP;

            INSERT INTO seed_results(schema_name, table_name, inserted_rows, status)
            VALUES (table_record.schema_name, table_record.table_name, inserted, 'inserted');
        EXCEPTION WHEN OTHERS THEN
            INSERT INTO seed_results(schema_name, table_name, inserted_rows, status, detail)
            VALUES (table_record.schema_name, table_record.table_name, inserted, 'skipped', SQLERRM);
        END;
    END LOOP;
END
$seed$;

SELECT schema_name, table_name, inserted_rows, status, detail
FROM seed_results
ORDER BY schema_name, table_name;

COMMIT;
