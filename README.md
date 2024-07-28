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

A `.env.example` file has been added to the repository. You should create a `.env` file and fill in the required fields with your values to configure your environment. The `ENVIRONMENT` and `UPTRACE_DSN` fields have been prefilled to suit the configurations on the application.

## Run the project

1. Clone the repository
```bash
git clone git@github.com:saviganga/power_labs.git
```

2. Set up your `.env` file
```bash
cd power_labs/
cp ./power_labs/.env.example ./power_labs/.env
```
Fill the .env file with your values

3. Build the project using `docker-compose`
```bash
docker-compose build
```

4. After the build is completed, start the project with `docker-compose`
```bash
docker-compose up
```

5. Test connectivity by making a `GET` request on postman on this endpont `http://127.0.0.1:8000/sensors/sensor-data/health/' or running this command in a new terminal
```bash
curl http://127.0.0.1:8000/sensors/sensor-data/health/

# response
{"status":"SUCCESS","message":"Success"}
```

6. Run database migrations: To complete the setup, run the database migrations. In another terminal tab, while your app is still runnung, run the following command
```bash
docker exec -it sensors-backend python3 manage.py migrate
```


## APIS

### Authentication
Some endpoints require authentication for access. The application uses JWT Authentication.

1. Signup
![Sign up request and response]<img width="1081" alt="sensors-data-signup" src="https://github.com/user-attachments/assets/023371b7-f15a-4825-9eb7-d19dca24d02e">




