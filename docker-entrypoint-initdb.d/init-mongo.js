print('Start #################################################################');

db = db.getSiblingDB('user_store');
db.createUser(
  {
    user: 'debug',
    pwd: 'debug',
    roles: [{ role: 'readWrite', db: 'user_store' }],
  },
);
db.createCollection('users');
db.createCollection('locations');

print('END #################################################################');