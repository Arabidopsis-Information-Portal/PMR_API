import requests
import logging
import request_builder as rb
import main as driver
from requests.exceptions import ConnectionError

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def main():
    """test logic for when running this module as the primary one!"""

    ## pass the namespace you test again (your dev namespace or production)
    test_namespace = 'ibelyaev-dev'

    #search
    args = {'experimentID': '106', 'platformID':'100', '_url': 'https://api.araport.org/community/v0.3', '_namespace': test_namespace}
    driver.search(args)
    param_map = rb.build_param_map(args, 'search')
    log.info("Param Map:")
    log.info(param_map)

    # list
    args = {'experimentID': '106', '_url': 'https://api.araport.org/community/v0.3', '_namespace': test_namespace}
    driver.list(args)
   

if __name__ == '__main__':
    main()
