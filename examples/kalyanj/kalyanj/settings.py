from pathlib import Path
from os.path import abspath

# defining the default import name for flask:
IMPORT_NAME = __name__

#defining the actual project name:
PROJECT_NAME = "kalyanj"


#defining the base directory
BASE_DIR = Path(abspath(__file__)).parent.parent

#app debug state:
DEBUG = True

#defining the base database configuration.
DATABASE = {
    "engine" : "sqlite3",
    "database": BASE_DIR / "navycut.sqlite3"
}

#defining the navycut app secret key
SECRET_KEY = r"y>EYb:G1YAZkpq{IGfPg9:Z}ro*5d}R7BQA[IbC/FKw2pSx%>rO>m" #should generate randomly at the time of creation.


#available installed app add here to bloom.
INSTALLED_APPS = [ # should change to first_app to get the app.
    "navycut.helpers.upload_server",
    #"first_app", 
]

ALLOWED_HOST = [ # 
    '127.0.0.1', 
]