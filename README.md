# Flask Application with MongoDB and CI/CD Pipeline

## Overview

This project implements a Flask web application with MongoDB integration. It includes unit tests for the application’s routes and database operations, and the tests are automatically run using GitHub Actions whenever code is pushed to the repository.

## Unit Tests

### 1. Route Test
- **Test Purpose:** Ensure that the `/products` route returns a `405` status code when an invalid method (e.g., `POST`) is used.
- **Test Logic:** The test sends a `POST` request to `/products` and verifies that the server returns a `405 Method Not Allowed` status code.

### 2. Database Read Test
- **Test Purpose:** Ensure that the MongoDB connection is working by performing a ping to the MongoDB server.
- **Test Logic:** The test attempts to send a `ping` command to MongoDB, and if the connection is successful, the test passes.

### 3. Database Write Test
- **Test Purpose:** Ensure that documents can be inserted into the MongoDB database.
- **Test Logic:** The test inserts a product into the `products` collection and verifies that the document is successfully stored in the database.

## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions, which automates the process of:
1. Installing dependencies.
2. Running unit tests.
3. Uploading test results as artifacts.

### Pipeline Workflow
- **Trigger:** The pipeline runs automatically on any `push` or `pull request` to the `main` branch.
- **Steps:**
  1. Checkout the repository.
  2. Set up Python and install dependencies from `requirements.txt`.
  3. Run the unit tests located in the `tests/` directory.
  4. Upload the test results as artifacts (optional).

The CI/CD pipeline ensures that the application is continuously tested with every change, helping maintain code quality.

## GitHub Repository

You can access the full project and its GitHub Actions configuration [here](insert-repo-link).

