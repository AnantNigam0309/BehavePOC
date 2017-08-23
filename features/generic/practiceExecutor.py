from  yaml import load,dump
from features.generic.constant import constant
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

stream = file(constant.clusterInfoYml, 'r')

data =load(stream)
print dump(data)