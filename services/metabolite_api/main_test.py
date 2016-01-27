import requests
import logging
import main as driver
from requests.exceptions import ConnectionError

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def main():
    """test logic for when running this module as the primary one!"""

    ## pass the namespace you test again (your dev namespace or production)
    test_namespace = 'ibelyaev-dev'

    #search test case
    args = {'experimentID': '106', 'platformID':'84', 'metaboliteID':'4349', '_url': 'https://api.araport.org/community/v0.3', '_namespace': test_namespace}
    driver.search(args)
    
    # list test case
    args = {'experimentID': '106', 'platformID':'84', '_url': 'https://api.araport.org/community/v0.3', '_namespace': test_namespace}
    driver.list(args)
    
    
if __name__ == '__main__':
    main()
