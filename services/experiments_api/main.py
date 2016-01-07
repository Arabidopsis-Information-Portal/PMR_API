# file: main.py

import requests
import json
import logging
import service as svc
import request_handler as rh
import experiments_service as es
from requests.exceptions import ConnectionError

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def search(args):

    svc_url = svc.get_search_base_url()

    try:
         response = es.get_experiment_by_id(svc_url, args)
         print json.dumps(json.loads(response))
         print '---'
    except ValueError as e:
         error_msg = "ValueError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)
    except requests.exceptions.HTTPError as e:
         error_msg = "HTTPError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)
    except ConnectionError as e:
         error_msg = "ConnectionError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)
    except Exception as e:
         error_msg = "GenericError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)

def list(args):
    svc_url = svc.get_list_base_url()

    try:
         response = es.get_experiments_as_json(svc_url, args)
         log.debug("List of Experiments:")
         log.debug(response)
         print json.dumps(response)
         print '---'
    except ValueError as e:
         error_msg = "ValueError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)
    except requests.exceptions.HTTPError as e:
         error_msg = "HTTPError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)
    except ConnectionError as e:
         error_msg = "ConnectionError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)
    except Exception as e:
         error_msg = "GenericError Exception:" + e.message
         log.error(error_msg, exc_info=True)
         raise Exception(error_msg)