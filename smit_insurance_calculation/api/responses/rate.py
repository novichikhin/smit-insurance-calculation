from smit_insurance_calculation.api.responses.main import BaseResponse


class RateNotFound(BaseResponse):
    detail: str = "Rate not found"
