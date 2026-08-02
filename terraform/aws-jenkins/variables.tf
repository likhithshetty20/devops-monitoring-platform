variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 Instance Type"
  type        = string
  default     = "c7i-flex.large"
}

variable "instance_name" {
  description = "EC2 Name"
  type        = string
  default     = "jenkins-server"
}

variable "key_name" {
  description = "AWS Key Pair Name"
  type        = string
}
