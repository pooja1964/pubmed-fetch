import argparse
import logging
from get_papers_list.fetch import fetch_papers
from get_papers_list.export import export_to_csv

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Fetch PubMed research papers and filter for non-academic authors."
    )
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file (default: print to console)", default="")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    # Parse command-line arguments
    args = parser.parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

    logging.info(f"Fetching papers for query: {args.query}")
    
    # Fetch papers
    papers = fetch_papers(args.query)

    if args.debug:
        logging.debug(f"Fetched {len(papers)} papers from PubMed.")

    # Export or print results
    if args.file:
        export_to_csv(papers, args.file)
        logging.info(f"Results saved to {args.file}")
    else:
        print("Results:")
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
