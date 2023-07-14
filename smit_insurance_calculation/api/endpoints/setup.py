from fastapi import FastAPI

from smit_insurance_calculation.api.endpoints import rate, cargo


def register_routers(app: FastAPI) -> None:
    app.include_router(
        rate.router,
        prefix="/rate",
        tags=["rate"]
    )

    app.include_router(
        cargo.router,
        prefix="/cargo",
        tags=["cargo"]
    )
