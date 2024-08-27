class IntrospectionInfo:
    def __init__(self, obj):
        self.obj = obj

    def type_(self):
        return type(self.obj)

    def attributes_(self):
        return dir(self.obj)

    def methods_(self):
        methods = []
        for at in self.attributes_():
            if at[0] != '_':
                methods.append(at)
        return methods

    def module_(self):
        module = self.obj, __class__.__module__
        if module == 'builtins':
            module = '__main__'
        return module


def introspection_info(obj):
    help_ = IntrospectionInfo(obj)
    info = {
        'type': help_.type_(),
        'attributes': help_.attributes_(),
        'methods': help_.methods_(),
        'module': help_.module_()}
    return info


number_info = introspection_info(42)
print(number_info)
