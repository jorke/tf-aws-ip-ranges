variable "aws_service" {
  description = "AWS service to return cidrs for"
  default     = "CLOUDFRONT"
}

data "external" "ip_ranges" {
  program = ["python3", "${path.module}/ranges.py", var.aws_service]
}

output "cidr_string" {
  description = "List of CIDRs based on service selected"
  value       = data.external.ip_ranges.result.cidrs
}

output "cidr_list" {
  description = "List of CIDRs based on service selected"
  value       = split(",", data.external.ip_ranges.result.cidrs)
}

