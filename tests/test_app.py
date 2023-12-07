# Test App

from auth.model import UserModel
from auth.roles import UserRoles
from auth.manager import UserManager
from auth.login import UserLogin


# Settings
model_db = 'test.db'
roles_db = 'roles.db'

model = UserModel(model_db)
manager = UserManager(model_db)
login = UserLogin(model_db)
roles = UserRoles(roles_db)