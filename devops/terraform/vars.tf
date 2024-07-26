variable "REGION" {
  default = "us-east-1"
}

variable "PROJECT_NAME" {
  type    = string
  default = "power-labs"

}

variable "db_password" {
  type        = string
  description = "database password"
  sensitive   = true
}

variable "db_user" {
  type        = string
  description = "database user"
}

variable "DB_ENGINE" {
  type    = string
  default = "postgres"
}

variable "DB_ENGINE_VERSION" {
  type    = string
  default = "16.1"
}

variable "DB_ALOCATED_STORAGE" {
  type    = number
  default = 5
}


variable "DB_INSTANCE_CLASS" {
  type    = string
  default = "db.t3.micro"
}


variable "DB_NAME" {
  type    = string
  default = "sensor_data"
}


variable "ALB_TARGET_GROUP_PORT" {
  type    = number
  default = 80
}


variable "ALB_TARGET_GROUP_PROTOCOL" {
  type    = string
  default = "HTTP"
}


variable "ALB_TARGET_GROUP_TARGET_TYPE" {
  type    = string
  default = "ip"
}


variable "ALB_TARGET_GROUP_HEALTH_CHECK_PATH" {
  type    = string
  default = "/"
}


variable "ALB_LISTENER_PORT" {
  type    = number
  default = 80
}


variable "ALB_LISTENER_PROTOCOL" {
  type    = string
  default = "HTTP"
}

