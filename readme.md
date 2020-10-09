# terraform module - aws ip ranges

quick and dirty module to get a range of ips for an aws service 

## usage

```
module "cloudfront_ips" {
  source = "./aws-ip-ranges"
  aws_service = "CLOUDFRONT"
}
```
