from uuid import uuid4

from tortoise import models, fields

from smit_insurance_calculation.core.enums import CargoType


class Rate(models.Model):
    id = fields.UUIDField(pk=True, default=uuid4)

    date = fields.DateField(null=False)
    cargo_type = fields.CharEnumField(CargoType, null=False)
    ratio = fields.FloatField(null=False)

    class Meta:
        table = "rates"
        unique_together = (("date", "cargo_type"),)

    class PydanticMeta:
        exclude = ["id"]
