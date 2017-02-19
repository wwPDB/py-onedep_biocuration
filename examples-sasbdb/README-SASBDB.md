# README

---
Title: README.md (examples-sasbdb)
Author: jdw
Date:  17-Feb-2017
Updated: 19-Feb-2017
---

### Example Files

Example files for the SASBDB content request service.

```
onedep_biocuration_apikey_sasbdb.jwt   JSON Web Token API Key
request-entry-report.py                Python example for entry-level content request
request-entry-report.sh                CLI example for entry-level content request

```

### Example Service Content Type Definitions

#### Example Entry-level Content Definition

The following JSON snippet describes an example entry-level content type definition.  The content
items refer to PDBx/mmCIF category and attribute names.

```json
 "report-entry-example-sasbdb": {
        "content": {
            "pdbx_database_status": [
                "status_code",
                "author_release_status_code",
                "deposit_site",
                "process_site",
                "recvd_initial_deposition_date",
                "date_of_NDB_release"
            ],
            "struct": [
                "entry_id",
                "title"
            ],
            "database_2": [
                "database_id",
                "database_code"
            ],
            "entity": [
                "id",
                "type",
                "src_method",
                "pdbx_description",
                "pdbx_number_of_molecules"
            ],
            "entity_poly": [
                "entity_id",
                "type",
                "nstd_linkage",
                "nstd_monomer",
                "pdbx_seq_one_letter_code",
                "pdbx_seq_one_letter_code_can"
            ],
            "audit_author": [
                "name",
                "pdbx_ordinal"
            ],
            "pdbx_database_related": [
                "db_name",
                "db_id",
                "content_type"
            ]
        },
        "conditions": {},
        "type": "entry"
    }
```
