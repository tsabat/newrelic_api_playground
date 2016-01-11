#!/usr/bin/env python

import requests, argparse


def metric_data(args):
    headers = {'X-Api-Key': args.api_key}
    payload = {'names[]': 'ActiveRecord/all'}

    print args
    # url = "https://api.newrelic.com/v2/applications/%/metrics/data.json" % args.application_id
    url = "https://api.newrelic.com/v2/applications/%s/metrics/data.json" % args.application_id
    print url

    response = requests.get(url, headers=headers, params=payload)
    print response.json()

parser        = argparse.ArgumentParser()
subparsers    = parser.add_subparsers()
metric_parser = subparsers.add_parser('metric_data')
metric_parser.add_argument('application_id')
metric_parser.add_argument('api_key')
metric_parser.set_defaults(func=metric_data)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function


