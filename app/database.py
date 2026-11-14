users = [
    {
        "name": "Garfield",
        "age": 8
    },
    {
        "name":"Petter",
        "age": 16
    }
]

class User:
    name = ""
    age = 0

    def __init__(self, name, age, id=0):
        self.name = name
        self.age = age
        self.id = id

    def get_user(self, id):
        if not (id >= 0 and id < len(users)):
            return {}

        user = users[id]
        
        return User(user.name, user.age)

    def get_users(self):
        return users