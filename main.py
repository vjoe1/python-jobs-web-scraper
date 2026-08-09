from scrapper import *

def main():
    page = 1

    all_jobs = []
    while True :
        url   = f"{BASE_URL}/jobs/?page={page}" # the web which i will scrab from
        soup = fetch_page(url)
        if soup is None:
            print(f"Failed to fetch page {page}")
            break
        
        jobs = scrape_jobs(soup)
        all_jobs.extend(jobs)

        if soup.find("a", class_ = "disabled" , string = "Next") :
            break

        page += 1
    save_to_csv(all_jobs , "python_jobs")


if __name__ == "__main__":
    main()