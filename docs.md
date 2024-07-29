# API Documentation

This guide provides detailed information on how to interact with the APIs, including endpoints for user authentication and sensor data management. Ensure you have the appropriate authentication tokens before making requests to secure endpoints.

## APIs Overview

### Authentication
The application uses JWT Authentication for secure access to specific endpoints

#### 1. Signup
This endpoint allows users to create a new account.

- **Endpoint**: `127.0.0.1:8000/users/account/`
- **Method**: POST

**Request Body:**
```json
{
    "user_name": "saviganga",
    "password": "xxxxxx",
    "re_password": "xxxxxx"
}
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


