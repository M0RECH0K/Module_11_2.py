def introspection_info(obj):
    print(type(obj).__name__)
    print(dir(obj))
    print([method for method in dir(obj) if callable(getattr(obj, method))])
    print(getattr(obj, '__module__', None))
    return {
        'type': type(obj),
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getattr(obj, '__module__', None)
    }


number_info = introspection_info(42)
print(number_info)
