def YGG(households: list) -> list:
    # Filter households eligible
    hh_eligible: list = [e for e in households if household_income_less_than_100000(e)]

    return hh_eligible

def household_income_less_than_100000(household: dict) -> bool:
    # Retrieve list of members
    members: list = household["members"]

    # Sum the annual_income of all members
    total_income = sum([member["annual_income"] for member in members])

    # Return True if sum of annual_income is less than 100000
    return total_income < 100000
