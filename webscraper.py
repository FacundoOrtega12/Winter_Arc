import urllib.request
import re
from bs4 import BeautifulSoup

# URL of the web page to fetch
url = 'https://www.linkedin.com/jobs/search/?currentJobId=4011191575&distance=25&geoId=103918656&keywords=biotechnology&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true'

try:
    # Open the URL and read its content
    response = urllib.request.urlopen(url)
    
    # Read the content of the response
    data = response.read()
    
    # Decode the data (if it's in bytes) to a string
    html_content = data.decode('utf-8')

    #remove HTML tags from page to clean it up :)
    CLEANR = re.compile('<.*?>')
    clean_html_content = re.sub(CLEANR, '', html_content) 
    more_clean = clean_html_content.split()
    test_clean = html_content.split()
    f = open("test.html", "w")  #THOUGHTS - need to store it as a base html file with no edits made to it that way hopefully it will search propery
                                # or find a way I can use BS to search the text file
    for word in test_clean:
        for char in word:
            f.write(char)
    f.close()

    # Print the HTML content of the web page

    # Using BS we can pull out the html elements we want. Then we can make a Dic of link and time posted (idk if we need the time but want to factor it in search)
    # use this list or dic of links to then serach through those for our jobs
    with open("test.html") as m:
        soup = BeautifulSoup(m.read(), 'html.parser')
    soupy_txt = soup.find_all("div", class_= "job-search-card__listdate")
    print("HERE", soupy_txt)
    
except Exception as e:
    print("Error fetching URL:", e)