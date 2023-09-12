

# Configuration for project details extraction


# config.py

PROJECT_DETAILS_CONFIG = {
    "overview_section": {"id": "project-overview"},
    "project_name": {"tag": "h2", "class_": "col-xxl-10 col-xl-10 col-lg-2 col-sm-2 col-xs-2 col-10"},
    "project_location": {"tag": "h5"},
    "project_description": {"tag": "p"},
    "additional_details": {"class_": "overdetails"},

    


}


# Configuration for specifications extraction
SPECIFICATIONS_CONFIG = {
    "section_id": "Specifications",
    "spec_title_tags": ["h3"],
    "spec_content_tags": ["p"],
    "image_tags": ["img"]
}

# Configuration for features extraction
FEATURES_CONFIG = {
    "section_id": "Features",
    "feature_tags": ["li"]
}
