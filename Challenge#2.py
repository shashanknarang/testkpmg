#!/usr/bin/env python3

import base64
import json
import re
import subprocess

import requests

imds_server_base_url = "http://169.254.169.254"

instance_api_version = "2021-02-01"
instance_endpoint = imds_server_base_url + "/metadata/instance?api-version=" + instance_api_version

filter_compute_key = imds_server_base_url + "/metadata/instance/compute?api-version=" + instance_api_version

filter_network_key = imds_server_base_url + "/metadata/instance/network/interface/0?api-version=" + instance_api_version

def api_call(endpoint):
    headers={'Metadata': 'True'}
    json_obj = requests.get(endpoint, headers=headers, proxies=proxies).json()
    return json_obj

def main():
    # Instance provider API call
    instance_json = api_call(instance_endpoint)
    print("Instance provider data:")
    pretty_print_json_obj_to_terminal(instance_json)

    compute_json = api_call(filter_compute_key)
    print("Instance provider data:")
    pretty_print_json_obj_to_terminal(compute_json)

    network_json = api_call(filter_network_key)
    print("Instance provider data:")
    pretty_print_json_obj_to_terminal(network_json)


def pretty_print_json_obj_to_terminal(json_obj):
    print(json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    main()