from src.auth import UserModel, Encrypt, DB

user1 = UserModel('Ekin', '', '1234')
# or
user2 = UserModel('Cenk', 'Moderator', '')
user2.password = Encrypt('1234').set_password()

db = DB('test.db')

db.add_table('users', [
    'username TEXT',
    'role TEXT',
    'password TEXT'
])

# First User
db.init('users', [
    user1.username,
    user1.role,
    user1.password
])

# Second User
db.init('users', [
    user2.username,
    user2.role,
    user2.password
])

db.migrate()