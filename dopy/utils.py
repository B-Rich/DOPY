import json
import requests
import urlparse

import config

def get_request(endpoint, authentication_token):

    header_and_url = prepare_header_and_url(endpoint, authentication_token)
    response = requests.get(header_and_url["url"], headers=header_and_url["header"])

    return response

def post_request(endpoint, json_data, authentication_token):

    header_and_url = prepare_header_and_url(endpoint, authentication_token)
    header_and_url["header"]["Content-Type"] = "application/json"
    response = requests.post(header_and_url["url"], data=json.dumps(json_data), headers=header_and_url["header"])

    return response

def put_request(endpoint, data, authentication_token):

    header_and_url = prepare_header_and_url(endpoint, authentication_token)
    header_and_url["header"]["Content-Type"] = "application/x-www-form-urlencoded"
    response = requests.put(header_and_url["url"], data=data, headers=header_and_url["header"])

    return response 

def delete_request(endpoint, authentication_token):

    header_and_url = prepare_header_and_url(endpoint, authentication_token)
    header_and_url["header"]["Content-Type"] = "application/x-www-form-urlencoded"
    response = requests.delete(header_and_url["url"], headers=header_and_url["header"])

    return response


def format_header_with_token(authentication_token):

    header = config.API_HEADER
    header["Authorization"] = header["Authorization"].format(TOKEN=authentication_token)

    return header

def prepare_header_and_url(endpoint, authentication_token):

    header = format_header_with_token(authentication_token)
    url = urlparse.urljoin(config.API_HOST, endpoint)

    return {"header": header, "url": url}
