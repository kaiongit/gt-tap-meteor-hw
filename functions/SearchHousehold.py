import GlobalConstants
from flask import jsonify, request
from google.cloud import firestore
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference

def search_hh(request: request):
    
    # Check if arg is given
    arg_dict: dict = request.args
    hh_id: str = arg_dict.get("hh_id", None)
    if hh_id is not None and len(hh_id) == 0:
        return jsonify({"msg": "Household ID not found"}), 404
    
    # Get DB
    client: firestore.Client = firestore.Client(project=GlobalConstants.GCLOUD_PROJECT_NAME)
    col_ref: CollectionReference = client.collection(GlobalConstants.FIRESTORE_COLLECTION_NAME)

    if hh_id:
        # Get household
        doc_ref: DocumentReference = col_ref.document(hh_id)
        doc: DocumentSnapshot = doc_ref.get()

        # Check if household exists
        if not doc.exists:
            return jsonify({"msg": "Household ID not found"}), 404

        doc_dict: dict = doc.to_dict()
        doc_dict["hh_id"] = hh_id

        # Get members
        members: list = []

        doc_col_ref: CollectionReference = \
            doc_ref.collection(GlobalConstants.FIRESTORE_SUBCOLLECTION_NAME)
        doc_col: list = doc_col_ref.get()

        for sdoc in doc_col:
            sdoc_dict: dict = sdoc.to_dict()
            sdoc_dict["pers_id"] = sdoc.id
            members.append(sdoc_dict)

        doc_dict["members"] = members

        return jsonify(doc_dict), 200

    else:
        households: list = []
        
        # Get docs
        docs = col_ref.get()
        
        for doc in docs:
            doc_dict: dict = doc.to_dict()
            doc_dict["hh_id"] = doc.id

            # Get members
            members: list = []

            doc_ref: DocumentReference = doc.reference
            doc_col_ref: CollectionReference = \
                doc_ref.collection(GlobalConstants.FIRESTORE_SUBCOLLECTION_NAME)
            doc_col: list = doc_col_ref.get()

            for sdoc in doc_col:
                sdoc_dict: dict = sdoc.to_dict()
                sdoc_dict["pers_id"] = sdoc.id
                members.append(sdoc_dict)

            doc_dict["members"] = members

            households.append(doc_dict)

        return jsonify(households), 200
