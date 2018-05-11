""" golden_json.py
"""

import json

class GoldenJson(object):
    """ Simple GoldenJson class used to simplify
        search of good/bad lumisections
    """

    def __init__(self, filename):
        self.filename = filename
        self.data = {}

        with open(self.filename) as json_data:
            self.data = json.load(json_data)

    def is_good(self, run, lumisection):
        """ Return True/False if given run and lumisection is good/bad
        """

        run = str(run)
        if run in self.data:
            # iterate over lumisection ranges
            for ls_range in self.data[run]:
                ls_min, ls_max = ls_range
                if ls_min <= lumisection <= ls_max:
                    return True
        return False

