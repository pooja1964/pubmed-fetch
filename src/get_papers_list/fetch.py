import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_papers(query: str) -> List[Dict]:
    """Fetch research papers from PubMed based on the query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10,  # Fetch 10 papers for now
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])

    papers = []
    for pubmed_id in paper_ids:
        details_params = {
            "db": "pubmed",
            "id": pubmed_id,
            "retmode": "xml",
        }
        details_response = requests.get(DETAILS_URL, params=details_params)
        details_response.raise_for_status()

        paper_info = parse_paper_details(pubmed_id, details_response.text)
        if paper_info:
            papers.append(paper_info)

    return papers

def parse_paper_details(pubmed_id: str, xml_data: str) -> Dict:
    """Extract necessary details from PubMed XML response."""
    root = ET.fromstring(xml_data)
    
    title = root.find(".//ArticleTitle")
    title_text = title.text if title is not None else "N/A"

    pub_date = root.find(".//PubDate/Year")
    pub_date_text = pub_date.text if pub_date is not None else "Unknown"

    authors = []
    non_academic_authors = []
    company_affiliations = []
    corresponding_email = "Not Available"

    for author in root.findall(".//Author"):
        last_name = author.find("LastName")
        first_name = author.find("ForeName")
        affiliation = author.find("AffiliationInfo/Affiliation")

        name = f"{first_name.text if first_name is not None else ''} {last_name.text if last_name is not None else ''}".strip()

        if name:
            authors.append(name)
        
        if affiliation is not None:
            aff_text = affiliation.text
            if is_company_affiliation(aff_text):
                company_affiliations.append(aff_text)
                non_academic_authors.append(name)

        # Find corresponding author email if available
        email = root.find(".//Author/Email")
        if email is not None:
            corresponding_email = email.text

    return {
        "PubMed ID": pubmed_id,
        "Title": title_text,
        "Publication Date": pub_date_text,
        "Non-academic Authors": ", ".join(non_academic_authors) if non_academic_authors else "None",
        "Company Affiliations": ", ".join(company_affiliations) if company_affiliations else "None",
        "Corresponding Author Email": corresponding_email,
    }

def is_company_affiliation(affiliation: str) -> bool:
    """Identify non-academic affiliations (pharma/biotech companies)."""
    company_keywords = ["Pharma", "Biotech", "Inc.", "Ltd.", "Corporation", "Company", "GmbH", "S.A."]
    return any(keyword in affiliation for keyword in company_keywords)
