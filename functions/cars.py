def make_car(manufacturer, model, **other_params):
    other_params['manufacturer'] = manufacturer
    other_params['model'] = model

    return other_params