"""
params.py
get param from yaml file;
@author wwtfly
@version 2019-05-21
"""
import yaml
from collections import defaultdict
import os
def getParams():
    with open('./initDisk.yaml') as f:
        params=yaml.load(f,yaml.FullLoader)
        param=defaultdict(list)
        print(param)
"""

"""
class params():
        def __init__(self,file):
                self._file=''
                # 定义两个空的字典
                self._loginParams=defaultdict(set)
                self._partitionParams=defaultdict(list)
                # 判断文件是否存在，如果存在则打开文件
                if os.path.exists(file):
                        with open(file) as inf:
                                p=yaml.load(inf,Loader=yaml.FullLoader)
                                self._file=p

                # 对yaml文件格式进行校验，如果格式由问题则退出执行
                else:
                        print("config file :"+file+" dose not exits")
                        # print(self._file)
        # 解析参数文件，返回两个字典对象，一个是登录参数，一个是分区参数
        def getParams(self):
                # self.file数组中由两部分组成，一个是登录信息，一个是分区信息；
                # self._loginParams=self._file['node']
                # for i in range(len(self._file['node'])):
                #         *loginParams,self._partitionParams=self._file['node'][i]
                        # print(*loginParams)
                #         print(self._partitionParams)
                for params in self._file['node']:
                        *login,disk=params.keys()
                        # disk={disk}
                        # print(params['ip'])
                        # self._loginParams[params['ip']].add({key:value for key,value in params.items() if key in login})
                        # self._partionParams = {key: value for key, value in params.items() if key == disk}
                        self._partitionParams[params['ip']].append(params[disk])
                        # print(self._loginParams)
                        print(self._partitionParams)
                return self._loginParams,self._partitionParams

        # 写入新的参数文件,根据用户提供的参数，主要是分区参数，生成实际参数，检查在另一个类中实现；
        # 这个函数主要时根据输入的json数据生成一个yaml格式的配置文件；
        def writeParams(self,conJson):
                with open('./newInitDisk.yaml','xt') as outf:
                        # 添加将json文件转换成yaml文件格式写入到文件
                        outf.write(conJson)

if __name__ == "__main__":
        pa=params('./initDisk.yaml')
        pa.getParams()
        
