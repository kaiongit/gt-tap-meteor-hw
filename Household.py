class Household:
    ALLOWED_HOUSING_TYPE: tuple = ("landed", "condo", "hdb", "others")

    def __init__(self, housing_type: str):
        if not self._check_housing_type(housing_type): raise ValueError("Housing Type is invalid")

        self.housing_type: str = housing_type
    
    def _check_housing_type(self, housing_type: str) -> bool:
        if housing_type not in self.ALLOWED_HOUSING_TYPE: return False
        return True

    def to_dict(self) -> dict:
        return self.__dict__

    @staticmethod
    def from_dict(household: dict):
        housing_type: str = household.get("housing_type", "").lower()

        return Household(housing_type)
