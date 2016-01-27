# PMR WebServices
# Copyright (C) 2016  Manhoi Hur, Belyaeva, Irina

# This file is part of PMR WebServices API.
#
# PMR API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# PMR API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with PMR API.  If not, see <http://www.gnu.org/licenses/>.


"""
Executes Request and Builds Response Payload returned to a web-client
"""

import requests
import json
import logging
import request_builder as rb
import metabolite as ml


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

# This builds a payload returned to a web-client in response of received request
def build_payload(url, params, type, **kwargs):
    """Build response payload for a request,
    pass parameters and optional parameters
    send external parameters for mapping and validation
    parse json like string
    return json object
    
    :type url: string
    :param url: request url
    
    :type params: string
    :param params: request parameters
    
    :type kwargs: string
    :param kwargs: optional request parameters
    
    :rtype: response json
    :return: Returns actual response payload from the webservice in the json format if success raises exception otherwise
    
    """
    # build  request parameters, set defaults, map external parameters
    log.debug("Payload request type:" + type)
    transformed_params = rb.build_param_map(params, type)
    log.debug("Transformed_params: {0}".format(transformed_params))
    
    # execute a request by passing completely mapped and validated request parameters
    response = requests.get(url, params=transformed_params)
    log.debug("Response Text:")
    log.debug(response.text)

    # Raise exception and abort if request is not successful
    response.raise_for_status()
    
    # convert received response (json like string) in a valid json object
    parsed_response = json.loads(response.text)
    return parsed_response

# This functions retrieves all available metabolites for a given experiment ID, and platform ID
def loadMetabolites(url, params, type, **kwargs):
    """Build response payload for a request,
    pass parameters and optional parameters
    send external parameters for mapping and validation
    parse json like string
    return json object
    
    :type url: string
    :param url: request url
    
    :type params: string
    :param params: request parameters
    
    :type kwargs: string
    :param kwargs: optional request parameters
    
    :rtype: response json
    :return: Returns actual response payload: list of all metabolites for a given experiment ID, and platform ID from the webservice in the json format if success raises exception otherwise
    
    """
    # build  request parameters, set defaults, map external parameters
    transformed_params = rb.build_param_map(params, type)
    log.debug("Transformed_params: {0}".format(transformed_params))
    
    # execute a request by passing completely mapped and validated request parameters
    response = requests.get(url, params=transformed_params)
    log.debug("Response Text:")
    log.debug(response.text)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    metabolites = json.loads(response.text, object_hook=lambda x: ml.Metabolite(**x))

    return metabolites
