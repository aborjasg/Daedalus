# Daedalus
A powerful all‑in‑one Cleaning Services SaaS platform that helps cleaning businesses operate smarter, faster, and more profitably. From effortless online booking to automated scheduling, real‑time job tracking, digital checklists, and integrated payments, the platform eliminates manual tasks and elevates the customer experience.

## Repository structure

Daedalus is organized as a monorepo. Each API under `services/` is independently
deployable and owns its application code, migrations, tests, and dependencies.

```text
services/
  auth-api/          Authentication and authorization
  customers-api/     Customer and address management
  bookings-api/      Cleaning booking lifecycle
  scheduling-api/    Staff, availability, and assignments
  jobs-api/          Job execution, checklists, and tracking
  payments-api/      Payment and invoice integration
  notifications-api/ Email, SMS, and in-app notifications
web/                 Flask server-rendered web application
shared/              Small cross-service infrastructure utilities
infrastructure/      Docker Compose, MySQL, and reverse proxy setup
```

Each service follows the same MVC-oriented layout:

```text
app/
  controllers/       Request/response coordination
  models/            SQLAlchemy persistence models
  repositories/      Database access
  routes/            Flask blueprints and URL registration
  schemas/           Request validation and serialization
  services/          Business logic
```
