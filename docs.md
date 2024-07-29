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
```
<img width="1081" alt="sensors-data-signup" src="https://github.com/user-attachments/assets/023371b7-f15a-4825-9eb7-d19dca24d02e">



#### 2. Login
This endpoint allows users to login to their accounts.

- **Endpoint**: `127.0.0.1:8000/auth/login/`
- **Method**: POST

**Request Body:**
```json
{
    "username": "saviganga",
    "password": "xxxxxx"
}
```
<img width="1085" alt="sensor-data-login" src="https://github.com/user-attachments/assets/9d878ccd-73fa-4f65-aa00-1e685b22dd67">



#### 3. Get user data
This endpoint allows users to view their user account information.

- **Endpoint**: `127.0.0.1:8000/users/account/`
- **Method**: GET
- **Authorization**: true

**Request Headers:**
```json
{
    "JWT": "JWT {{jwt_token}}"
}
```




### Sensor data


#### 1. Post sensor data
This endpoint allows users to post vehicle sensor data.

- **Endpoint**: `127.0.0.1:8000/sensors/sensor-data/`
- **Method**: POST
- **Authorization**: false

**Request body:**
```json
{
    "vehicle_id": "gangax",
    "sensor_type": "fuel",
    "sensor_value": "50"
}
```
<img width="1086" alt="post-sensor-data" src="https://github.com/user-attachments/assets/7b03b4cd-8cdc-49e7-9705-2d71fd85b447">



#### 2. Get sensor data
This endpoint allows users to get vehicle sensor data.

- **Endpoint**: `127.0.0.1:8000/sensors/sensor-data/`
- **Method**: GET
- **Authorization**: true

**Request headers:**
```json
{
    "JWT": "JWT {{jwt_token}}"
}
```
<img width="1073" alt="get-sensor-data" src="https://github.com/user-attachments/assets/1ceb66e4-6543-446e-a68a-cd15294223b3">


Additionally, the `GET` sensors data response can be filtered based on the following optional fields:
- vehicle_id
- sensor_type
- start_time (ISO 8601 format)
- end_time (ISO 8601 format)

<img width="1083" alt="get-sensor-data-filtered" src="https://github.com/user-attachments/assets/d9c8ef77-9f7f-4ac3-ab64-06b8e8fa0fb2">



# Infrastructure and Deployment

## Cloud Infrastructure

The cloud infrastructure for this service is hosted on AWS. Key components include:

- **Containerization**: The application is containerized and runs on AWS Elastic Container Service (ECS) with Fargate. This setup reduces costs associated with virtual machine resource management.
- **Load Balancer**: The ECS cluster is positioned behind an Application Load Balancer (ALB), which restricts access to traffic from the load balancer only, blocking direct public internet access.

## Infrastructure as Code

Terraform is utilized for defining and managing the infrastructure on AWS. The configuration files are located in `./devops/terraform/`:

- **`providers.tf`**: Declares the Terraform providers and defines the backend (AWS S3) for storing the Terraform state.
- **`vars.tf`**: Contains variables used in the Terraform configuration.
- **`security_groups.tf`**: Configures ingress and egress rules for the resources.
- **`alb.tf`**: Provisions the Application Load Balancer, including its target group and listener.
- **`db.tf`**: Sets up the database configuration.
- **`ecs.tf`**: Manages the ECS infrastructure, including the cluster, service, and task definitions.
- **`iam.tf`**: Defines IAM roles and policies for the cloud infrastructure.
- **`vpc.tf`**: Configures and retrieves VPC information.

## Configuration Management

Ansible is used for configuring the application on the provisioned infrastructure. The Ansible script runs from the CI/CD pipeline, ensuring the application is updated with the latest image on every push to the branch.

- **`./devops/ansible/playbooks/update_ecs_task.yaml`**: Updates the AWS ECS task definition and service with the latest application image.

## CI/CD Pipeline

The CI/CD pipeline is built using GitHub Actions and consists of two main pipelines:

1. **Infrastructure Pipeline**:
   - **Trigger**: Activates on a push to the `devops` branch.
   - **Action**: Runs Terraform to build and update the infrastructure if there are any changes.

2. **Application Image Pipeline**:
   - **Trigger**: Activates on a push to the `ganga` branch.
   - **Action**: Runs Ansible to update the ECS cluster with the new application image.

This setup ensures that infrastructure changes and application updates are managed efficiently and deployed automatically based on branch activity.
