from SSDT.data import json_extract

CATEGORIES = []


class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def create_category(self):

        new_category = {
            "id": int(self.id),
            "name": str(self.name)
        }

        existing_id = json_extract(CATEGORIES, "id")

        if self.id in existing_id:
            return 'This ID is not available'
        else:
            CATEGORIES.append(new_category)
            return CATEGORIES
