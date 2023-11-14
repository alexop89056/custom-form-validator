from app.schema.validators import BaseForm


def is_dict_subset(subset: dict, superset: dict):
    for key in subset.keys():
        if key not in superset.keys():
            return False
    return True


def filter_data(subset: dict, superset: dict):
    form_errors = {}
    new_form = BaseForm()
    for key, value in superset.items():
        if key in subset.keys():
            validate_attr = getattr(new_form, subset.get(key), None)
            validate_data = validate_attr.validate_data(value)
            if not validate_data:
                form_errors[key] = subset.get(key)
    return form_errors
