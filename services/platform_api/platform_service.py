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
Plarform Service API. Provides search, and serialization services
"""

import logging
import request_handler as rh
import exception
import jsonpickle

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# This function retrieves platform record by experiment ID, and platform ID
def get_platform_by_id(url, args):
    """ Retrieve platform record by experiment ID, and platform ID
    validate parameters
    perform platform lookup
    
    :type url: string
    :param url: The service url
      
    :type args: dict
    :param args: The dictionary(map) of parameters submitted via query string 
       
    :rtype: json like string
    :return: Returns Platform as json-like string
    
    """

    # retrieve platform ID from request parameters
    platform_lookup_id = args['platformID']
    
    # retrieve experiment ID from request parameters
    experiment_lookup_id = args['experimentID']

    # get platform lookup ID as integer value
    try:
        int_platform_lookup_id = int(platform_lookup_id)
    except ValueError as e:
            raise Exception("Non integer platform ID was submitted!")

    log.debug("Platform Lookup Id:" + str(int_platform_lookup_id))
    log.debug("Experiment Lookup Id:" + str(experiment_lookup_id))
    
    # get list of Platform objects
    response = get_platform_as_objects(url, args)

    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load platforms to search for platform ID.")

    # search for platform by ID
    lookup_object = find(lambda item: item.platformId == int_platform_lookup_id, response)
    log.debug(lookup_object)

    # raise not found exception if no such platform
    if not lookup_object:
        raise exception.NotFound("No platform found for experimentID/platform ID. " + "ExperimentID:" + str(experiment_lookup_id)+ " PlatformID:" + str(int_platform_lookup_id))

    # transform to json like string
    lookup_object_as_json_string = jsonpickle.encode(lookup_object, unpicklable=False)
    log.debug("JSON deserialization:")
    log.debug(lookup_object_as_json_string)

    return lookup_object_as_json_string

# get all platforms as list of Platforms objects
def get_platform_as_objects(url, args):
    """ Retrieves all platforms as Platform objects by experiment ID
    return  list of Platform objects
    
    :type url: string
    :param url: request url
    
    :type args: string
    :param args: request parameters
      
    :rtype: list
    :return: Returns list of Platform objects if success raises exception otherwise
    
    """
    
    response = rh.loadPlatforms(url, args, 'list')
    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load platforms to search for platform ID.")
    return response

# This function get all platforms by experiment ID in json format
def get_platforms_as_json(url, args):
    """ Retrieves all platforms in json format
    return  platforms in json format
    
    :type url: string
    :param url: request url
    
    :type args: string
    :param args: request parameters
      
    :rtype: list
    :return: Returns list of Platform objects in json format if success raises exception otherwise
    
    """
    
    response = rh.build_payload(url, args, 'list')
    return response

# This function performs an exact search by identifier
def find(f, seq):
   """ Retrieves object by identifier
    return  experiment object
    
    :type f: int
    :param f: current value of identifier 
    
    :type seq: string
    :param seq: value to search for
      
    :rtype: Platform
    :return: Returns Platform object if object found None otherwise
    
    """
   for item in seq:
    if f(item):
      return item
