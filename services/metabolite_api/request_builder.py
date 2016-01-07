# file: request_builder.py
import json
import logging
import service as svc
import exception

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

user_params_map = {
  'experimentID' : 'expId',
  'platformID' : 'pId',
  'metaboliteID' : 'mId'
  }

search_api_param_value_map = {
    'species' : 'Arabidopsis_thaliana',
}

list_api_param_value_map = {
    'species' : 'Arabidopsis_thaliana',
}

def build_param_map(args, type):
    params = {}

    log.info("Request Type:" + type)

    if not type or not type in ('search', 'list'):
        raise Exception("Incorrect Request Type. Valid Request Types: search, list.")

    # extract required parameters

    # type searh
    if (type == 'search'):
        # experiment ID
        _key_experimentID = 'experimentID'

        if _key_experimentID in args.keys():
            _key_expID = user_params_map[_key_experimentID]
            params[_key_expID] = args[_key_experimentID]
        else:
            raise exception.InvalidParameter("No experimentID has been submitted!")

        # platform ID
        _key_platformID = 'platformID'

        if _key_platformID in args.keys():
            _key_platID = user_params_map[_key_platformID]
            params[_key_platID] = args[_key_platformID]
        else:
            raise exception.InvalidParameter("No platformID has been submitted!")

        # metabolite ID
        _key_metaboliteID = 'metaboliteID'

        if _key_metaboliteID in args.keys():
            _key_metaboliteID = user_params_map[_key_metaboliteID]
            params[_key_metaboliteID] = args[_key_metaboliteID]
        else:
            raise exception.InvalidParameter("No metaboliteID has been submitted!")

    else:
        # experiment ID
        _key_experimentID = 'experimentID'

        if _key_experimentID in args.keys():
            _key_expID = user_params_map[_key_experimentID]
            params[_key_expID] = args[_key_experimentID]
        else:
            raise exception.InvalidParameter("No experimentID has been submitted!")

        # platform ID
        _key_platformID = 'platformID'

        if _key_platformID in args.keys():
            _key_platID = user_params_map[_key_platformID]
            params[_key_platID] = args[_key_platformID]
        else:
            raise exception.InvalidParameter("No platformID has been submitted!")

    # fill default parameters
    if (type == 'search'):
        for key, value in search_api_param_value_map.iteritems():
            params[key] = value
    else:
        for key, value in list_api_param_value_map.iteritems():
            params[key] = value
    return params
