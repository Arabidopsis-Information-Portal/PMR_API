# file: request_builder.py
import json
import logging
import service as svc

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

user_params_map = {
  'experimentID' : 'expId',
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
            raise Exception("No experimentID has been submitted!")

    # fill default parameters
    if (type == 'search'):
        for key, value in search_api_param_value_map.iteritems():
            params[key] = value
    else:
        for key, value in list_api_param_value_map.iteritems():
            params[key] = value
    return params
