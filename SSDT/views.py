from flask import request
from SSDT import app
from SSDT.Classes.Category import *
from SSDT.Classes.Record import *
from SSDT.Classes.User import *
from SSDT.data import *
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'lab1'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/')
def main():
    return "IO-01 Mila Bibik"


# endpoint 1
@app.route('/user', methods=['POST'])
def create_user():
    user = User(request.json["id"],
                request.json["name"])
    return user.create_user()


# endpoint 2
@app.route('/category', methods=['POST'])
def create_category():
    category = Category(request.json["id"],
                        request.json["name"])
    return category.create_category()


# endpoint 3
@app.route('/record', methods=['POST'])
def create_record():
    record = Record(request.json["id"],
                    request.json["user id"],
                    request.json["category id"],
                    request.json["date"],
                    request.json["amount"])
    return record.create_record()


# endpoint 4
@app.route('/categories', methods=['GET'])
def get_categories():
    return json_extract(CATEGORIES, "name")


# endpoint 5
@app.route('/records/user/<int:uid>', methods=['GET'])
def get_record_by_user(uid):
    existing_id = json_extract(RECORDS, "user id")
    records_by_user = []
    if uid in existing_id:
        for i in range(len(RECORDS)):
            if RECORDS[i]["user id"] == uid:
                records_by_user.append(RECORDS[i])
        return records_by_user
    else:
        return "No records are available for this user"


# endpoint 6
@app.route('/records/user/<int:uid>/<int:cid>', methods=['GET'])
def get_record_by_user_in_category(uid, cid):
    existing_user_id = json_extract(RECORDS, "user id")
    records_by_user = []
    if uid in existing_user_id:
        for i in range(len(RECORDS)):
            if RECORDS[i]['user id'] == uid:
                if RECORDS[i]['category id'] == cid:
                    records_by_user.append(RECORDS[i])
    if len(records_by_user) > 0:
        return records_by_user
    else:
        return "Error: No records are available for this user OR this user doesn't have any records in this category"
