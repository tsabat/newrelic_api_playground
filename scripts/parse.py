#!/usr/bin/env python

import requests, argparse


def metric_data(args):
    url = "https://api.newrelic.com/v2/applications/%s/metrics/data.json" % args.application_id
    response = requests.get(url, headers=headers(), params=params())

    json =  response.json()
    print json
    print len(json['metric_data']['metrics'][0]['timeslices'])

def params():
    payload            = {}
    payload['names[]'] = 'ActiveRecord/all'
    payload['from']    = '2016-01-11T13:08:55+00:00'
    payload['to']      = '2016-01-11T13:08:56+00:00'

    return payload

def headers():
    return {'X-Api-Key': args.api_key}

parser        = argparse.ArgumentParser()
subparsers    = parser.add_subparsers()
metric_parser = subparsers.add_parser('metric_data')
metric_parser.add_argument('application_id')
metric_parser.add_argument('api_key')
metric_parser.set_defaults(func=metric_data)

if __name__ == '__main__':
    args = parser.parse_args()
    print args
    args.func(args)  # call the default function


