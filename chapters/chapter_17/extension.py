## EXTENSIONS

# 1. Extension - Inheritance hierarchy for a data type system
"""
a. Build a base class called DataField:
   __init__(self, name, nullable=False):
   - self.name: field name
   - self.nullable: whether None is a valid value
   - self.value: current value (initially None)
   Methods:
   - validate(self, value): returns True if value is valid for this field type. Base implementation: if nullable, None is valid. Subclasses extend this.
   - set(self, value): validates, then sets self.value; raises ValueError if invalid
   - get(self): returns self.value
   - __str__: 'FieldName: value (type)'
b. Create subclasses:
   - IntField(DataField): value must be an integer within [min_val, max_val]
    __init__(self, name, min_val, max_val, nullable=False)
     Override validate(self, value)
   - FloatField(DataField): value must be float or int, within [min_val, max_val]
     Override validate(self, value)
   - StringField(DataField): value must be a string, with max_length constraint
    __init__(self, name, max_length, nullable=False)
     Override validate(self, value)
   - CategoricalField(DataField): value must be in a predefined set of choices
    __init__(self, name, choices, nullable=False)
     Override validate(self, value)
c. Build a class called Record that composes multiple DataFields:
   __init__(self, **field_definitions): stores a dict of field_name -> DataField
   - set_field(self, name, value): calls field.set(value)
   - get_field(self, name): calls field.get()
   - is_complete(self): True if all non-nullable fields have non-None values
   - validate_all(self): returns a dict of {field_name: error_message_or_None}
   - __str__: prints all field names and values
d. Write a function called create_patient_record() that builds a Record representing a medical data entry:
   - patient_id: IntField(1, 999999)
   - name: StringField(max_length=100)
   - age: IntField(0, 150)
   - temperature: FloatField(35.0, 43.0)
   - status: CategoricalField(['stable', 'critical', 'discharged'])
   Try setting invalid values and verify ValueError is raised with clear messages.
"""
print("\nEXTENSION 1")

# 1.a
class DataField:
    def __init__(self, name: str, nullable: bool = False):
        self.name: str = name
        self.nullable: bool = nullable
        self.value = None

    def validate(self, value) -> bool:
        if value == None: return self.nullable
        return True

    def set(self, value):
        if not self.validate(value): raise ValueError("Valor inválido.")
        self.value = value

    def get(self):
        return self.value

    def __str__(self):
        tipo = type(self.value).__name__ if self.value is not None else 'None'
        return f'{self.name}: {self.value} ({tipo})'


# 1.b
class IntField(DataField):
    def __init__(self, name: str, min_val: int | float, max_val: int | float, nullable = False):
        super().__init__(name, nullable)
        self.min_val, self.max_val = min_val, max_val
    def validate(self, value: int):
        if value is None: return self.nullable
        return (self.min_val <= value <= self.max_val) and (type(value) == int)
    
class FloatField(DataField):
    def __init__(self, name: str, min_val: int | float, max_val: int | float, nullable = False):
        super().__init__(name, nullable)
        self.min_val, self.max_val = min_val, max_val
    def validate(self, value: float):
        if value is None: return self.nullable
        return (self.min_val <= value <= self.max_val) and (type(value) == float)
    
class StringField(DataField):
    def __init__(self, name: str, max_length: int, nullable = False):
        super().__init__(name, nullable)
        self.max_length: int = max_length
    def validate(self, value: str):
        if value is None: return self.nullable
        return (len(value) <= self.max_length) and (type(value) == str)
    
class CategoricalField(DataField):
    def __init__(self, name: str, choices: set, nullable = False):
        super().__init__(name, nullable)
        self.choices: set = choices
    def validate(self, value):
        if value is None: return self.nullable
        return value in self.choices

# 1.c
class Record:
    def __init__(self, **field_definitions):
        self.fields = field_definitions

    def set_field(self, name, value):
        if name not in self.fields: raise KeyError(f"'{name}' no existe en este Record")
        self.fields[name].set(value)

    def get_field(self, name):
        if name not in self.fields:
            raise KeyError(f"'{name}' no existe en este Record")
        return self.fields[name].get()

    def is_complete(self):
        for field in self.fields.values():
            if not field.nullable and field.get() is None: return False
        return True

    def validate_all(self):
        errors: dict = {}
        for name, field in self.fields.items():
            current_value = field.get()
            if field.validate(current_value):
                errors[name] = None
                continue
            errors[name] = f"Valor inválido: {current_value}"
        return errors

    def __str__(self):
        lines = [f"Record ({len(self.fields)} fields):"]
        for name, field in self.fields.items(): lines.append(f"  {field}")
        return "\n".join(lines)

# 1.d
def create_patient_record():
    fields = {
        "patient_id": IntField("patient_id", 1, 999999, nullable=False),
        "name": StringField("name", 100, nullable=False),
        "age": IntField("age", 0, 150, nullable=False),
        "temperature": FloatField("temperature", 35.0, 43.0, nullable=False),
        "status": CategoricalField("status", ['stable', 'critical', 'discharged'], nullable=False)
    }
    return Record(**fields)
print(create_patient_record())