import asyncio
import logging

import uvicorn

from smit_insurance_calculation.api.setup import register_app
from smit_insurance_calculation.core import models


def run_application() -> None:
    setting = models.Setting()
    app = register_app(setting=setting)

    config = uvicorn.Config(
        app,
        host=setting.server_host,
        port=setting.server_port,
        reload=True,
        log_level=logging.INFO
    )

    server = uvicorn.Server(config)

    asyncio.run(server.serve())


if __name__ == "__main__":
    run_application()
