import datetime as dt

from fastapi import APIRouter, Depends
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ErrorWrapper
from starlette.status import HTTP_404_NOT_FOUND

from smit_insurance_calculation.api import responses
from smit_insurance_calculation.api.deps.rate import RateRepoMarker
from smit_insurance_calculation.core import models, enums
from smit_insurance_calculation.core.repo import RateRepo

router = APIRouter()


@router.get(
    "/",
    response_model=models.RatePydantic,
    responses={
        HTTP_404_NOT_FOUND: {
            "model": responses.RateNotFound
        }
    }
)
async def read(
        cargo_type: enums.CargoType,
        date: dt.date,
        rate_repo: RateRepo = Depends(RateRepoMarker)
):
    """
    Возвращает тариф по типу грузу и дате
    """
    return await rate_repo.read(cargo_type=cargo_type, date=date)


@router.put("/", response_model=models.RatePydantic)
async def upsert_rate(
        rate_upsert: models.RateUpsertPydantic,
        rate_repo: RateRepo = Depends(RateRepoMarker)
):
    """
    Создает или обновляет текущий тариф
    """

    try:
        """
        https://github.com/tortoise/tortoise-orm/issues/576
        """
        enums.CargoType(rate_upsert.cargo_type)
    except ValueError as e:
        raise RequestValidationError(errors=[ErrorWrapper(e, ("query", enums.CargoType.__name__.lower()))])

    return await rate_repo.upsert(rate_upsert=rate_upsert)
