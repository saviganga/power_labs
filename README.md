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

1. Signup `127.0.0.1:8000/users/account/`
```json
request body

{
    "user_name": "saviganga",
    "password": "xxxxxx",
    "re_password": "xxxxxx"
}
```
<img width="1081" alt="sensors-data-signup" src="https://github.com/user-attachments/assets/023371b7-f15a-4825-9eb7-d19dca24d02e">

2. Login `127.0.0.1:8000/auth/login/`
```json
request body

{
    "username": "saviganga",
    "password": "xxxxxx"
}
```
<img width="1085" alt="sensor-data-login" src="https://github.com/user-attachments/assets/9d878ccd-73fa-4f65-aa00-1e685b22dd67">

3. Get user data `127.0.0.1:8000/users/account/`
This endpoint requires authentication, so update your headers
```json

headers

{
    "Authorization": "JWT {{JWT_TOKEN}}",
}
```


### Sensor data
1. POST `127.0.0.1:8000/sensors/sensor-data/`
```json

request body

{
    "vehicle_id": "gangax",
    "sensor_type": "fuel",
    "sensor_value": "50"
}
```
<img width="1086" alt="post-sensor-data" src="https://github.com/user-attachments/assets/7b03b4cd-8cdc-49e7-9705-2d71fd85b447">


2. GET `127.0.0.1:8000/sensors/sensor-data/`
This endpoint requires authentication, so update your headers
```json

headers

{
    "Authorization": "JWT {{JWT_TOKEN}}",
}
```
<img width="1073" alt="get-sensor-data" src="https://github.com/user-attachments/assets/1ceb66e4-6543-446e-a68a-cd15294223b3">

Additionally, the `GET` response can be filtered based on the following optional fields:
- vehicle_id
- sensor_type
- start_time (ISO 8601 format)
- end_time (ISO 8601 format)

<img width="1083" alt="get-sensor-data-filtered" src="https://github.com/user-attachments/assets/d9c8ef77-9f7f-4ac3-ab64-06b8e8fa0fb2">


