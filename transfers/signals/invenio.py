#!/usr/bin/env python

# Send the status to Invenio. You can setup the IP in the config variable
# at the top of this file.

import requests

INVENIO_URL = "http://127.0.0.1:5000/api/oais/archive/{}/"
"""IP addresse of the Invenio server."""

def main(path, unit_type, status, uuid, accession_id):
    if unit_type == "ingest" and status == "PROCESSING":
        status = "AIP_PROCESSING"
    params = {
        "accession_id": accession_id,
        "status": status,
        "archivematica_id": uuid
    }
    response = requests.patch(INVENIO_URL.format(accession_id), json=params)
    if not response.ok:
        # TODO
        pass


if __name__ == '__main__':
    path = sys.argv[1]
    unit_type = sys.argv[2]  # String True or False
    status = sys.argv[3]
    uuid = sys.argv[4]
    accession_id = sys.argv[5]
    sys.exit(main(path, unit_type, status, uuid, accession_id))
