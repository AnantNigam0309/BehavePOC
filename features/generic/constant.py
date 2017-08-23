import os


class constant():
    def __init__(self):
        pass

    rootPath = (os.path.dirname((os.path.dirname(os.path.abspath(__file__)))))
    thiftPath = rootPath + '/files/thrift'
    ymlPath= rootPath + '/files/yaml'
    timlineThriftPath = thiftPath + '/temporal_engine.thrift'
    clusterInfoYml= ymlPath+'/cluster_info.yml'

    @staticmethod
    def session(orgid,orgconfigid):
        dict = {'orgId': orgid, 'orgConfigId': orgconfigid, 'apacheThreadId': 'random', 'userId': -1, 'moduleName': 'auto'}
        return dict