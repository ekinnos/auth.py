from auth.roles import UserRoles
from auth.model import UserModel
from auth.manager import UserManager

model = UserModel('users.db')
roles = UserRoles('roles.db')
manager = UserManager('users.db','roles.db')

manager.give_role('ekin','admin')