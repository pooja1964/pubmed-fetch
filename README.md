# pubmed-fetch
# 📄 get-papers-list  

**get-papers-list** is a command-line tool to fetch research papers from **PubMed** based on a given search query. It filters for authors affiliated with pharmaceutical or biotech companies and exports the results into a **CSV file**.

## 🚀 Features  
- Fetches research papers from **PubMed** using Entrez API.  
- Extracts **PubMed ID, Title, Publication Date, Non-academic Authors, Company Affiliation, and Corresponding Author Email**.  
- Saves results as a CSV file for easy reference.  
- Supports **command-line arguments** for flexible usage.  
- Uses **Poetry** for dependency management.  

## 🛠️ Installation  
Install Dependencies using Poetry
pip install poetry
Then, install dependencies:
poetry install

Usage
Run the script from the terminal:
poetry run python cli.py "your search query" -f output.csv

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/your-username/get-papers-list.git
cd get-papers-list


This contains everything:
✔ **Installation**  
✔ **Usage**  
✔ **CLI Arguments**  
✔ **Project Structure**  
✔ **Full Code for cli.py, fetch.py, and export.py**  
✔ **Error Handling & Contribution Guidelines**  

Now, just **copy and paste** it into your `README.md` and you're good to go! 🚀
