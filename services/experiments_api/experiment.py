# file: experiments.py

class Experiment(object):
    def __init__(self, expId, expName, species):
        self.expId = expId
        self.expName = expName
        self.species = species

def object_hook_handler(parsed_dict):
    return Experiment(expId=parsed_dict['expId'],
                   expName=parsed_dict['expName'],
                   species=parsed_dict['species'])
