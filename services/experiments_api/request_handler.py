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
import experiment as exp

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# This function executes a request passing parameters to the underlying webservice
def handle_request(url, token, params, **kwargs):
    """Executes a request,
    pass parameters and optional parameters
    
    :type url: string
    :param url: request url
    
    :type token: string
    :param token: ARAPORT API token (internal parameter)
    
    :type params: string
    :param params: request parameters
    
    :type kwargs: string
    :param kwargs: optional request parameters
    
    :rtype: response json
    :return: Returns a response object from the webservice in the json format if success raises exception otherwise
    
    """
    headers = {}
    
    # extract internal parameter token form the request header
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
    transformed_params = rb.build_param_map(params, type)
    log.debug("Transformed_params: {0}".format(transformed_params))
    
    # execute a request by passing completely mapped and validated request parameters
    response = requests.get(url, params=transformed_params)
    log.debug("Response Text:")
    log.debug(response.text)
    
    # Raise exception and abort if requests is not successful
    response.raise_for_status()
    
    # convert received response (json like string) in a valid json object
    parsed_response = json.loads(response.text)
    return parsed_response

# This functions retrieves all available experiments
def loadExperiments(url, params, request_type, **kwargs):
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
    :return: Returns actual response payload: list of experiments from the webservice in the json format if success raises exception otherwise
    
    """
    # build  request parameters, set defaults, map external parameters
    transformed_params = rb.build_param_map(params, request_type)
    log.debug("Transformed_params: {0}".format(transformed_params))
    
    # execute a request by passing completely mapped and validated request parameters
    response = requests.get(url, params=transformed_params)
    log.debug("Response Text:")
    log.debug(response.text)
    
    # Raise exception and abort if requests is not successful
    response.raise_for_status()
    experiments = json.loads(response.text, object_hook=lambda x: exp.Experiment(**x))
    return experiments
