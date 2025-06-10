#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 07:55:41 2025

Find papers using ElectraSyn from Google Scholar.

Version history
1.0.0       Search for a specific quantity of publications using scholarly.
1.1.0       Use serpapi because scholarly is blocked by Google.
1.2.0       Change the data type of collect_electrasyn_publications()'s output to DataFrame.
            Add Lens.org metadata enrichment using paper title.

@author: cj
"""


import pandas as pd
import requests
import xlsxwriter
import time
from datetime import datetime




### PARAMETERS ###
# Get SerpApi API key.
SERPAPI_KEY = "01f35978095e9e4e441c15ce0da63050bba53a4a998670ae448daef9ac135168" # Personal key
SERPAPI_KEY = "42c510565cb68f0e659192598cc5ffd0de483128ef6588cd43766f569b7dbdc7" # charles.jiao@ika.net key
# Get SerApi license key.
LENS_API_KEY = "xWloyzMKGx1M8dRVFBMs06VuK8Nr3MnnOwGC4cUXzEOmIXHh1VnE"
# Set key word.
query = "ElectraSyn 2.0"
# Decide the searching time span.
year_from = 2017
year_to = 2025
# Decide the maximum number of search results.
num_results = 100000
# Get current date & time.
now = datetime.now()
# Format as string: YYYYMMDD_HHMMSS
timestamp_str = now.strftime("%Y%m%d_%H%M%S")
# Name the output file path.
filepath = "Export/ElectraSyn Publications" + timestamp_str



def fetch_google_scholar_results(query, year_from, year_to, num_results):
    """
    Fetch Google Scholar results.

    Parameters
    ----------
    query : str
        Key word to search.
    year_from : int
        The earliest year to search.
    year_to : int
        The latest year to search.
    num_results : int
        Maximum number of search results.

    Returns
    -------
    all_results : list
        All of the search results.

    """
    
    # Initialize a list of all search results.
    all_results = []
    # Set search result per page.
    results_per_page = 20  # SerpAPI limit
    # Iterate each page of search result.
    for start in range(0, num_results, results_per_page):
        # Update the progress.
        print(f"Fetching results {start} to {start + results_per_page}...")
        # Set parameters for GET request..
        parameters = {
            "engine": "google_scholar",
            "q": query,
            "as_ylo": year_from,
            "as_yhi": year_to,
            "api_key": SERPAPI_KEY,
            "num": results_per_page,
            "start": start
        }
        # Send a .get() request to the SERP API endpoint to retrieve search results.
        response = requests.get('https://serpapi.com/search.json', params=parameters)
        # Raise an exception if the request was not successful (status code >= 400).
        response.raise_for_status()
        # Extract organic search results from the JSON response or initialize as an empty list.
        page_results = response.json().get("organic_results", [])
        # If no organic results are returned.
        if not page_results:
            # Print a message and exit the loop early
            print("No more results found, stopping early.")
            break
        # Add this page's search results to the cumulative list of all results.
        all_results.extend(page_results)
        # Avoid rate limiting.
        time.sleep(1)  # Be nice to SerpAPI rate limits
    
    return all_results

 
def fetch_lens_metadata(title, api_key):
    """
    

    Parameters
    ----------
    title : str
        Title of the paper.
    api_key : str
        Lens API key.

    Returns
    -------
    dict
        Enriched data.

    """
    # Set up the request headers including the Lens API key for authorization.
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    # Define the body of the POST request using a boolean query with match_phrase on the title.
    body = {
        "query": {
            "bool": {
                "must": [
                    {"match_phrase": {"title": title}}
                ]
            }
        },
        "size": 1  # Limit the number of search results to 1 (we only want the best match)
    }
    # Send the POST request to the Lens Scholarly API.
    response = requests.post("https://api.lens.org/scholarly/search", headers=headers, json=body)
    # Check if the request was successful.
    if response.status_code != 200:
        # Print an error message if the API response indicates failure.
        print(f"Lens API error for title: {title}")
        return {}
    # Parse the JSON response and get the list of results under "data".
    results = response.json().get("data", [])
    # Return the first result if any are found; otherwise, return an empty dictionary.
    return results[0] if results else {}



def collect_electrasyn_publications():
    """
    Collect a list of papers and their information.

    Returns
    -------
    papers : pandas.core.frame.DataFrame
        A list of papers with their information.

    """
    
    # Get search results.
    results = fetch_google_scholar_results(query, year_from, year_to, num_results)
    # Initialize a list for all papers.
    papers = []
    # Iterate each search result.
    for result in results:
        # Get the title of the paper.
        title = result.get("title")
        # Get the link to the paper.
        link = result.get("link")
        # Extract Authors.
        authors_data = result.get("publication_info", {}).get("authors", [])
        # If author information is retrieved as a list.
        if isinstance(authors_data, list):
            # Write co-author names in string.
            authors = ', '.join([author.get('name', '') for author in authors_data])
        # If author information is unavailable.
        else:
            authors = "Unknown"
        # Get the summary of publication information.
        summary = result.get("publication_info", {}).get("summary", "")
        # Initialize default journal information.
        journal_info = "Unknown"
        # Initialize default publication year.
        publication_year = "Unknown"
        # Iterate each publication's summary that has "-".
        if summary and " - " in summary:
            # Break down summary into parts.
            parts = summary.split(" - ")
            # If journal information is in summary (more than two parts).
            if len(parts) >= 2:
                # Set journal information properly.
                journal_info = parts[1].split(",")[0].strip()
                # Get information (that contains month) after comma.
                publication_year = parts[1].split(",")[-1].strip()

        # Fetch additional metadata from the Lens API based on the paper title.
        lens_data = fetch_lens_metadata(title, LENS_API_KEY)
        # Attempt to extract the full publication date from the metadata.
        publication_date = lens_data.get("publication_date", "Unknown")        
        # Default the publication month to "Unknown" unless we can parse it.
        publication_month = "Unknown"
        # Iterate aeach vailable publication date.
        if publication_date and publication_date != "Unknown":
            try:
                # Parse the date string and extract the full month name (e.g., "March")
                publication_month = datetime.strptime(publication_date, "%Y-%m-%d").strftime("%B")
            except:
                # Silently ignore parsing errors and leave month as "Unknown"
                pass
        # Initialize sets to store unique country codes.
        countries = set()
        # Initialize sets to store unique city names.
        cities = set()
        # Initialize sets to store unique institution names from authors' affiliations.
        institutions = set()
        # Iterate each author listed in the metadata.
        for author in lens_data.get("authors", []):
            # Iterate through each author's list of affiliations.
            for aff in author.get("affiliations", []):
                # If country code is available, add it to the countries set.
                if aff.get("country_code"):
                    countries.add(aff["country_code"])
                # If city name is available, add it to the cities set.
                if aff.get("city"):
                    cities.add(aff["city"])
                # If institution name is available, add it to the institutions set.
                if aff.get("name"):
                    institutions.add(aff["name"])
        # Extract the list of fields of study if present, otherwise use an empty list.
        fields_of_study = lens_data.get("fields_of_study", [])
        # Extract the abstract text if available, otherwise use an empty string.
        abstract = lens_data.get("abstract", "")
        # Add this paper and its information.
        papers.append({
            # Get the title of the paper.
            "Title": title,
            # Get the author names of the paper.
            "Authors": authors,
            # Get the journal information where the paper was published.
            "Journal": journal_info,
            # Get the year when the paper was published.
            "Year": publication_year,
            # Get the month when the paper was published.
            "Month": publication_month,
            # Get the link to the paper.
            "Link": link,
            # Get the country where author's institution is.
            "Country": "; ".join(sorted(countries)) if countries else "Unknown",
            # Get the city where author's institution is.
            "City": "; ".join(sorted(cities)) if cities else "Unknown",
            # Get the institute name.
            "Institutions": "; ".join(sorted(institutions)) if institutions else "Unknown",
            # Get the application.
            "Applications": "; ".join(fields_of_study) if fields_of_study else abstract[:200]
        })
    # Convert to DataFrame.
    papers = pd.DataFrame(papers)
    # Sort the DataFrame.
    papers = papers.sort_values(by='Year', ascending=False)
    
    return papers



def save_to_xlsx(data, filename):
    """
    

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A list of papers with their information.
    filename : str
        The name of the output file.

    Returns
    -------
    None.

    """
    # If there is no data.
    if data.empty:
        # Print warning.
        print("No data to write.")
        return
    # Save DataFrame to Excel
    data.to_excel(filename, index=False)
    # Print confirmation.
    print(f"Data saved to {filename}.")



def write_a_memo():
    """
    Write a txt. file of what year's papers are collected.

    Returns
    -------
    None.

    """
    # Save as txt. file
    memo_filename = filepath + ".txt"
    # Edit the file.
    with open(memo_filename, 'w', encoding='utf-8') as f:
        # Write message to that file.
        f.write(f"Publications from {year_from} to {year_to} saved.")



def main():
    papers = collect_electrasyn_publications()
    save_to_xlsx(papers, filepath+'.xlsx')
    write_a_memo()


if __name__ == '__main__':
    main()