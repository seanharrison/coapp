import os, sys
from bl.config import Config
from bsql.database import Database
from bsvn import SVN

path = os.path.dirname(os.path.abspath(__file__))
config = Config(fn=os.path.join(path, '__config__.ini'))
try:
    db = Database(**config.Database)
except:
    print(sys.exc_info()[1], config.Database)

try:
    svn = SVN(**config.SVN)
except:
    print(sys.exc_info()[1], config.SVN)
