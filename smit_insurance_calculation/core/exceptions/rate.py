from smit_insurance_calculation.core.exceptions.main import BaseAppException


class RateNotFound(BaseAppException):

    @property
    def message(self) -> str:
        return "Rate not found"
