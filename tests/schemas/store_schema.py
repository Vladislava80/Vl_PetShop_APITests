STORE_SCHEMA = {
    "type": "object",
    "properties":{
        "id": {
            "type": "integer"
        },
        "petId": {
            "type": "integer"
        },
        "quantity": {
            "type": "integer"
        },
        "status": {
            "type": "string",
            "enum": ["placed", "approved", "delivered"]
        },
        "complete": {
            "type": "boolean"}
    },
    "additionalProperties": True,
    "required": ["id", "petId", "quantity", "complete"]
}


INVENTORY_SCHEMA = {
    "type": "object",
    "properties":{
        "approved": {
            "type": "integer"},
        "placed": {
            "type": "integer"},
        "delivered": {
            "type": "integer"
        }
    },
    "additionalProperties": False
}