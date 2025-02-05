import requests
import csv
from typing import List, Dict, Optional

def fetch_papers(query: str, debug: bool = False) -> List[Dict[str, str]]:
    """
    Fetches a list of papers from PubMed based on the given query.

    Args:
        query (str): The search query for PubMed.
        debug (bool): Enable debug output if True.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing paper details.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",  # We are querying PubMed.
        "term": query,   # The search term.
        "retmode": "xml", # Format to return data as XML.
        "retmax": "100",  # Limit the number of results returned.
    }
    
    if debug:
        print(f"Fetching papers with query: {query}")
    
    response = requests.get(base_url, params=params)
    
    # Handle HTTP errors
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data: {response.status_code}")
    
    # Parse the XML response and extract paper details
    papers = parse_papers(response.text)
    
    return papers

def parse_papers(xml_data: str) -> List[Dict[str, str]]:
    """
    Parses the XML data from PubMed and extracts the required details.

    Args:
        xml_data (str): The XML response data from PubMed.

    Returns:
        List[Dict[str, str]]: A list of paper details (ID, title, etc.).
    """
    # In a real application, you would parse XML here. For now, let's assume the response
    # gives us the paper data directly. This is where you will handle PubMed's XML response.
    
    # Example output:
    return [
        {
            "PubmedID": "12345678",
            "Title": "Sample Paper Title",
            "Publication Date": "2023-01-01",
            "Non-academic Author(s)": "Dr. John Doe",
            "Company Aﬃliation(s)": "Acme Pharma",
            "Corresponding Author Email": "john.doe@example.com"
        }
    ]
    
def save_to_csv(papers: List[Dict[str, str]], filename: str):
    """
    Saves the list of papers to a CSV file.

    Args:
        papers (List[Dict[str, str]]): The list of papers to save.
        filename (str): The name of the CSV file.
    """
    # Writing the data to a CSV file
    keys = papers[0].keys()  # Get the fieldnames (keys of the first paper)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(papers)
