import datetime as dt

from abc import ABC

from tortoise.exceptions import DoesNotExist, IntegrityError

from smit_insurance_calculation.core import models, enums, exceptions


class Repo(ABC):
    pass


class RateRepo(Repo):

    async def upsert(self, rate_upsert: models.RateUpsertPydantic) -> models.RatePydantic:
        new_fields = dict(
            date=rate_upsert.date,
            cargo_type=rate_upsert.cargo_type,
            ratio=rate_upsert.ratio
        )

        try:
            rate = await models.RateTortoise.create(**new_fields)
        except IntegrityError:
            searched_fields = dict(
                date=rate_upsert.date,
                cargo_type=rate_upsert.cargo_type
            )

            await models.RateTortoise.filter(**searched_fields).update(**new_fields)
            rate = await models.RateTortoise.get(**searched_fields)

        return await models.RatePydantic.from_tortoise_orm(rate)

    async def read(
            self,
            cargo_type: enums.CargoType,
            date: dt.date
    ) -> models.RatePydantic:
        try:
            return await models.RatePydantic.from_queryset_single(
                models.RateTortoise.get(cargo_type=cargo_type, date=date)
            )
        except DoesNotExist:
            raise exceptions.RateNotFound
