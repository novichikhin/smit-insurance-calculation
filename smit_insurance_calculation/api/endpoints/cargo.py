import datetime as dt

from fastapi import APIRouter, Depends
from starlette.status import HTTP_404_NOT_FOUND

from smit_insurance_calculation.api import responses
from smit_insurance_calculation.api.deps.rate import RateRepoMarker
from smit_insurance_calculation.core import enums
from smit_insurance_calculation.core.repo import RateRepo

router = APIRouter()


@router.get(
    "/",
    response_model=float,
    responses={
        HTTP_404_NOT_FOUND: {
            "model": responses.RateNotFound
        }
    }
)
async def read(
        cargo_type: enums.CargoType,
        date: dt.date,
        cost: float,
        rate_repo: RateRepo = Depends(RateRepoMarker)
):
    """
    Возвращает стоимость груза по коэффициенту тарифа
    """
    rate = await rate_repo.read(cargo_type=cargo_type, date=date)

    return cost * rate.ratio
