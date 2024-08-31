def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = getattr(obj, '__module__', None)
    return {
        'type': type_obj,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }


number_info = introspection_info(42)
print(number_info)

list_info = introspection_info([4, 1, 3])
print(list_info)


class IntrospectionInfo:
    pass


class_info = introspection_info(IntrospectionInfo)
print(class_info)

