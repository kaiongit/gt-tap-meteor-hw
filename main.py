from functions.CreateHousehold import create_hh
from functions.AddMember import add_mb
from functions.SearchHousehold import search_hh
from functions.ListGrants import list_grants

import functions_framework  # Only for local development, do not include in deployment

@functions_framework.http # Only for local development, do not include in deployment
def gov_grant_disb(request):
    
    allowed_methods: tuple = ("POST", "GET")

    allowed_requests: list = [
        {"method": "POST", "path": "/create_hh"},
        {"method": "POST", "path": "/add_mb"},
        {"method": "GET", "path": "/search_hh"},
        {"method": "GET", "path": "/list_grants"},
    ]

    method = request.method

    # Check if method is allowed
    if method not in allowed_methods:
        return {"msg": "Unknown request"}, 405

    path = request.path
    allowed = False

    for allowed_request in allowed_requests:
        if method == allowed_request["method"] and path == allowed_request["path"]:
            allowed = True

    # Check if path is allowed/implemented
    if not allowed:
        return {"msg": "Unknown request"}, 400

    if path == "/create_hh":
        return create_hh(request)
    elif path == "/add_mb":
        return add_mb(request)
    elif path == "/search_hh":
        return search_hh(request)
    elif path == "/list_grants":
        return list_grants(request)

    return {"msg": "Unknown request"}, 400