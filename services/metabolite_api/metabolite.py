# file: metabolite.py

class Metabolite(object):
    def __init__(self, mId, metaboliteName):
        self.mId = mId
        self.metaboliteName = metaboliteName

def object_hook_handler(parsed_dict):
    return Metabolite(mId=parsed_dict['mId'],
                   metaboliteName=parsed_dict['metaboliteName']
                                   )
