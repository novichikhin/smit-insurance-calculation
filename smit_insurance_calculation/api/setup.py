from fastapi import FastAPI

from smit_insurance_calculation.api.deps.rate import RateRepoMarker
from smit_insurance_calculation.api.deps.setting import SettingMarker
from smit_insurance_calculation.api.endpoints.setup import register_routers
from smit_insurance_calculation.api.exception import register_exceptions
from smit_insurance_calculation.core import models
from smit_insurance_calculation.core.event import lifespan
from smit_insurance_calculation.core.repo import RateRepo


def register_app(setting: models.Setting) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    register_routers(app=app)
    register_exceptions(app=app)

    app.dependency_overrides.update(
        {
            RateRepoMarker: lambda: RateRepo(),
            SettingMarker: lambda: setting
        }
    )

    return app
