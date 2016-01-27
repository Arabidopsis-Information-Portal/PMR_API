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
Experiments Service API. Provides search, and serialization sevices
"""

import logging
from collections import namedtuple
import request_handler as rh
import experiment as exp
import exception
import jsonpickle

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# This function retrieves experiment record by experiment ID
def get_experiment_by_id(url, args):
    """ Retrieve experiment record by experiment ID
    from passed service url and parameters
    validate parameters
    perform experiment lookup
    
    :type url: string
    :param url: The service url
      
    :type args: dict
    :param args: The dictionary(map) of parameters submitted via query string 
       
    :rtype: json like string
    :return: Returns Experiment as json-like string
    
    """
   
    # retrieve experiment ID from request parameters
    lookup_id = args['experimentID']

    try:
        int_lookup_id = int(lookup_id)
    except ValueError:
        raise Exception("Non integer experiment ID was submitted!")

    log.debug("Experiment Lookup Id:" + str(lookup_id))
    
    # get list of Experiment objects
    response = get_experiment_as_objects(url, args)

    if not response:
        raise Exception ("Error ocurred. Cannot load experiments to search for experiment ID.")

    # search for experiment by ID
    lookup_object = find(lambda item: item.expId == int_lookup_id, response)
    log.debug(lookup_object)

    # raise not found exception if no such experiment
    if not lookup_object:
        raise exception.NotFound("No experiment found for experiment ID: " + str(lookup_id))

    # transform to json like string
    lookup_object_as_json_string = jsonpickle.encode(lookup_object, unpicklable=False)
    log.debug("JSON deserialization:")
    log.debug(lookup_object_as_json_string)

    return lookup_object_as_json_string

# get all experiments as list of Experiment objects
def get_experiment_as_objects(url, args):
    """ Retrieves all experiments as Experiment objects
    return  list of Experiment objects
    
    :type url: string
    :param url: request url
    
    :type args: string
    :param args: request parameters
      
    :rtype: list
    :return: Returns list of Experiment objects if success raises exception otherwise
    
    """
    response = rh.loadExperiments(url, args, 'list')
    if not response:
        raise Exception ("Error ocurred. Cannot load list of experiments.")
    return response

# This function get all experiments in json format
def get_experiments_as_json(url, args):
    """ Retrieves all experiments in json format
    return  experiments in json format
    
    :type url: string
    :param url: request url
    
    :type args: string
    :param args: request parameters
      
    :rtype: list
    :return: Returns list of Experiment objects in json format if success raises exception otherwise
    
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
      
    :rtype: Experiment 
    :return: Returns Experiment object if object found None otherwise
    
    """
    for item in seq:
     if f(item):
       return item
