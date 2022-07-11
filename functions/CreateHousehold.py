import GlobalConstants
from flask import jsonify, request
from google.cloud import firestore
from google.cloud.firestore_v1.collection import CollectionReference
from objects.Household import Household

def create_hh(request: request):

    request_dict: dict = request.get_json(silent=True)
    request_dict = request_dict if request_dict else {}
    
    try:
        household: Household = Household.from_dict(request_dict)
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

    client: firestore.Client = firestore.Client(project=GlobalConstants.GCLOUD_PROJECT_NAME)
    col_ref: CollectionReference = client.collection(GlobalConstants.FIRESTORE_COLLECTION_NAME)

    try:
        _, doc_ref = col_ref.add(household.to_dict())
    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"msg": "An error has occured"}), 500

    return jsonify({"hh_id": doc_ref.id}), 201
