from jsonschema import validate

def example():
    print("example")

def validate_me(obj, schema):
    validate(obj, schema)


