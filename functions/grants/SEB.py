from datetime import datetime, timedelta

def SEB(households: list):
    # Filter households eligible
    hh_eligible: list = [e for e in households if household_with_members_that_are_students(e)]

    # Filter members eligible
    mb_eligible: list = [only_members_below_16(e) for e in hh_eligible]

    # Remove households with empty members
    mb_eligible = [e for e in mb_eligible if e]

    return mb_eligible

def household_with_members_that_are_students(household: dict) -> bool:
    # Retrieve list of members
    members: list = household["members"]

    # Filter to only include members that are students
    students: list = [member for member in members if member_is_student(member)]

    # Return true if there is more than 1 students
    return len(students) > 0

def member_is_student(member: dict) -> bool:
    # Return true if member is student
    return member["occupation_type"] == "student"

def only_members_below_16(household: dict) -> dict:
    # Retrieve list of members
    members: list = household["members"]

    # Filter to only include members that are 16 or younger
    students: list = [member for member in members if member_is_below_16(member)]

    # If there is no eligible members, return nothing
    if len(students) == 0: return None

    # Otherwise, return eligible members
    household["members"] = students
    return household

def member_is_below_16(member: dict) -> bool:
    # Convert dob into datetime object
    dob_datetime = datetime.strptime(str(member["dob"]), "%Y%m%d")

    # Calculate age as today's date subtract dob 
    age = (datetime.today() - dob_datetime) // timedelta(days=365.2425)

    # Return true if age is 16 or younger
    return age <= 16
