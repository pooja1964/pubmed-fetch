import csv
import logging

logging.basicConfig(level=logging.INFO)

def export_to_csv(papers, filename):
    """Exports a list of papers to a CSV file."""
    if not papers:
        logging.warning("No papers to export.")
        return

    logging.debug(f"Exporting the following papers: {papers}")

    fieldnames = ["PubMed ID", "Title", "Publication Date", "Non-academic Authors", "Company Affiliation", "Corresponding Author Email"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for paper in papers:
                if isinstance(paper, dict):
                    writer.writerow(paper)
                else:
                    logging.warning(f"Skipping invalid entry: {paper}")

        logging.info(f"Successfully saved {len(papers)} papers to {filename}")

    except Exception as e:
        logging.error(f"Error writing to CSV: {e}")
