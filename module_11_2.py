def introspection_info(obj):
    obj_type = type(obj)
    attributes = dir(obj)
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = getattr(obj, '__module__', None)
    return {'type': obj_type.__name__,
            'attributes': attributes,
            'methods': methods,
            'module': module}


number_info = introspection_info(42)
print(number_info)
