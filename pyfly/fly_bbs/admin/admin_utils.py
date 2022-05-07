from bson import ObjectId
from .admin_config import admin_permissions


def fill_form_choices(form_field, collection_name: str, db_field_name: str):
    from fly_bbs.extensions import mongo
    form_field.choices = [(str(item['_id']), item[db_field_name]) for item in mongo.db[collection_name].find()]


def get_user_permissions(user):
    from fly_bbs.extensions import mongo
    if user['is_admin']:
        return set([p[0] for p in admin_permissions])
    if 'role_ids' not in user:
        return set()
    roles = mongo.db.roles.find({'_id': {'$in': user['role_ids']}})
    permissions = []
    for role in roles:
        permissions += role['permissions']
    return set(permissions)
