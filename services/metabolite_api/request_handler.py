# file: request_builder.py

import requests
import json
import logging
import request_builder as rb
import metabolite as ml
import exception

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def handle_request(url, token, params, **kwargs):

    headers = {}
    if token:
        headers["Authorization"] = "Bearer %s" % token
    response = requests.get(url, headers=headers, params=params)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    try:
        # Try to convert result to JSON
        # abort if not possible
        return response.json()
    except ValueError:
        raise Exception('not a JSON object: {}'.format(response.text))

def build_payload(url, params, type, **kwargs):
    log.debug("Payload request type:" + type)
    transformed_params = rb.build_param_map(params, type)
    log.info("Transformed_params: {0}".format(transformed_params))
    r = requests.get(url, params=transformed_params)
    log.debug("Response Text:")
    log.debug(r.text)

    r.raise_for_status()
    parsed_response = json.loads(r.text)
    return parsed_response

def loadMetabolites(url, params, type, **kwargs):
    transformed_params = rb.build_param_map(params, type)
    log.info("Transformed_params: {0}".format(transformed_params))
    r = requests.get(url, params=transformed_params)
    log.debug("Response Text:")
    log.debug(r.text)

    r.raise_for_status()

    #try:
    metabolites = json.loads(r.text, object_hook=lambda x: ml.Metabolite(**x))
    #except Exception as e:
    #        error_msg = "There are no information of metabolite for a experimentID/platformID submitted!"
    #        raise exception.NotFound(error_msg)

    return metabolites
