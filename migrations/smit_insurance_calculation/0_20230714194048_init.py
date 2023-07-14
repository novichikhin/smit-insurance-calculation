from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "rates" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "date" DATE NOT NULL,
    "cargo_type" VARCHAR(5) NOT NULL,
    "ratio" DOUBLE PRECISION NOT NULL,
    CONSTRAINT "uid_rates_date_9d5fa2" UNIQUE ("date", "cargo_type")
);
COMMENT ON COLUMN "rates"."cargo_type" IS 'GLASS: glass\nOTHER: other';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
