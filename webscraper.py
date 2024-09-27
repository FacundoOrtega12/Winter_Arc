import urllib.request
import re
from bs4 import BeautifulSoup

def main():
    # URL of the web page to fetch
    url = 'https://www.linkedin.com/jobs/search/?currentJobId=4007877353&distance=25&geoId=103918656&keywords=Oligonucleotides&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true'
    try:
        # Open the URL and read its content
        response = urllib.request.urlopen(url)
        
        # Read the content of the response
        data = response.read()
        
        # Decode the data (if it's in bytes) to a string
        html_content = data.decode('utf-8')
    except Exception as e:
        print("Error fetching URL:", e)
    
    #creates the HTML data from the content of the page using a html parser
    soup = BeautifulSoup(html_content, 'html.parser')

    get_times(soup)
    get_details(soup)
    get_links(soup)
    get_tags(soup)

def get_times(soup):
        time_posted_list = soup.find_all("time")
        # Creating times file to further clean it up
        t = open("times.txt", "w")
        for time in time_posted_list:
            time = str(time)
            time.split()
            t.write(time)
        t.close()

        #cleans up the output in another text file
        with open( 
            "times.txt", 'r') as r, open( 
                'times_clean.txt', 'w') as o: 
            
            for line in r: 
                if line.strip(): 
                    o.write(line) 

        f = open("times_clean.txt", "r")
        f.close()
        print("IN TIMES")
        
def get_details(soup):   
        #this will give basic info on the jobs - location and title - location can be used to filter out results
        job_details_list = soup.find_all("span", "job-search-card__location")
        
        d = open("details.txt", "w")
        for job in job_details_list:
            job = str(job)
            job.split()
            d.write(job)
        d.close()

        #cleans up the output in another text file
        with open( 
            "details.txt", 'r') as r, open( 
                'details_clean.txt', 'w') as o: 
            
            for line in r: 
                if line.strip(): 
                    o.write(line) 

        f = open("details_clean.txt", "r")
        f.close()
        print("IN DEETS")

def get_links(soup):
        #this gives the links of the jobs posted
        job_links_list = soup.find_all(href=re.compile("/jobs/")) 
        
        l = open("links.txt", "w")
        for link in job_links_list:
            link = str(link['href'])
            l.write('\n')
            l.write(link)
        l.close()

        #cleans up the output in another text file
        with open( 
            "links.txt", 'r') as r, open( 
                'links_clean.txt', 'w') as o: 
            
            for line in r: 
                if line.strip(): 
                    o.write(line) 

        f = open("times_clean.txt", "r")
        f.close()
        print("IN LINKS")

def get_tags(soup):
    tags_list = soup.find_all(True)
    # Creating times file to further clean it up
    t = open("tags.txt", "w")
    for tag in tags_list:
        tag = str(tag)
        tag.split()
        t.write(tag)
    t.close()

if __name__ == "__main__":
     main()
