import urllib.request
import re

# URL of the web page to fetch
url = 'https://www.linkedin.com/jobs/search/?currentJobId=3998441031&keywords=Biotechnology&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true'


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
    #for word in more_clean:
        #print(word)

    f = open("test.txt", "w")
    f.write(more_clean)
    f.close()

    # Print the HTML content of the web page

except Exception as e:
    print("Error fetching URL:", e)