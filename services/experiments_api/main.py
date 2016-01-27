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
Main Module
"""

import requests
import json
import logging
import service as svc
import experiments_service as es
from requests.exceptions import ConnectionError

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# This function acts as a search endpoint
def search(args):
    """Retrieves experiment record by experiment ID
    required parameters: 
    
    experimentID
                
    :rtype: response json
    :return: Returns a response object from the webservice in the json format if success raises exception otherwise
    
    """
    # get search service url
    svc_url = svc.get_search_base_url()

    try:
        # execute request
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

# This function acts as a list endpoint
def list(args):
    """Retrieves a list of all experiments
    no parameters required
                                       
    :rtype: response json
    :return: Returns a response object from the webservice in the json format if success raises exception otherwise
    
    """
    # get list service url
    svc_url = svc.get_list_base_url()

    try:
        # execute request
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
