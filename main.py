def get_module_inside(module_name):
    result = dict()
    try:
        checking_module = __import__(module_name)
        result['module'] = checking_module
        functions = []
        modules = []
        others = {'objs': [], 'vars': []}
        for attr in dir(checking_module):
            attrbute = getattr(checking_module, attr)
            if callable(attrbute):
                if type(attrbute) == type(__import__('re').match):
                    functions.append(
                        {'function': attrbute, 'function_name': attrbute.__name__, 'in_module': attrbute.__module__})
                else:
                    others['objs'].append(
                        {'obj': attrbute, 'obj_name': attrbute.__name__, 'in_module': attrbute.__module__})
            else:
                if type(attrbute) == type(__import__('re')):
                    modules.append(attrbute)
                else:
                    others['vars'].append({'name': attr, 'value': attrbute})
        result['functions'] = functions
        result['modules'] = modules
        result['others'] = others
        return result
    except ModuleNotFoundError as e:
        return {'Error': e}


def get_import_tags(import_string):
    import builtins
    builtins_import = builtins.__import__
    import_result = []
    def _import_(*args, **kwargs):
        nonlocal import_result
        import_result = [i for i in args] + [i for i in kwargs]
    builtins.__import__ = _import_
    exec(import_string)
    builtins.__import__ = builtins_import
    return import_result


# get_module_inside e.g.
print('|=================|\n|\033[31mget_module_inside\033[38m|\n|=================|')
module_result = get_module_inside('re')
print(module_result)
# get_import_tags e.g.
print('|===============|\n|\033[31mget_import_tags\033[38m|\n|===============|')
import_tags = get_import_tags('import re')
print(import_tags)
