import requests
from typing import List, Dict

# This function fetches papers from PubMed based on the user's query
def fetch_papers(query: str, debug: bool = False) -> List[Dict[str, str]]:
    """
    Fetches research papers from PubMed using the given query.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",  # PubMed database
        "term": query,   # Search term
        "retmode": "xml",  # Response format
        "retmax": "100",  # Max results returned
    }
    
    if debug:
        print(f"Fetching papers for query: {query}")
    
    response = requests.get(base_url, params=params)

    # Handle potential HTTP errors
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data: {response.status_code}")

    # Parse the XML response from PubMed
    papers = parse_papers(response.text)
    return papers


def parse_papers(xml_data: str) -> List[Dict[str, str]]:
    """
    Parse the XML data from PubMed and extract the paper details.
    For simplicity, this is a mock function.
    In a real-world case, you'd parse the XML using an XML parser.
    """
    # In reality, you'd use an XML library to extract the fields from the PubMed XML response
    # This is just a mock data structure as an example
    return [
        {
            "PubmedID": "12345678",
            "Title": "Cancer Research in Biotech",
            "Publication Date": "2023-01-01",
            "Non-academic Author(s)": "John Doe, Jane Smith",
            "Company Affiliation(s)": "PharmaCorp, BioTech Ltd.",
            "Corresponding Author Email": "johndoe@pharmacorp.com"
        },
        {
            "PubmedID": "87654321",
            "Title": "Genomic Studies in Pharma",
            "Publication Date": "2022-12-01",
            "Non-academic Author(s)": "Alice Johnson",
            "Company Affiliation(s)": "PharmaLab",
            "Corresponding Author Email": "alice.j@pharmalab.com"
        }
    ]
