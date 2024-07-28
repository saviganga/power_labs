# power_labs

You are tasked with developing a backend service for a fleet management software system. This service will collect, store, and process data from field sensors installed on vehicles. Additionally, you will set up a CI/CD pipeline and deploy the backend service to a cloud platform. Use an IaC tool (e.g., Terraform) to define your cloud infrastructure.

Detailed documentation of your solution, including setup instructions, API documentation, and infrastructure configuration is required.

## Setup

### Prerequisites

To run the development environment, you need to have the following installed:

- **Django**
- **Docker**
- **Docker Compose**
- **Environment Variables**

### Environment Variables

A `.env.example` file has been added to the repository. You should create a `.env` file and fill in the required fields with your values to configure your environment.

Example:
```.env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
DEBUG=True