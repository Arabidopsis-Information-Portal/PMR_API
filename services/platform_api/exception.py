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
API Exception Module
"""

# This function creates Not Found Exception 
class NotFound(Exception):
    """Creates Not Found Exception inherited from Exception class
         
    :rtype: NotFound Exception
    :return: Returns NotFound exception with a custom message
    
    """
    pass

class InvalidParameter(Exception):
    """Creates Invalid Parameter Exception inherited from Exception class
         
    :rtype: InvalidParameter Exception
    :return: Returns InvalidParameter exception with a custom message
    
    """
    pass

class EmptyResponse(Exception):
    """Creates EmptyResponse Exception inherited from Exception class
         
    :rtype: EmptyResponse Exception
    :return: Returns EmptyResponse exception with a custom message
    
    """
    pass