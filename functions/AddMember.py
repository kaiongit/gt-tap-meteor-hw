import GlobalConstants
from flask import jsonify, request
from google.cloud import firestore
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from objects.Person import Person

def add_mb(request: request):
    
    # Validate person information
    request_dict: dict = request.get_json(silent=True)
    request_dict = request_dict if request_dict else {}

    try:
        person: Person = Person.from_dict(request_dict)
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

    # Get DB
    client: firestore.Client = firestore.Client(project=GlobalConstants.GCLOUD_PROJECT_NAME)
    col_ref: CollectionReference = client.collection(GlobalConstants.FIRESTORE_COLLECTION_NAME)
    
    # Validate hh_id exists
    hh_id: str = request_dict.get("hh_id", None)
    if not hh_id or len(hh_id) == 0:
        return jsonify({"msg": "hh_id not found"}), 404

    hh_doc_ref: DocumentReference = col_ref.document(hh_id)
    hh_doc: DocumentSnapshot = hh_doc_ref.get()

    if not hh_doc.exists:
        return jsonify({"msg": "hh_id not found"}), 404
    
    # Create new member in household
    try:
        hh_doc_col_ref: CollectionReference = \
            hh_doc_ref.collection(GlobalConstants.FIRESTORE_SUBCOLLECTION_NAME)
        _, member_doc_ref = hh_doc_col_ref.add(person.to_dict())
    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"msg": "An error has occured"}), 500

    return "", 201
