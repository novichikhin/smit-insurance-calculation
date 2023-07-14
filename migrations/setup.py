from smit_insurance_calculation.core import models

setting = models.Setting()

TORTOISE_ORM = {
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
            "models": ["smit_insurance_calculation.core.models.tortoise.rate", "aerich.models"],
            "default_connection": "default"
        }
    }
}
