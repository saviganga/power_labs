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


### Infrastructure

The cloud infrastructure for this service is AWS.

Since the application is containerized, it is hosted on AWS Elastic Cluster Service (FARGATE) saving cost on virtual machine resource management. 

The ECS sits behind a loadbalancer, allowing only traffic from the load balancer, and denying access from the public internet

### Infrastructure as Code

Terraform is used to define the infrastructure on AWS

- ./devops/terraform/:
    
    - providers.tf: Declares the providers that Terraform will use, and defines the backend (AWS S3) where Terraform will store the state of our infrastructure.
    
    - vars.tf: Contains variables for the Terraform configuration.
    
    - security_groups.tf: Contains Terraform configurations to provision ingress and egress rules for the provisioned resources.
    
    - alb.tf: Contains Terraform configurations to provision an Application Load Balancer, a target group, and a listener.
    
    - db.tf: Contains Terraform configurations to provision the database.
    
    - ecs.tf: Contains Terraform configurations to provision the ECS infrastructure (cluster, service, task definitions, etc)
    
    - iam.tf: Contains terraform configurations to provision iam roles and policies for the cloud infrastructure
    
    - vpc.tf: contains terraform configurations to fetch cloud VPC information


### Configuration Management

Ansible is used to configure the application on the provisioned infrastructure. The ansible script is run from the CICD pipeline, ensuring the application is up to date with its latest image on every push to the branch

- ./devops/ansible/:
    
    - ./playbooks/update_ecs_task.yaml: Updates the AWS ECS task definition and service with the application's latest image.


### CI/CD

The CICD pipeline is built with GitHub Actions. It builds the new application image, and either updates the AWS infrastructure or the application on the infrastructure depending on the branch that is pushed to

- The infrastructure pipeline is triggered when there is a push to the `devops` branch. When there is a push to that branch, the terraform build is triggered, and the infrastructure is updated (if any changes).

- The application image pipeline is triggered when there is a push to the `ganga` branch. When there is a push to that branch, the ansible build is triggered, and the ECS cluster is updated with the new application image.



