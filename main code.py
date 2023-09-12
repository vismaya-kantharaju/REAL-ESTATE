import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import json
from config import PROJECT_DETAILS_CONFIG, SPECIFICATIONS_CONFIG, FEATURES_CONFIG

def extract_and_store_specifications(soup, data):
    specifications_data = {}
    
    specifications_section = soup.find("section", {"id": SPECIFICATIONS_CONFIG["section_id"]})
    if specifications_section:
        spec_title_tags = SPECIFICATIONS_CONFIG["spec_title_tags"]
        spec_content_tags = SPECIFICATIONS_CONFIG["spec_content_tags"]
        image_tags = SPECIFICATIONS_CONFIG["image_tags"]

        current_spec_title = None
        for spec in specifications_section.find_all(spec_title_tags + spec_content_tags + image_tags):
            if spec.name in spec_title_tags:
                current_spec_title = spec.get_text(strip=True)
                specifications_data[current_spec_title] = []
            elif spec.name in spec_content_tags:
                if current_spec_title:
                    specifications_data[current_spec_title].append(spec.get_text(strip=True))
            elif spec.name in image_tags:
                specifications_data[current_spec_title].append(str(spec))

    data["Specifications"] = specifications_data

def extract_and_store_features(soup, data):
    features_data = []
    features_section = soup.find("section", {"id": FEATURES_CONFIG["section_id"]})
    if features_section:
        features = features_section.find_all(FEATURES_CONFIG["feature_tags"])
        for feature in features:
            features_data.append(feature.get_text(strip=True))

    data["Features"] = features_data

# Define the URL of the project page
project_url = input("Enter the project URL: ")

response = requests.get(project_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Create a dictionary to store the data
    project_data = {}

    # Extract and store project details
    project_details_data = {}
    project_details_section = soup.find("section", {"id": PROJECT_DETAILS_CONFIG["overview_section"]["id"]})
    if project_details_section:
        additional_details_section = project_details_section.find_all(**PROJECT_DETAILS_CONFIG["additional_details"])
        for detail in additional_details_section:
            detail_span = detail.find("span")
            detail_value = detail.get_text(strip=True).replace(detail_span.text, "")
            project_details_data[detail_span.text] = detail_value

    # Extract project name
        project_name_element = project_details_section.find(**PROJECT_DETAILS_CONFIG["project_name"])
        if project_name_element:
            project_name = project_name_element.get_text(strip=True)
            print("Project Name:", project_name)

        
        # Extract project location
        project_location_element = project_details_section.find(**PROJECT_DETAILS_CONFIG["project_location"])
        if project_location_element:
            project_location = project_location_element.get_text(strip=True)
            print("Project Location:", project_location)

        
        # Extract project description
        project_description_element = project_details_section.find(**PROJECT_DETAILS_CONFIG["project_description"])
        if project_description_element:
            project_description = project_description_element.get_text(strip=True)
            print("Project Description:", project_description)



    project_data["Project Details"] = project_details_data

    # Extract and store specifications
    extract_and_store_specifications(soup, project_data)

    # Extract and store features
    extract_and_store_features(soup, project_data)

    # Extract the filename from the URL
    parsed_url = urlparse(project_url)
    file_name = os.path.basename(parsed_url.path)
    if not file_name:
        # If the URL doesn't contain a filename, you can specify a default name or generate one
        file_name = "output.json"

    # Save the data as a JSON file
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(project_data, json_file, indent=4)

    print(f"Data saved to {file_name} as a JSON file.")
else:
    print("Failed to fetch the URL.")
