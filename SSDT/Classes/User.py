from SSDT.data import json_extract

USERS = []


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def create_user(self):

        new_user = {
            "id": int(self.id),
            "name": str(self.name)
        }

        existing_id = json_extract(USERS, "id")

        if self.id in existing_id:
            return 'This ID is not available'
        else:
            USERS.append(new_user)
            return USERS
