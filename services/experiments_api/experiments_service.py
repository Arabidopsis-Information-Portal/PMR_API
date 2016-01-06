# file: experimments_service.py

import json
import logging
from collections import namedtuple
import request_handler as rh
import experiment as exp
import exception
import jsonpickle

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def get_experiment_by_id(url, args):

    lookup_id = args['experimentID']

    try:
        int_lookup_id = int(lookup_id)
    except ValueError:
        raise Exception("Non integer experiment ID was submitted!")

    log.debug("Experiment Lookup Id:" + str(lookup_id))
    response = get_experiment_as_objects(url, args)

    if not response:
        raise Exception ("Error ocurred. Cannot load experiments to search for experiment ID.")

    lookup_object = find(lambda item: item.expId == int_lookup_id, response)
    log.debug(lookup_object)

    # raise not found exception if no such experiment
    if not lookup_object:
        raise exception.NotFound("No experiment found for experiment ID: " + str(lookup_id))

    lookup_object_as_json_string = jsonpickle.encode(lookup_object, unpicklable=False)
    log.debug("JSON deserialization:")
    log.debug(lookup_object_as_json_string)

    return lookup_object_as_json_string

def get_experiment_as_objects(url, args):
    response = rh.loadExperiments(url, args, 'list')
    if not response:
        raise Exception ("Error ocurred. Cannot load list of experiments.")
    return response

def get_experiments_as_json(url, args):
    response = rh.build_payload(url, args, 'list')
    return response

def find(f, seq):
   for item in seq:
    if f(item):
      return item
