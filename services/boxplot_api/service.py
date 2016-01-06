# file: service.py

import os.path as op
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def get_svc_base_url():
    return 'http://pmr-webapi.gdcb.iastate.edu/pmrWebApi/api/v1/boxplot/list'
