
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
Platform Class
"""

# Class Constructor
class Platform(object):
    """Creates an instance of Platform class
    by experiment ID, experiment name, platform ID, platform name, and species name
    
    :type expId: string
    :param expId: experiment ID
    
    :type expName: string
    :param expName: experiment name
    
    :type platformId: string
    :param platformId: platform ID
    
    :type platformName: string
    :param platformName: platform name
    
    :type species: string
    :param species: species name
    
    :rtype: Platform
    :return: Returns Platform object
    """
    
    def __init__(self, expId, expName, species, platformId, platformName):
        self.expId = expId
        self.expName = expName
        self.species = species
        self.platformId = platformId
        self.platformName = platformName

# This function transform json object into an instance of Platform class
def object_hook_handler(parsed_dict):
    """Performs json string serialization into an Platform object
    by experiment ID, experiment name, platform ID, platform name, and species name
    
    :type parsed_dict: dict
    :param parsed_dict: json object as dictionary
         
    :rtype: Platform 
    :return: Returns Platform  object
    """
    
    return Platform(expId=parsed_dict['expId'],
                   expName=parsed_dict['expName'],
                   species=parsed_dict['species'],
                   platformId=parsed_dict['platformId'],
                   platformName=parsed_dict['platformName']
                   )
