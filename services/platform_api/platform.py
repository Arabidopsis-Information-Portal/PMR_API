# file: platform.py

class Platform(object):
    def __init__(self, expId, expName, species, platformId, platformName):
        self.expId = expId
        self.expName = expName
        self.species = species
        self.platformId = platformId
        self.platformName = platformName

def object_hook_handler(parsed_dict):
    return Platform(expId=parsed_dict['expId'],
                   expName=parsed_dict['expName'],
                   species=parsed_dict['species'],
                   platformId=parsed_dict['platformId'],
                   platformName=parsed_dict['platformName']
                   )
