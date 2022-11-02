from SSDT.data import json_extract

RECORDS = []


class Record:
    def __init__(self, id, user_id, category_id, date, amount):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.date = date,
        self.amount = amount

    def create_record(self):

        new_record = {
            "id": int(self.id),
            "user id": int(self.user_id),
            "category id": int(self.category_id),
            "date": str(self.date),
            "amount": str(self.amount)
        }

        existing_id = json_extract(RECORDS, "id")

        if self.id in existing_id:
            return 'This ID is not available'
        else:
            RECORDS.append(new_record)
            return RECORDS
