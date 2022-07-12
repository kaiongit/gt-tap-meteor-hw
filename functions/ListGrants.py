import GlobalConstants
from flask import jsonify, request
from google.cloud import firestore
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference

from functions.grants import BSG, ELB, MGS, SEB, YGG


def list_grants(request: request):

    ALLOWED_GRANTS = ("seb", "mgs", "elb", "bsg", "ygg")

    # Check if arg is given
    arg_dict: dict = request.args
    grant_name: str = arg_dict.get("grant_name", None).lower()
    
    if not grant_name or grant_name not in ALLOWED_GRANTS:
        return jsonify({"msg": "Grant Name not valid"}), 400
    
    # Get DB
    client: firestore.Client = firestore.Client(project=GlobalConstants.GCLOUD_PROJECT_NAME)
    col_ref: CollectionReference = client.collection(GlobalConstants.FIRESTORE_COLLECTION_NAME)

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

    # Invoke grant determination functions
    elig_hh: list = []

    if grant_name == "seb":
        elig_hh = SEB.SEB(households)
    elif grant_name == "mgs":
        elig_hh = MGS.MGS(households)
    elif grant_name == "elb":
        elig_hh = ELB.ELB(households)
    elif grant_name == "bsg":
        elig_hh = BSG.BSG(households)
    elif grant_name == "ygg":
        elig_hh = YGG.YGG(households)

    return jsonify(elig_hh), 200
