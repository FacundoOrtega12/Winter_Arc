import urllib.request
import re
from bs4 import BeautifulSoup

# URL of the web page to fetch
url = 'https://www.linkedin.com/jobs/search/?currentJobId=4007877353&distance=25&geoId=103918656&keywords=Oligonucleotides&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true'
try:
    # Open the URL and read its content
    response = urllib.request.urlopen(url)
    
    # Read the content of the response
    data = response.read()
    
    # Decode the data (if it's in bytes) to a string
    html_content = data.decode('utf-8')

    #remove HTML tags from page to clean it up :)
    
    # CLEANR = re.compile('<.*?>')
    # clean_html_content = re.sub(CLEANR, '', html_content) 
    # more_clean = clean_html_content.split()
    # test_clean = html_content.split()
    # f = open("test.txt", "w")  
    # for word in test_clean:
    #     for char in word:
    #         f.write(char)
    # f.close()
   
   #Looks through the HTML decoded from the webpage for desired things only times posted right now but want to get link of job amd time
    soup = BeautifulSoup(html_content, 'html.parser')
    time_posted_list = soup.find_all("time")
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

     
except Exception as e:
    print("Error fetching URL:", e)