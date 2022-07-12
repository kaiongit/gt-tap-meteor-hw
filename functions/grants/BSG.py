from datetime import datetime, timedelta

def BSG(households: list) -> list:
    # Filter households eligible
    hh_eligible: list = [e for e in households if household_has_members_younger_than_8mos(e)]

    # Filter members eligible
    mb_eligible: list = [only_members_below_8mos(e) for e in hh_eligible]

    # Remove households with empty members
    mb_eligible = [e for e in mb_eligible if e]
    
    return hh_eligible

def household_has_members_younger_than_8mos(household: dict) -> bool:
    # Retrieve list of memebers
    members: list = household["members"]

    # Filter to only include members that are 8mos or younger
    below_8mos: list = [member for member in members if member_is_younger_than_8mos(member)]
    
    # Return True if there is more than 1 member 8mos or younger
    return len(below_8mos) > 0

def member_is_younger_than_8mos(member: dict) -> bool:
    # Convert dob into datetime object
    dob_datetime = datetime.strptime(str(member["dob"]), "%Y%m%d")

    # Calculate age as today's date subtract dob 
    time_difference = datetime.today() - dob_datetime
    day_difference = time_difference.days
    month_difference = int((day_difference / 365) * 12)

    # Return true if age is 8mos or below
    return month_difference <= 8

def only_members_below_8mos(household: dict) -> dict:
    # Retrieve list of members
    members: list = household["members"]

    # Filter to only include members that are 8mos or younger
    babies: list = [member for member in members if member_is_younger_than_8mos(member)]

    # If there is no eligible members, return nothing
    if len(babies) == 0: return None

    # Otherwise, return eligible members
    household["members"] = babies
    return household
