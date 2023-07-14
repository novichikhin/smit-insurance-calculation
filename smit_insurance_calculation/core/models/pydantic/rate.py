from tortoise.contrib.pydantic import pydantic_model_creator

from smit_insurance_calculation.core.models.tortoise.rate import Rate as RateTortoise

Rate = pydantic_model_creator(RateTortoise, name="Rate")
RateUpsert = pydantic_model_creator(
    RateTortoise,
    name="RateUpsert",
    exclude_readonly=True
)
