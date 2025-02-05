import csv
from typing import List, Dict

def save_to_csv(papers: List[Dict[str, str]], filename: str):
    """
    Saves the list of papers to a CSV file.
    """
    if not papers:
        raise ValueError("No papers to save.")
    
    keys = papers[0].keys()  # Get field names from the first paper (headers)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(papers)
