from jsonschema import validate
from jsonschema.validators import Draft202012Validator, validator_for
from jsonschema import RefResolver
from jsonschema.exceptions import ValidationError
import requests
from typing import Union
import json
import enum
import functools
import sys

#root_path = "https://raw.githubusercontent.com/flexiblepower/s2-ws-json/main/s2-json-schema/"

def fetch_schema(schema : Union[str, dict]) -> dict:

    print(schema)
    # dictionary
    if isinstance(schema, dict):
        return schema

    # URL: try to fetch the schema from a url
    try:
        return requests.get(schema).json()
    except:
        pass
        
    # Local file: try to read schema from local path
    try:
        with open(schema, "r") as f:
            return json.load(f)
    except:
        pass

    raise ValueError("Schema couldn't be fetched.")
        
            
class ValidatorMixin:
    """Mixin for validation against a JSON schema.
    """

    def __init__(self, *args, **kwargs) -> None:
        
        # checks if schema is valid according to the 2020-12 Draft Spec
        validator_for(self.schema)
        
        # create a Draft 2020-12 JSONSchema validator for the schema
        self.validator = Draft202012Validator(schema=self.schema)

    def validate(self):
        self.validator.validate(self)
        return self

    def is_valid(self):
        try:
            self.validator.validate(self)
            return True
        except ValidationError:
            return False
        
class ValidatorDictMixin(dict, ValidatorMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        ValidatorMixin.__init__(self)
        self.validator.validate(self)
class ValidatorIntMixin(int, ValidatorMixin):
    """Subclass of int with validation upon creation (using __new__).

    This works a bit special, because the int class is immutable.
    See https://santoshk.dev/posts/2022/__init__-vs-__new__-and-when-to-use-them/
    """
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        self.validator.validate()
        return self
    
class ValidatorListMixin(list, ValidatorMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        ValidatorMixin.__init__(self)
        self.validator.validate(self)
class ValidatorStrMixin(str, ValidatorMixin):
    """Subclass of str with validation upon creation (using __new__).

    This works a bit special, because the str class is immutable.
    See https://santoshk.dev/posts/2022/__init__-vs-__new__-and-when-to-use-them/
    """
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        
        ValidatorMixin.__init__(self)
        self.validator.validate(self)

        return self

class ValidatorType(enum.Enum):
    INT = "int"
    STR = "str"
    DICT = "dict"
    LIST = "list"


def validator_factory_constructor(self, *args, **kwargs):
    super(self.__class__, self).__init__(self, *args, **kwargs) # setting up validator

def validator_factory__call__(self, entity : Union[dict, str, int]):
    
    if isinstance(entity, str):
        desearialized_entity = json.loads(entity)
        self.validate(desearialized_entity)
    
    return self.type_(entity).validate()


# class ValidatorFactory():
#     def __init__(self, schema : Union[str, dict], type_ : ValidatorType, validate_schema=False) -> None:
#         """ This class loads a JSONSchema as a dictionary
#         """

#         self._schema = fetch_schema(schema)
#         self.name = self._schema["title"]
#         self.type_ = type_

#     def __call__(self, *args, **kwargs):
        
#         # choosing which validator class to use
#         validator_class = None
#         if self.type_ == ValidatorType.DICT:
#             validator_class = ValidatorDictMixin
#         elif self.type_ == ValidatorType.LIST:
#             validator_class = ValidatorListMixin
#         elif self.type_ == ValidatorType.STR:
#             validator_class = ValidatorStrMixin
#         elif self.type_ == ValidatorType.INT:
#             validator_class = ValidatorIntMixin

#         ValidatorClass = type(self.name, (validator_class,), {
#             "__init__": validator_factory_constructor, 
#             "__call__" : validator_factory__call__,
#             "schema" : self._schema
#         })

#         return ValidatorClass

def get_validator_factory(schema : Union[str, dict], type_ : ValidatorType, validate_schema=False):
    _schema = fetch_schema(schema)
    name = _schema["title"]
    
    # choosing which validator class to use
    validator_class = None
    if type_ == ValidatorType.DICT:
        validator_class = ValidatorDictMixin
    elif type_ == ValidatorType.LIST:
        validator_class = ValidatorListMixin
    elif type_ == ValidatorType.STR:
        validator_class = ValidatorStrMixin
    elif type_ == ValidatorType.INT:
        validator_class = ValidatorIntMixin

    ValidatorClass = type(name, (validator_class,), {
        "__init__": validator_factory_constructor, 
        "__call__" : validator_factory__call__,
        "schema" : _schema
    })

    return ValidatorClass

"""

    Syntax
    FillLevelTargetProfileElement = ValidatorFactory("{...}", INT, validate_schema=True) <- pros i can change root of url
    
    coche = Coche(ruedas=1, color="verde") --> new class

    coche.is_valid()

    coche.validate()

    coche.rueda = 1
    coche.validate()


    FillLevelTargetProfileElement(ruedas=1, color="verde") --> new class
    FillLevelTargetProfileElement(**) --> new class


    FillLevelTargetProfileElement(**)
    I can have 1 generator class that fetches and process the schedule ONCE -> then we use

"""

def change_base_uri(base_uri):
    thismodule = sys.modules[__name__]
    thismodule.BASE_URI = base_uri


BASE_URI = "https://raw.githubusercontent.com/flexiblepower/s2-ws-json/main/s2-json-schema"



def get_schema_validator(message_name, type_ : ValidatorType):
    return get_validator_factory(f"{BASE_URI}/schema/{message_name}.schema.json", type_)


Commodity = get_schema_validator("Commodity", ValidatorType.STR)
Commodity = get_schema_validator("Commodity", ValidatorType.STR)
Commodity = get_schema_validator("Commodity", ValidatorType.STR)
Commodity = get_schema_validator("Commodity", ValidatorType.STR)
Commodity = get_schema_validator("Commodity", ValidatorType.STR)
Commodity = get_schema_validator("Commodity", ValidatorType.STR)

# def validate_jsonschema(validator : Validator, input=True):
    
#     def wrapper(func):
#         @functools.wraps(func)
#         def inner(*args, **kwargs):
#             if input:

            

#             result = func(*args, **kwargs)


#             if not input:
#                 validator.validate(result)

#             return result
            
        
#         return inner
#     return wrapper
