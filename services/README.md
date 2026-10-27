# Microservices

Each directory is an independently deployable Django API. Services should
communicate over HTTP or asynchronous events and should not access another
service's database tables directly.

## API services

- `auth-api` — authentication and authorization.
- `bookings-api` — cleaning booking lifecycle.
- `customers-api` — customer and address management.
- `jobs-api` — job execution, checklists, and tracking.
- `notifications-api` — email, SMS, and in-app notifications.
- `payments-api` — payment and invoice integration.
- `quotes-api` — Quote Estimator; the public estimate and pricing contracts
  are not defined yet.
- `scheduling-api` — staff, availability, and assignments.
