# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
from swagger_py_codegen.parser import RefNode

# TODO: datetime support


###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/jeremyzhang7413/DentistReservation'

definitions = {'definitions': {'cancelbooked': {'type': 'object', 'properties': {'timeId': {'type': 'integer'}}}, 'alltimeslots': {'type': 'object', 'properties': {'dentistId': {'type': 'integer'}, 'timeId': {'type': 'integer'}, 'data': {'type': 'string', 'format': 'date'}, 'timeslot': {'type': 'string'}, 'reserved': {'type': 'boolean', 'default': False}}, 'xml': {'name': 'alltimeslots'}}, 'alltimeslotsbook': {'type': 'object', 'properties': {'dentistId': {'type': 'integer'}, 'timeId': {'type': 'integer'}}, 'xml': {'name': 'alltimeslotsbook'}}, 'timeslot': {'type': 'object', 'properties': {'timeId': {'type': 'integer'}, 'data': {'type': 'string', 'format': 'date'}, 'timeslot': {'type': 'string'}, 'reserved': {'type': 'boolean', 'default': False}}, 'xml': {'name': 'timeslot'}}, 'timeslotbook': {'type': 'object', 'properties': {'timeId': {'type': 'integer'}}, 'xml': {'name': 'timeslot'}}}, 'parameters': {}}

validators = {
    ('timeslots', 'POST'): {'json': {'$ref': '#/definitions/alltimeslotsbook'}},
    ('timeslots_cancel_appointment', 'PUT'): {'json': {'$ref': '#/definitions/cancelbooked'}},
    ('timeslots_dentistId_book_appointment', 'POST'): {'json': {'$ref': '#/definitions/timeslotbook'}},
}

filters = {
    ('timeslots', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/alltimeslots'}}}, 404: {'headers': None, 'schema': None}},
    ('timeslots', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/alltimeslots'}}, 404: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': {'type': 'object', 'properties': {'message': {'type': 'string'}}}}},
    ('timeslots_cancel_appointment', 'PUT'): {400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}, 200: {'headers': None, 'schema': None}},
    ('timeslots_dentistId_book_appointment', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/timeslot'}}}, 404: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': {'type': 'object', 'properties': {'message': {'type': 'string'}}}}},
    ('timeslots_dentistId_book_appointment', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/timeslot'}}, 404: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': {'type': 'object', 'properties': {'message': {'type': 'string'}}}}},
}

scopes = {
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key and '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors