from datetime import datetime

class Person:
    ALLOWED_GENDERS: tuple = ("male", "female", "others")
    ALLOWED_MARITAL_STATUS: tuple = ("single", "married", "divorced", "widowed")
    ALLOWED_OCCUPATION_TYPE: tuple = ("student", "unemployed", "employed")
    INPUT_ERROR_MSG_FORMAT: str = "{} is invalid"

    def __init__(self, name: str, gender: str, marital_status: str, spouse: str, 
        occupation_type: str, annual_income: float, dob: int):
        
        if not self._check_name(name): raise ValueError("Name is invalid")
        if not self._check_gender(gender): raise ValueError("Gender is invalid")
        if not self._check_marital_status(marital_status): 
            raise ValueError("Marital Status is invalid")
        if not self._check_spouse(spouse, marital_status): raise ValueError("Spouse is invalid")
        if not self._check_occupation_type(occupation_type): 
            raise ValueError("Occupation Type is invalid")
        if not self._check_annual_income(annual_income, occupation_type): 
            raise ValueError("Annual Income is invalid")
        if not self._check_dob(dob): raise ValueError("DOB is invalid")

        self.name: str = name
        self.gender: str = gender
        self.marital_status: str = marital_status
        self.spouse: str = spouse
        self.occupation_type: str = occupation_type
        self.annual_income: float = annual_income
        self.dob: int = dob
        
    def _check_name(self, name: str) -> bool:
        if len(name) == 0: return False
        return True

    def _check_gender(self, gender: str) -> bool:
        if gender not in self.ALLOWED_GENDERS: return False
        return True

    def _check_marital_status(self, marital_status: str) -> bool:
        if marital_status not in self.ALLOWED_MARITAL_STATUS: return False
        return True

    def _check_spouse(self, spouse: str, marital_status: str) -> bool:
        if marital_status == "married" and len(spouse) == 0: return False
        if marital_status != "married" and len(spouse) > 0: return False
        return True

    def _check_occupation_type(self, occupation_type: str) -> bool:
        if occupation_type not in self.ALLOWED_OCCUPATION_TYPE: return False
        return True

    def _check_annual_income(self, annual_income: float, occupation_type: str):
        if occupation_type == "employed" and annual_income == 0.0: return False
        return True

    def _check_dob(self, dob: int) -> bool:
        try:
            datetime.strptime(str(dob), "%Y%m%d")
            return True
        except ValueError:
            return False

    def to_dict(self) -> dict:
        return self.__dict__

    @staticmethod
    def from_dict(person: dict):
        name: str = person.get("name", "").lower()
        gender: str = person.get("gender", "").lower()
        marital_status: str = person.get("marital_status", "").lower()
        spouse: str = person.get("spouse", "").lower()
        occupation_type: str = person.get("occupation_type", "").lower()
        annual_income: float = person.get("annual_income", 0.0) * 1.0
        dob: int = person.get("dob", 0) * 1

        return Person(name, gender, marital_status, spouse, occupation_type, annual_income, dob)
