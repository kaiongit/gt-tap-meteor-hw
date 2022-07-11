from datetime import datetime, timedelta

def ELB(households: list) -> list:
    # Filter households eligible
    hh_eligible: list = [e for e in households if household_has_members_older_than_55(e)]

    return hh_eligible

def household_has_members_older_than_55(household: dict) -> bool:
    # Retrieve list of memebers
    members: list = household["members"]

    # Filter to only include members that are 55 or older
    above_55s: list = [member for member in members if member_is_older_than_55(member)]
    
    # Return True if there is more than 1 member 55 or older
    return len(above_55s) > 0

def member_is_older_than_55(member: dict) -> bool:
    # Convert dob into datetime object
    dob_datetime = datetime.strptime(str(member["dob"]), "%Y%m%d")

    # Calculate age as today's date subtract dob 
    age = (datetime.today() - dob_datetime) // timedelta(days=365.2425)

    # Return true if age is 55 or above
    return age >= 55
