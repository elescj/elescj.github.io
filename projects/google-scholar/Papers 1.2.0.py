#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 07:55:41 2025

Find papers using ElectraSyn from Google Scholar.

Version history
1.0.0       Search for a specific quantity of publications using scholarly.
1.1.0       Use serpapi because scholarly is blocked by Google.
1.2.0       xxxxxxxxxxxxxxxxxxxx

@author: cj
"""

# TODO
"""
√ Enrich datasheet information: published year.
√ Sort by recency.
* Enrich other datasheet information.
"""

import requests
import xlsxwriter
import time
from datetime import datetime




### PARAMETERS ###
# Get SerpApi API key.
SERPAPI_KEY = "personal-license"
# Get SerApi license key.
LENS_API_KEY = "xxxxxxxxx"
# Set key word.
query = "ElectraSyn 2.0"
# Decide the searching time span.
year_from = 2024
year_to = 2025
# Decide the maximum number of search results.
num_results = 10
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

 

# def fetch_lens_metadata(title, lens_api_key):
#     """
    


#     """
#     # Set the HTTP request headers
#     headers = {
#         # Set authorization header with the Lens API key.
#         "Authorization": f"Bearer {lens_api_key}",
#         # Specify the content type as JSON.
#         "Content-Type": "application/json"
#         }
#     # Prepare the query body to search for publications that match the given title.
#     body = {
#         "query": {
#             "bool": {
#                 "must": [
#                     {"match_phrase": {"title": title}}  # Match the exact phrase in the title
#                 ]
#             }
#         },
#         "size": 1  # Limit the results to 1 publication
#     }
#     # Send the POST request to the Lens.org API with the specified headers and body.
#     response = requests.post("https://api.lens.org/scholarly/search", headers=headers, json=body)
#     # Check if the request fails (status code other than 200).
#     if response.status_code != 200:
#         # Return an empty dictionary.
#         return {}
#     # Parse the JSON response to get the 'data' field.
#     results = response.json().get("data", [])
#     # Return the first result if any results are found, otherwise return an empty dictionary.
#     return results[0] if results else {}



def collect_electrasyn_publications():
    """
    Collect  a list of papers and their information.

    Returns
    -------
    papers : list
        DESCRIPTION.

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
        # Iterate each publication's summary.
        if summary:
            # Is summary is connected by "-".
            if " - " in summary:
                # Break down summary into parts.
                parts = summary.split(" - ")
                # If journal information is in summary (more than two parts).
                if len(parts) >= 2:
                    # Set journal information properly.
                    journal_info = parts[1].split(",")[0].strip()
                    # Get information (that contains month) after comma.
                    publication_year = parts[1].split(",")[-1].strip()
                    print(summary)
                    print(parts)
                    print(publication_year)
                    print(journal_info)
                    print()

        # # Enrich the metadata of search results.
        # lens_data = fetch_lens_metadata(title, LENS_API_KEY)
        # Avoid rate limiting.
        time.sleep(1)
        # # I suspect Chat made a mistake. Keep it until proven wrong
        # countries = set()
        # organizations = set()
        # research_fields = set()
        # for author in lens_data.get("authors", []):
        #     for aff in author.get("affiliations", []):
        #         if aff.get("country"):
        #             countries.add(aff["country"])
        #         if aff.get("name"):
        #             organizations.add(aff["name"])
        # for field in lens_data.get("fields_of_study", []):
        #     research_fields.add(field)

        # Add this paper to the list.
        papers.append({
            # Get the title of the paper.
            "Title": title,
            # Get the author names of the paper.
            "Authors": authors,
            # Get the journal information where the paper was published.
            "Journal": journal_info,
            # Get the year when the paper was published.
            "Year": publication_year,
            # Get the link to the paper.
            "Link": link,
            # # Get the countries where the authors are in.
            # "Countries": "; ".join(sorted(countries)) if countries else "Unknown",
            # # Get the countries where the authors belong to.
            # "Organizations": "; ".join(sorted(organizations)) if organizations else "Unknown",
            # # Get the research field of this paper.
            # "Research Fields": "; ".join(sorted(research_fields)) if research_fields else "Unknown"
        })

    return papers



def save_to_xlsx(data, filename):
    """
    

    Parameters
    ----------
    data : list
        A list of papers and their information.
    filename : str
        The name of the output file.

    Returns
    -------
    None.

    """
    # If there is no data.
    if not data:
        # Print warning message.
        print("No data to write.")
        return
    # Create an Excel workbook.
    workbook = xlsxwriter.Workbook(filename)
    # Add a worksheet.
    worksheet = workbook.add_worksheet()
    # Get the headers from the first dictionary.
    headers = list(data[0].keys())
    # Write the header row.
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)
    # Write the data rows.
    for row_num, entry in enumerate(data, start=1):
        for col_num, key in enumerate(headers):
            worksheet.write(row_num, col_num, entry.get(key))
    # Close the workbook.
    workbook.close()
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
    papers.sort(key=lambda x: int(x["Year"]) if x["Year"].isdigit() else 0, reverse=True)
    save_to_xlsx(papers, filepath+'.xlsx')
    write_a_memo()


if __name__ == '__main__':
    main()
