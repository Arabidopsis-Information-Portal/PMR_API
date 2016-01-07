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

def get_metabolite_by_id(url, args):

    platform_lookup_id = args['platformID']
    experiment_lookup_id = args['experimentID']
    metabolite_lookup_id = args['metaboliteID']

    # get metabolite lookup ID
    try:
        int_metabolite_lookup_id = int(metabolite_lookup_id)
    except ValueError as e:
            raise Exception("Non integer metabolite ID has been submitted!")

    log.debug("Platform Lookup Id:" + str(platform_lookup_id))
    log.debug("Experiment Lookup Id:" + str(experiment_lookup_id))
    log.debug("Metabolite Lookup Id:" + str(int_metabolite_lookup_id ))

    response = get_metabolite_as_objects(url, args)

    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load platforms to search for platform ID.")

    lookup_object = find(lambda item: item.mId == int_metabolite_lookup_id, response)
    log.debug(lookup_object)

    # raise not found exception if no such metabolite
    if not lookup_object:
        raise exception.NotFound("No metabolite found for given experimentID/platform ID/metabolite ID. " + "ExperimentID:" + str(experiment_lookup_id)+ " PlatformID:" + str(int_platform_lookup_id) + " Metabolite:" + str(int_metabolite_lookup_id))

    lookup_object_as_json_string = jsonpickle.encode(lookup_object, unpicklable=False)
    log.debug("JSON deserialization:")
    log.debug(lookup_object_as_json_string)

    return lookup_object_as_json_string

def get_metabolite_as_objects(url, args):
    response = rh.loadMetabolites(url, args, 'list')
    if not response:
        raise exception.EmptyResponse("Empty response received. Cannot load metabolites to search for metabolite ID.")
    return response

def get_metabolites_as_json(url, args):
    response = rh.build_payload(url, args, 'list')
    return response

def find(f, seq):
   for item in seq:
    if f(item):
      return item
