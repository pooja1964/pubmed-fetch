import argparse
import logging
from src.get_papers_list.fetch import fetch_papers
from src.get_papers_list.export import export_to_csv

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, default="results.csv", help="Output CSV filename.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    logging.info(f"Fetching papers for query: {args.query}")
    papers = fetch_papers(args.query)

    if not papers:
        logging.warning("No papers found for the given query.")
        return

    logging.debug(f"Fetched papers: {papers}")  # PRINT RESULTS FOR DEBUGGING

    export_to_csv(papers, args.file)
    logging.info(f"Results saved to {args.file}")

if __name__ == "__main__":
    main()
