from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette import status

from smit_insurance_calculation.core import exceptions
from smit_insurance_calculation.core.exceptions.main import BaseAppException


def register_exceptions(app: FastAPI) -> None:
    app.add_exception_handler(exceptions.RateNotFound, rate_not_found_handler)


async def rate_not_found_handler(_, err: exceptions.RateNotFound) -> ORJSONResponse:
    return await handle_error(err, status_code=status.HTTP_404_NOT_FOUND)


async def handle_error(err: BaseAppException, status_code: int) -> ORJSONResponse:
    return ORJSONResponse({"status": "fail", "detail": err.message}, status_code=status_code)
