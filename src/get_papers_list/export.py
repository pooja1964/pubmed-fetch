import csv
from typing import List, Dict

def export_to_csv(papers: List[Dict], filename: str):
    """Export filtered research papers to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "PubMed ID",
            "Title",
            "Publication Date",
            "Non-academic Authors",
            "Company Affiliations",
            "Corresponding Author Email"
        ])
        writer.writeheader()

        for paper in papers:
            writer.writerow(paper)
