WEBSCRAPER

#While its running read urls as HTML file
    #if words/content we want is in the file store the raw url
        #move on
    #move on

<time
class="job-search-card__listdate"
datetime="2024-03-07">
5
months
ago
</time>


data-entity-urn="urn:li:jobPosting:3848529807"


#search jobs and post link into code 
#this code will draw out jobs based on jobposting and <time> if the time is within a certain period it stores the url from href into a list
#iterate through list of urls and look for keywords inside (qualifications/ salary/ shifts/ etc.)
#store list of urls that have the criteria in it


div><timeclass="job-search-card__listdate--new"datetime="2024-09-18">11hoursago</time><!----></div></div><!----></div></li><li><divclass="base-cardrelativew-fullhover:no-underlinefocus:no-underlinebase-card--linkbase-search-cardbase-search-card--linkjob-search-card"data-entity-urn="urn:li:jobPosting:4027803324"data-impression-id="jobs-search-desktop-14"data-reference-id="8A/w4+ri0RpTvAcgSv08cA=="data-tracking-id="H8zOHIkfVb46K1z+qG832w=="data-column="1"data-row="15"><aclass="base-card__full-linkabsolutetop-0right-0bottom-0left-0p-0z-[2]"href="https://www.linkedin.com/jobs/view/global-training-manager-commercial-excellence-onsite-at-integrated-dna-technologies-4027803324?position=15&amp;pageNum=0&amp;refId=8A%2Fw4%2Bri0RpTvAcgSv08cA%3D%3D&amp;trackingId=H8zOHIkfVb46K1z%2BqG832w%3D%3D&amp;trk=public_jobs_jserp-result_search-card"data-tracking-control-name="public_jobs_jserp-result_search-card"data-tracking-client-ingraphdata-tracking-will-navigate><spanclass="sr-only">GlobalTrainingManager,CommercialExcellence-ONSITE</span></

    job_links_list = soup.find_all("a", class_="base-card__full-linkabsolutetop-0right-0bottom-0left-0p-0z-[2]")
    print(job_links_list)
    for link in job_links_list:
        print(link['href'])