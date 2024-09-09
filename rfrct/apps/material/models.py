from extensions import nosql
import datetime

class MaterialType(nosql.Document):
    name = nosql.StringField(max_length=255, required=True, unique=True)
    description = nosql.StringField(max_length=255, required=True)
    created_at = nosql.DateTimeField(default=datetime.datetime.now)
    updated_at = nosql.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    meta = {
        'ordering': ['name']
    }

class Material(nosql.Document):
    name = nosql.StringField(max_length=255, required=True, unique=True)
    description = nosql.StringField(max_length=255, required=True)
    #material_type = nosql.ReferenceField(MaterialType)
    created_at = nosql.DateTimeField(default=datetime.datetime.now)
    updated_at = nosql.DateTimeField(default=datetime.datetime.now)
    price_per_square_meter = nosql.DecimalField(min_value=0, required=True, symbol="mm")
    thickness = nosql.DecimalField(min_value=0, required=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    meta = {
        'ordering': ['name']
    }