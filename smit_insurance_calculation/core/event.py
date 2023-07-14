from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

from smit_insurance_calculation.api.deps.setting import SettingMarker
from smit_insurance_calculation.core import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    setting: models.Setting = app.dependency_overrides[SettingMarker]()

    tortoise_config = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "host": setting.pg_host,
                    "port": setting.pg_port,
                    "user": setting.pg_user,
                    "password": setting.pg_password,
                    "database": setting.pg_db
                }
            }
        },
        "apps": {
            "smit_insurance_calculation":
            {
                "models": ["smit_insurance_calculation.core.models.tortoise.rate"],
                "default_connection": "default"
            }
        }
    }

    await Tortoise.init(config=tortoise_config)

    yield

    await Tortoise.close_connections()
