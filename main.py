from functions.CreateHousehold import create_hh
from functions.AddMember import add_mb
from functions.SearchHousehold import search_hh
from functions.ListGrants import list_grants

import functions_framework  # Only for local development, do not include in deployment

@functions_framework.http # Only for local development, do not include in deployment
def gov_grant_disb(request):
    
    allowed_methods: tuple = ("POST", "GET")
    allowed_paths: tuple = ("/create_hh", "/add_mb", "/search_hh", "/list_grants")

    # Check if method is allowed
    if request.method not in allowed_methods:
        return {"msg": "Unknown request"}, 405

    # Check if path is allowed/implemented
    if request.path not in allowed_paths:
        return {"msg": "Unknown request"}, 400

    # Route to each path's function
    function = request.path
    print(function)

    if function == "/create_hh":
        return create_hh(request)
    elif function == "/add_mb":
        return add_mb(request)
    elif function == "/search_hh":
        return search_hh(request)
    elif function == "/list_grants":
        return list_grants(request)

    return {"msg": "Unknown request"}, 200