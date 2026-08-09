# Python Jobs Web Scraper

A Python web scraping project that collects job listings from the Python.org Jobs website, extracts detailed job information, and exports the results to a CSV file.

## Features

- Scrape job listings from multiple pages
- Extract job title, company, location, and category
- Visit each job page to collect additional details
- Extract job description, company information, and requirements
- Handle missing company information
- Retry failed HTTP requests
- Export collected data to CSV
- Use a persistent `requests.Session` for HTTP requests

## Data Collected

The scraper collects the following information:

- Job Name
- Company Name
- Location
- Category
- Job Link
- Job Description
- About the Company
- Requirements

## Technologies

- Python
- Requests
- BeautifulSoup
- lxml
- CSV
- Pathlib

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