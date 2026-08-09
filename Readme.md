# Python Jobs Web Scraper

A Python web scraper that collects job listings from the [Python.org Jobs](https://www.python.org/jobs/) website, extracts detailed information from each listing, and exports the collected data to a CSV file.

## Features

* Scrape job listings from multiple pages
* Extract job title, company, location, category, and job link
* Visit individual job pages to collect additional details
* Extract job descriptions, company information, and requirements
* Handle missing company information
* Retry failed HTTP requests
* Use a persistent `requests.Session` for HTTP requests
* Export collected data to a CSV file

## Data Collected

The scraper collects the following information:

* Job Name
* Company Name
* Location
* Category
* Job Link
* Job Description
* About the Company
* Requirements

## Technologies

* **Python**
* **Requests** — HTTP requests and session management
* **BeautifulSoup** — HTML parsing and data extraction
* **lxml** — HTML parser
* **CSV** — Data export
* **Pathlib** — File and path handling

## Project Structure

```text
python-jobs-web-scraper/
│
├── constants.py
├── example_python_jobs.csv
├── main.py
├── README.md
├── requirements.txt
└── scraper.py
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vjoe1/python-jobs-web-scraper.git
cd python-jobs-web-scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the scraper

```bash
python main.py
```

The collected job listings will be saved as a CSV file.

## Output

The scraper generates a CSV file containing the collected job listings and their detailed information.

An example output file is included in the repository:

`example_python_jobs.csv`

## Technical Highlights

This project focuses on building a reliable web scraping workflow using Python.

It includes:

* Pagination handling for multiple job listing pages
* Extraction of data from both listing pages and individual job pages
* HTTP error handling and request retries
* A persistent `requests.Session` to efficiently manage HTTP requests
* Structured CSV output for further data analysis

## Future Improvements

Possible future improvements include:

* Add support for additional job websites
* Add more advanced filtering options
* Store scraped data in a database
* Add automated scheduled scraping
* Add logging and monitoring
