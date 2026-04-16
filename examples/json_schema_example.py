from jsonschema import validate

from tools.assertions.schema import validate_json_schema


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

data = {
    "name": "Alice",
    "age": 30
}

validate_json_schema(instance=data, schema=schema)