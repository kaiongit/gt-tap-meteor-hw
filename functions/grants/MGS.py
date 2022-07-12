from datetime import datetime, timedelta

def MGS(households: list):
    # Filter households eligible
    hh_eligible: list = [e for e in households if household_income_less_than_150000(e)]
    hh_eligible = [e for e in households if household_has_members_older_than_55_or_younger_than_18(e)]

    return hh_eligible

def household_income_less_than_150000(household: dict) -> bool:
    # Retrieve list of members
    members: list = household["members"]

    # Sum the annual_income of all members
    total_income = sum([member["annual_income"] for member in members])

    # Return True if sum of annual_income is less than 150000
    return total_income < 150000

def household_has_members_older_than_55_or_younger_than_18(household: dict) -> bool:
    # Retrieve list of memebers
    members: list = household["members"]

    # Filter to only include members that are 55 or older
    above_55s: list = [member for member in members if member_is_older_than_55(member)]

    # Filter to only include members that are 18 or younger
    below_18s: list = [member for member in members if member_is_younger_than_18(member)]
    
    print("55", above_55s, "18", below_18s)

    # Return True if there is more than 1 member 55 or older
    return len(above_55s) > 0 or len(below_18s) > 0

def member_is_older_than_55(member: dict) -> bool:
    # Convert dob into datetime object
    dob_datetime = datetime.strptime(str(member["dob"]), "%Y%m%d")

    # Calculate age as today's date subtract dob 
    age = (datetime.today() - dob_datetime) // timedelta(days=365.2425)

    # Return true if age is 55 or above
    return age >= 55

def member_is_younger_than_18(member: dict) -> bool:
    # Convert dob into datetime object
    dob_datetime = datetime.strptime(str(member["dob"]), "%Y%m%d")

    # Calculate age as today's date subtract dob 
    age = (datetime.today() - dob_datetime) // timedelta(days=365.2425)

    # Return true if age is 18 or lower
    return age <= 18