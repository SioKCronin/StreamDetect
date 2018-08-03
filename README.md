# sift

### Overview
Sift provides a clean, scalable architecture for real-time search on streaming text data. Implementing realtime search can 
provide companies with the ability to monitor high velocity text feeds, with applications ranging from media
monitoring to anti-vandelism/abuse detection.

Achieving near real-time search in high volume streaming text data. For example, when we implement document search in a 
static setting we typically create an index, which is often not feasible in high velocity streams. This has led developers
to explore reverse search strategies where queries are indexed and matched against a tokenized document field. Challenges
emerge as additional processing is added beyond identifying matches, as well as handling complex queries. 

### Architecture
* **AWS (S3)**: Data
* **Flask**: Frontend
* **Kakfa Streams**: Scalable, fault-tolerant, low-latency streaming
* **Elasticsearch-Lucene**: Text indexing (Percolator queries) and tokenization

### Development technology
* Boto3 (AWS cluster provisioning and deployment)
* Great Expectations (pipeline testing)

#### Wikipedia revision logs
* 31 million registered users, although only about 119K active users making at least 1 edit/month
* 3TB of revision log data (XML)
* 10-20 changes/second from the RCFeed (can speed up using the historical data for velocity)
* 29 million pages (reduce to 10 million that are in the encyclopedia, and 4.2 million are articles, stubs and 
disambiguation pages) 

#### Data
* All data from inception to 2008: https://snap.stanford.edu/data/wiki-meta.html
* Archived data: https://dumps.wikimedia.org/enwiki/latest/

#### Specs/Constraints
* Presently sift can return match results at a rate of 0 records/second (room for improvement!)
