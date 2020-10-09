import sys
import urllib.request
import json
import ssl
import argparse


parser = argparse.ArgumentParser(description='AWS Service')
parser.add_argument('service', help='AWS service to filter')
args = parser.parse_args()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://ip-ranges.amazonaws.com/ip-ranges.json')
req.add_header('Content-Type','application/json')
result = urllib.request.urlopen(req, context=ctx).read()

prefixes = json.loads(result, encoding='utf-8')
args = parser.parse_args()

cloudfront = [ x['ip_prefix'] for x in prefixes['prefixes'] if x['service'] == args.service]
joined = ','.join(x for x in cloudfront)
export = { 'cidrs': joined }
json.dump(export, sys.stdout)