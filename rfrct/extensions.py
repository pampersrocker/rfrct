#
# All extensions are defined here. They are initialized by Empty if
# required in your project's configuration. Check EXTENSIONS.
#

import os

from flask_security import Security
from flask_security import MongoEngineUserDatastore
from flask_admin import Admin
from flask_mongoengine import MongoEngine
from flask_static_compress import FlaskStaticCompress
from flask_socketio import SocketIO


toolbar = None

if os.environ['FLASK_ENV'] == 'development':
    # only works in development mode
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension()

admin = Admin()
nosql = MongoEngine()
compress = FlaskStaticCompress()
security = Security()
db = nosql
io = SocketIO()

from flask_login import LoginManager
login_manager = LoginManager()

def security_init_kwargs():
    """
    **kwargs arguments passed down during security extension initialization by
    "empty" package.
    """
    from apps.auth.models import User, Role

    user_datastore = MongoEngineUserDatastore(nosql, User, Role)
    return dict(datastore=user_datastore)
