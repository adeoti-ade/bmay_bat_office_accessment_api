## Part 3 - Questions

* As mentioned in the context section, the final aim of metadata ingestion is to create a SingleView. What could be doone if two files provide conflicting information on the same work?
    - Nothing may be done. Unless there is evidence that one of the files contains the most accurate information about the work, the two information must be kept

* Could you use the endpoints described in this assignment or would have to create some new endpoints to provide the works of the SingleView?
    - yes, the endpoints described already capture all the information available for the works. Except new information comes in which may require news access to it, the availabe endpoints is good enough

* Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time? What technologies would you use to keep response times reasonable?
    - No, the response time would have been affected and increase significantly. Below are the techologies that may be used to keep response time reasonabl
        * indexing of the query parameter. (i.e; source)
        * caching the data to limit request to database
        * get a strronger cpu for database
        * increase memory