import requests
import logging

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_papers(query):
    """Fetches papers from PubMed based on a query."""
    logging.info("Fetching data from PubMed API...")
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10,  # Fetch up to 10 papers
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        logging.debug(f"API Response: {data}")  # Debugging API response

        if "esearchresult" not in data or "idlist" not in data["esearchresult"]:
            logging.warning("No papers found.")
            return []

        paper_ids = data["esearchresult"]["idlist"]
        
        # Now fetch details of these papers
        papers = []
        for pubmed_id in paper_ids:
            details_params = {
                "db": "pubmed",
                "id": pubmed_id,
                "retmode": "xml",
            }
            details_response = requests.get(DETAILS_URL, params=details_params, timeout=15)
            details_response.raise_for_status()
            paper_info = details_response.text  # XML response

            # Simulating parsed data for debugging
            paper_data = {
                "PubMed ID": pubmed_id,
                "Title": f"Sample Title {pubmed_id}",
                "Publication Date": "2024-01-01",
                "Non-academic Authors": "Dr. John Doe",
                "Company Affiliation": "XYZ Pharma",
                "Corresponding Author Email": "john.doe@example.com"
            }
            papers.append(paper_data)

        return papers

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []
