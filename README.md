# REAL-ESTATE
 WEBSCRAPPING REAL ESTATE PROJECTS 

The provided code and configuration file are used to scrape information from a web page, particularly a project page, and store specific details, specifications, and features into a JSON file. Below, I'll explain what the code does, the libraries required, how to install them, and the purpose of the configuration file.

**Libraries Required:**

- Requests: Used for making HTTP requests to fetch the web page.
Install it using pip:
pip install requests

- BeautifulSoup (from the bs4 package): Used for parsing the HTML content of the web page.
Install it using pip:
pip install beautifulsoup4

- urllib.parse: Used for parsing the URL.
This library is part of Python's standard library, so there's no need to install it separately.

- json: Used for creating and writing JSON files.
This library is part of Python's standard library.

**Explanation of the Code:**

1. Import necessary libraries and modules.

2. Define functions for extracting and storing specifications and features from the web page.

3. Read a project URL from the user.

4. Send an HTTP GET request to the provided URL and check if the response status code is 200 (which means a successful request).

5. If the request is successful, parse the HTML content of the web page using BeautifulSoup.

6. Create a dictionary (project_data) to store the scraped data.

7. Extract and store project details, specifications, and features using the defined functions and configuration settings.

8. Determine the output filename from the URL and save the scraped data as a JSON file.

9. If the URL cannot be fetched (status code not 200), display an error message.

**Explanation of Configuration File (config.py)**

- The configuration file (config.py) contains settings for identifying and extracting specific information from the web page. It is used to customize the data extraction process for different types of web pages.

- PROJECT_DETAILS_CONFIG: Configuration settings for extracting project details. It includes information about the HTML tags and attributes used to identify project details, such as project name, location, description, and additional details.

- SPECIFICATIONS_CONFIG: Configuration settings for extracting specifications. It includes information about the HTML tags used for specification titles, specification content, and images.

- FEATURES_CONFIG: Configuration settings for extracting features. It includes information about the HTML tags used for feature descriptions.

By using these configuration settings, you can adapt the code to work with different web pages by modifying the HTML structure identifiers in the configuration file without changing the code's core logic.






