from flask import Blueprint, request

from app.db import db_instance
from app.helpers.tools import is_dict_subset, filter_data
from app.schema.validators import BaseForm

base_bp = Blueprint('base_bp', __name__)


@base_bp.route('/get-form', methods=['POST'])
def get_form():
    args = request.form
    if not args:
        return {'message': 'No data was provided'}

    dict_args = dict(args)
    all_data = db_instance.all()

    for base_dict in all_data:
        copy_dict = {key: value for key, value in base_dict.items() if key != 'name'}
        dict_subset = is_dict_subset(copy_dict, dict_args)

        if dict_subset:
            form_errors = filter_data(base_dict, dict_args)
            if not form_errors:
                return {'form_name': base_dict.get('name')}

    new_custom_form = BaseForm()
    result_form = new_custom_form.get_custom_data_type(data=dict_args)
    if result_form:
        return result_form
