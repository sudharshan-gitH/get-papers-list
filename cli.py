import argparse
import sys
from .pubmed import fetch_papers, save_to_csv

def create_parser():
    """
    Creates and returns an ArgumentParser instance.

    Returns:
        argparse.ArgumentParser: The argument parser for the CLI.
    """
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers based on a query and filter by author affiliation."
    )
    parser.add_argument(
        'query', 
        type=str, 
        help="Search query for PubMed"
    )
    parser.add_argument(
        '-f', '--file', 
        type=str, 
        help="Filename to save the results as CSV"
    )
    parser.add_argument(
        '-d', '--debug', 
        action='store_true', 
        help="Enable debug output"
    )
    return parser

def main():
    """
    Main entry point for the CLI. It fetches papers based on the user's query
    and outputs the results to a file or the console.
    """
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        # Fetch papers based on the user's query
        papers = fetch_papers(args.query, debug=args.debug)
        
        if args.file:
            # Save the results to a CSV file if filename is provided
            save_to_csv(papers, args.file)
            print(f"Results saved to {args.file}")
        else:
            # Otherwise, print the results to the console
            for paper in papers:
                print(f"Title: {paper['Title']}, PubMed ID: {paper['PubmedID']}")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
