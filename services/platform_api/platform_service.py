# file: platform_service.py

import json
import logging
from collections import namedtuple
import request_handler as rh
import exception
import jsonpickle

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def get_platform_by_id(url, args):

    platform_lookup_id = args['platformID']
    experiment_lookup_id = args['experimentID']

    # get platform lookup ID
    try:
        int_platform_lookup_id = int(platform_lookup_id)
    except ValueError as e:
            raise Exception("Non integer platform ID was submitted!")

    log.debug("Platform Lookup Id:" + str(int_platform_lookup_id))
    log.debug("Experiment Lookup Id:" + str(experiment_lookup_id))
    response = get_platform_as_objects(url, args)

    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load platforms to search for platform ID.")

    lookup_object = find(lambda item: item.platformId == int_platform_lookup_id, response)
    log.debug(lookup_object)

    # raise not found exception if no such platform
    if not lookup_object:
        raise exception.NotFound("No platform found for experimentID/platform ID. " + "ExperimentID:" + str(experiment_lookup_id)+ " PlatformID:" + str(int_platform_lookup_id))

    lookup_object_as_json_string = jsonpickle.encode(lookup_object, unpicklable=False)
    log.debug("JSON deserialization:")
    log.debug(lookup_object_as_json_string)

    return lookup_object_as_json_string

def get_platform_as_objects(url, args):
    response = rh.loadPlatforms(url, args, 'list')
    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load platforms to search for platform ID.")
    return response

def get_platforms_as_json(url, args):
    response = rh.build_payload(url, args, 'list')
    return response

def find(f, seq):
   for item in seq:
    if f(item):
      return item
