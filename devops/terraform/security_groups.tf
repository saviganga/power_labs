
# provision security groups
resource "aws_security_group" "sensor_data_rds_sg" {
  name        = "${var.PROJECT_NAME}_sensor_data_rds_sg"
  description = "Allow TLS inbound traffic from the internet to port 5432"

  ingress {
    description = "Allow all inbound traffic to port 5432"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "${var.PROJECT_NAME}_sensor_data_rds_sg"
  }
}

# print out some output
output "sensor_data_rds_sg_output" {
  value = aws_security_group.sensor_data_rds_sg.name
}
