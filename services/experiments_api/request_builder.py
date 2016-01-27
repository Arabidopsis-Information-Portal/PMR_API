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
Builds Request Parameters from a query string
"""

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# mapping between external user visible API parameters and underlying webservice
USER_PARAMS_MAP = {
  'experimentID' : 'expId',
  }

# internal default parameters for the serch endpoint
SEARCH_API_PARAM_VALUE_MAP = {
    'species' : 'Arabidopsis_thaliana',
}

# internal default parameters for the serch endpoint
LIST_API_PARAM_VALUE_MAP = {
    'species' : 'Arabidopsis_thaliana',
}

# This function builds a parameter map to pass to the underlying webservice
def build_param_map(args, request_type):
    """Build a parameter map,
    add default parameters
    validate parameters/values
    match passed parameters by name with parameters of the underlying service
        
    :type args: dict
    :param args: The dictionary(map) of parameters submitted via query string 
    
    :type request_type: string
    :param request_type: The request request_type: must be one of those: list or search 
  
    
    :rtype: string
    :return: Returns parameter map that matches to the underlying webservice
    
    """
    params = {}

    log.debug("Request Type:" + request_type)

    if not request_type or not request_type in ('search', 'list'):
        raise Exception("Incorrect Request Type. Valid Request Types: search, list.")

    # extract required parameters

    # request_type searh
    if (request_type == 'search'):
        # experiment ID
        _key_experimentID = 'experimentID'

        if _key_experimentID in args.keys():
            _key_expID = USER_PARAMS_MAP[_key_experimentID]
            params[_key_expID] = args[_key_experimentID]
        else:
            raise Exception("No experimentID has been submitted!")

    # fill default parameters
    if (request_type == 'search'):
        for key, value in SEARCH_API_PARAM_VALUE_MAP.iteritems():
            params[key] = value
    else:
        for key, value in LIST_API_PARAM_VALUE_MAP.iteritems():
            params[key] = value
    return params
