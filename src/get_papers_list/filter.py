import re
from typing import List, Dict

def filter_company_authors(papers: List[Dict]) -> List[Dict]:
    """Filter papers with at least one author affiliated with a pharmaceutical or biotech company."""
    company_keywords = ["Pharma", "Biotech", "Inc.", "Ltd.", "Corporation"]

    filtered_papers = []
    for paper in papers:
        affiliations = extract_affiliations(paper["details"])
        company_affiliations = [aff for aff in affiliations if any(word in aff for word in company_keywords)]

        if company_affiliations:
            paper["company_affiliations"] = company_affiliations
            filtered_papers.append(paper)

    return filtered_papers

def extract_affiliations(xml_data: str) -> List[str]:
    """Extract author affiliations from XML data."""
    return re.findall(r"<Affiliation>(.*?)</Affiliation>", xml_data)
