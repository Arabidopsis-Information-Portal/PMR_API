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
Metabolite Service API. Provides search, and serialization services
"""

import logging
import request_handler as rh
import exception
import jsonpickle

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# This function retrieves metabolite record by experiment ID, platform ID, and metabolite ID
def get_metabolite_by_id(url, args):
    """ Retrieve metabolite record by experiment ID, platform ID, and metabolite ID
    validate parameters
    perform metabolite lookup
    
    :type url: string
    :param url: The service url
      
    :type args: dict
    :param args: The dictionary(map) of parameters submitted via query string 
       
    :rtype: json like string
    :return: Returns Metabolite as json-like string
    
    """

     # retrieve platform ID from request parameters
    platform_lookup_id = args['platformID']
    
    # retrieve experiment ID from request parameters
    experiment_lookup_id = args['experimentID']
    
    # retrieve metabolite ID from request parameters
    metabolite_lookup_id = args['metaboliteID']

    # get metabolite lookup ID as integer value
    try:
        int_metabolite_lookup_id = int(metabolite_lookup_id)
    except ValueError as e:
            raise Exception("Non integer metabolite ID has been submitted!")

    log.debug("Platform Lookup Id:" + str(platform_lookup_id))
    log.debug("Experiment Lookup Id:" + str(experiment_lookup_id))
    log.debug("Metabolite Lookup Id:" + str(int_metabolite_lookup_id ))
    
    # get list of Metabolite objects
    response = get_metabolite_as_objects(url, args)

    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load platforms to search for platform ID.")

    # search for metabolite by ID
    lookup_object = find(lambda item: item.mId == int_metabolite_lookup_id, response)
    log.debug(lookup_object)

    # raise not found exception if no such metabolite
    if not lookup_object:
        raise exception.NotFound("No metabolite found for given experimentID/platform ID/metabolite ID. " + "ExperimentID:" + str(experiment_lookup_id)+ " PlatformID:" + str(int_platform_lookup_id) + " Metabolite:" + str(int_metabolite_lookup_id))

    # transform to json like string
    lookup_object_as_json_string = jsonpickle.encode(lookup_object, unpicklable=False)
    log.debug("JSON deserialization:")
    log.debug(lookup_object_as_json_string)

    return lookup_object_as_json_string

# get all metabolites as list of Metabolites objects
def get_metabolite_as_objects(url, args):
    """ Retrieves all metabolites as Metabolite objects by experiment ID, and paltform ID
    return  list of Platform objects
    
    :type url: string
    :param url: request url
    
    :type args: string
    :param args: request parameters
      
    :rtype: list
    :return: Returns list of Metabolite objects if success raises exception otherwise
    
    """
    response = rh.loadMetabolites(url, args, 'list')
    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load metabolites to search for metabolite ID.")
    return response

# This function get all metabolites by experiment ID, and platform ID in json format
def get_metabolites_as_json(url, args):
    """ Retrieves all metabolites in json format
    return  platforms in json format
    
    :type url: string
    :param url: request url
    
    :type args: string
    :param args: request parameters
      
    :rtype: list
    :return: Returns list of Metabolite objects in json format if success raises exception otherwise
    
    """
    response = rh.build_payload(url, args, 'list')
    return response

# This function performs an exact search by identifier
def find(f, seq):
    """ Retrieves object by identifier
    return  metabolite object
    
    :type f: int
    :param f: current value of identifier 
    
    :type seq: string
    :param seq: value to search for
      
    :rtype: Platform
    :return: Returns Metabolite object if object found None otherwise
    
    """
    for item in seq:
     if f(item):
      return item
