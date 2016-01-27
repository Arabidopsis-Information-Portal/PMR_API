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
Metabolite Class
"""
# Class Constructor
class Metabolite(object):
    """Creates an instance of Metabolite class
    by metabolite ID, metabolite name
    
    :type mId: string
    :param mId: metabolite ID
    
    :type metaboliteName: string
    :param metaboliteName: metabolite name
    
    :rtype: Metabolite
    :return: Returns Metabolite object
    """
    def __init__(self, mId, metaboliteName):
        self.mId = mId
        self.metaboliteName = metaboliteName

# This function transform json object into an instance of Metabolite class
def object_hook_handler(parsed_dict):
    """Performs json string serialization into an Metabolite object
    by metabolite ID, metabolite name
    
    :type parsed_dict: dict
    :param parsed_dict: json object as dictionary
         
    :rtype: Metabolite
    :return: Returns Metabolite object
    """
    return Metabolite(mId=parsed_dict['mId'],
                   metaboliteName=parsed_dict['metaboliteName']
                                   )
