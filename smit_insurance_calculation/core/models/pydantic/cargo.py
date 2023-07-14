import datetime as dt

from pydantic import BaseModel

from smit_insurance_calculation.core import enums


class Cargo(BaseModel):
    cost: float
    type: enums.CargoType
    date: dt.date
