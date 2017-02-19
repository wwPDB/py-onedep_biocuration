# README

---
Title: README.md (examples-emdb)
Author: jdw
Date:  17-Feb-2017
Updated: 19-Feb-2017
---

### Example Files

Example files for the EMDB content request service.

```
onedep_biocuration_apikey_emdb.jwt   JSON Web Token API Key
request-entry-report.py              Python example for entry-level content request
request-entry-report.sh              CLI example for entry-level content request
request-summary-report.py            Python example for summary report content request
request-summary-report.sh            CLI example for summary report content request

```

### Example Service Content Type Definitions

#### Example Summary Content Definition

The following JSON snippet describes an example summary content type definition. The content
items refer to table and column names in the various OneDep database schema.

```json

 "report-summary-example-emdb-status": {
        "content": {
            "deposition": [
                "dep_set_id",
                "pdb_id",
                "initial_deposition_date",
                "status_code",
                "author_release_status_code",
                "title",
                "title_emdb",
                "author_list",
                "author_list_emdb",
                "exp_method",
                "status_code_exp",
                "emdb_id",
                "status_code_emdb",
                "dep_author_release_status_code_emdb"
            ],
            "em_admin": [
                "entry_id",
                "structure_id",
                "title",
                "map_release_date",
                "deposition_date"
            ]
        },
        "resource": {
            "deposition": [
                "status",
                "status"
            ],
            "em_admin": [
                "da_internal",
                "da_internal"
            ]
        },
        "conditions": {
            "deposition": {
                "exp_method": [
                    "ELECTRON MICROSCOPY",
                    "char",
                    "LIKE"
                ]
            }
        },
        "type": "rdbms"
    }

```

#### Example Entry-level Content Definition

The following JSON snippet describes an example entry-level content type definition.  The content
items refer to PDBx/mmCIF category and attribute names.  This content definition may be applied
to data files within both the deposition and biocuration systems, dialects for both EM namespaces
are included in this example.

```json
  "report-entry-example-emdb": {
        "content": {
            "pdbx_database_status": [
                "status_code",
                "author_release_status_code",
                "deposit_site",
                "process_site",
                "recvd_initial_deposition_date",
                "date_of_NDB_release"
            ],
            "entity_poly": [
                "entity_id",
                "type",
                "nstd_linkage",
                "nstd_monomer",
                "pdbx_seq_one_letter_code",
                "pdbx_seq_one_letter_code_can"
            ],
            "emd_admin": [
                "entry_id",
                "current_status",
                "deposition_date",
                "deposition_site",
                "details",
                "map_hold_date",
                "last_update",
                "map_release_date",
                "obsoleted_date",
                "replace_existing_entry_flag",
                "title",
                "header_release_date"
            ],
            "database_2": [
                "database_id",
                "database_code"
            ],
            "em_map": [
                "id",
                "annotation_details",
                "axis_order_fast",
                "axis_order_medium",
                "axis_order_slow",
                "cell_a",
                "cell_alpha",
                "cell_b",
                "cell_beta",
                "cell_c",
                "cell_gamma",
                "contour_level",
                "contour_level_source",
                "data_type",
                "dimensions_col",
                "dimensions_row",
                "dimensions_sec",
                "endian_type",
                "file",
                "format",
                "label",
                "limit_col",
                "limit_row",
                "limit_sec",
                "origin_col",
                "origin_row",
                "origin_sec",
                "partition",
                "pixel_spacing_x",
                "pixel_spacing_y",
                "pixel_spacing_z",
                "size_kb",
                "spacing_x",
                "spacing_y",
                "spacing_z",
                "statistics_average",
                "statistics_maximum",
                "statistics_minimum",
                "statistics_std",
                "symmetry_space_group",
                "type"
            ],
            "entity": [
                "id",
                "type",
                "src_method",
                "pdbx_description",
                "pdbx_number_of_molecules"
            ],
            "struct": [
                "entry_id",
                "title"
            ],
            "em_admin": [
                "entry_id",
                "current_status",
                "deposition_date",
                "deposition_site",
                "details",
                "map_hold_date",
                "last_update",
                "map_release_date",
                "obsoleted_date",
                "replace_existing_entry_flag",
                "title",
                "header_release_date"
            ],
            "emd_map": [
                "id",
                "contour_level",
                "contour_level_source",
                "annotation_details",
                "file",
                "original_file",
                "label",
                "type",
                "partition",
                "format",
                "size_kb",
                "axis_order_fast",
                "axis_order_medium",
                "axis_order_slow",
                "cell_alpha",
                "cell_beta",
                "cell_gamma",
                "cell_a",
                "cell_b",
                "cell_c",
                "data_type",
                "dimensions_col",
                "dimensions_row",
                "dimensions_sec",
                "origin_col",
                "origin_row",
                "origin_sec",
                "limit_col",
                "limit_row",
                "limit_sec",
                "pixel_spacing_x",
                "pixel_spacing_y",
                "pixel_spacing_z",
                "symmetry_space_group",
                "spacing_x",
                "spacing_y",
                "spacing_z",
                "statistics_minimum",
                "statistics_maximum",
                "statistics_average",
                "statistics_std",
                "endian_type"
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