Create a dic to store all found job details(location and title, when job was posted, and job link)
Perform first filter on the dic by looking at when job was posted and only take recently posted jobs
Iterate through filtered dic to look through all the links
perform second filter on the links - filter based on keywords in job description, job requirements and salary ranges 
return a clean dic of desired jobs to apply for



other plans - get working with other jobs sites so you can post multiple site links in a at time and filter all (linkdin, indeed, glassdoor, etc)
maybe make some sore of user interface to add experience

09/24 --- create the other file by looking for the specific classes like the links file (how it has link['href'])
        this will allow creation of the dictionary more 

09/26 --- tried to make the file neater to no avail on the details/times with Bsoup, might need to make cleaner elsewhere. Will make it so just 
        see location. Once cleaned up we can through it into dic for second filter=
                
10/01 --- Can change page number. "&start=25" is page 2 make a for loop iterate through until "No matching jobs found" then end loop and store job urls