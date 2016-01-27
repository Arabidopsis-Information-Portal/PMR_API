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
Returns base urls for the underlying endpoints
"""

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# This function returns the platforms base url to use by the search endpoint
def get_search_base_url():
    """Return the platforms base url
    
    :rtype: string
    :return: Returns the platforms base url
    
    """
    return 'http://pmr-webapi.gdcb.iastate.edu/pmrWebApi/api/v1/platforms/list'

# This function returns the experiments base url to use by the list endpoint
def get_list_base_url():
    """Return the platforms base url
    
    :rtype: string
    :return: Returns the platforms base url
    
    """
    return 'http://pmr-webapi.gdcb.iastate.edu/pmrWebApi/api/v1/platforms/list'
