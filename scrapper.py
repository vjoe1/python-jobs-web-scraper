import csv
from bs4 import BeautifulSoup
import requests
from pathlib import Path    
from constants import HEADERS , BASE_URL

session = requests.Session()


def fetch_page(url : str ) -> BeautifulSoup | None:
        for _ in range(3) :
            try :
                response = session.get(url , headers=HEADERS , timeout= 10)
                response.raise_for_status()
                return BeautifulSoup(response.text , "lxml") 
            except requests.RequestException:
                continue
        return None



def scrape_jobs (soup : BeautifulSoup ) -> list:
    """ A function to scrap the job card and ( name , location , category)"""
    job_cards = soup.select("ol.list-recent-jobs li") # to extract the card
    
    jobs = []
    for job in job_cards :  # to loop over the job card
     
        job_name = job.find("a").get_text(strip=True) 

        
        company_name =job.find("span" , class_ = "listing-company-name").contents[-1].strip()

        # the company name is the last part of card

        location = job.find("span"  , class_ = "listing-location").get_text(strip=True)

        category = job.find("span" , class_ = "listing-company-category").get_text(strip=True)

        job_link = job.find("a").get("href")
        # getting the link to request it and scrap the details

        details = scrape_job_details(job_link)

        jobs.append(
        { "job_name": job_name,
            "company_name": company_name,
            "location": location,
            "category": category,
            "job_link": job_link,
            "description": details["description"],
            "about_company": details["about_company"],
            "requirements": details["requirements"], })

    return jobs



def scrape_job_details(link : str) -> dict:
    """a function to scrap the job details from its link , including the description , about , requirement"""
    soup = fetch_page(f"{BASE_URL}{link}") 
    if soup is None:
        return {
            "description": "",
            "about_company": "",
            "requirements": []
        }

    job_description = soup.find("div"  , class_ = "job-description").find("p").get_text(strip=True)

    about_the_company = ""    
    try :
        about_the_company = soup.find("h2" , string = "About the Company" ).find_next_sibling("p").get_text(strip=True)

    except AttributeError:
        about_the_company = ""    



    job_req = soup.find("div"  , class_ = "job-description").find("h2" , string = "Requirements" )
    requirement_list = []
    if job_req :

        for one_job_req in job_req.find_next_siblings() :

            if one_job_req.name == "h2" :
                break

            elif one_job_req.name == "ul" :
                for li in one_job_req.find_all("li") :
                 requirement_list.append(li.get_text(" ", strip=True) + "  ")

            elif one_job_req.name == "p" :
                requirement_list.append(one_job_req.get_text(" ", strip=True) + " ")

    return {
    "description": job_description,
    "about_company": about_the_company,
    "requirements": requirement_list }



def save_to_csv(jobs: list , filename : str ) -> None:

    if not jobs :
        print("No jobs found")
        return
    
    keys = jobs[0].keys()

    file_path = Path(__file__).parent / f"{filename}.csv"
    with open(file_path, "w" , encoding="utf-8", newline="") as output :
        writer = csv.DictWriter(output, keys)
        writer.writeheader()
        writer.writerows(jobs)
        print(f"File created : {file_path}")       

