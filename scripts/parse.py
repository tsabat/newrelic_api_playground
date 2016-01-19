#!/usr/bin/env python

import requests
import argparse


def metric_data(args):
    url = "https://api.newrelic.com/v2/applications/%s/metrics/data.json"
    url = url % args.application_id
    response = requests.get(url, headers=headers(), params=params(args))

    json = response.json()
    for timeslice in json['metric_data']['metrics'][0]['timeslices']:
        print timeslice['from']
        print timeslice['to']

        for v in timeslice['values']:
            values = timeslice['values']
            print "\t", v, ':',  values[v]

        print ''


def params(args):
    payload = {}
    payload['names[]'] = args.metric_name

    return payload


def headers():
    return {'X-Api-Key': args.api_key}

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
metric_parser = subparsers.add_parser('metric_data')
metric_parser.add_argument('api_key')
metric_parser.add_argument('application_id')
metric_parser.add_argument('metric_name')
metric_parser.set_defaults(func=metric_data)

if __name__ == '__main__':
    args = parser.parse_args()
    print args
    args.func(args)  # call the default function
