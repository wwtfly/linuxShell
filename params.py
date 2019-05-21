"""
params.py
get param from yaml file;
@author wwtfly
@version 2019-05-21
"""
import yaml
from collections import defaultdict
def getParams():
    with open('./initDisk.yaml') as f:
        params=yaml.load(f,yaml.FullLoader)
        param=defaultdict(list)
        print(param)
"""

"""
class params():
        def __init__(self,file):
                self._file=""
                with open(file) as f:
                        self._file=f
        
        def getParams(self):
                print(self._file)

if __name__ == "__main__":
        p=params('./initDisk.yaml')
        p.getParams()