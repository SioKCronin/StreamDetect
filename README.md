# sift

### Objective
Provide a clean, scalable architecture for real-time search on streaming text data.

### Business case
Companies like Wikipedia, Twitter, Reddit, and Youtube are providers of entertaining and stimulating content, 
yet are also hotbeds for heated community disputes. These companies require systems to flag early signs of abuse 
and bullying, so that conflicts can be curbed. Sift provides a clean, scalable architecture for real-time detection 
of trigger words on streaming text data.

### Goals
* Achieve near real-time search of a streaming text data source. 
* Explore stream architecture and optimization. 

### Project contents

#### Setup
* includes Boto3 for automated AWS cluster deployment (S3 and EC2)

#### Pipeline
* S3 (Wikipedia article updates since 2008)
* Solr-Lucene & Spark (search stream of article recent changes for hot words)
* Redis (record incidents of hot word use along with usr_id and article_id)
* Dash (display hot word analytics)

### Data

#### About
* 31 million registered users, although only 119K active users (at least 1 edit/month)
* 3TB of change log data since 2008
* 10-20 changes/second from the RCFeed (can speed up using the historical data for velocity)
* 29 million pages (reduce to 10 million that are in the encyclopedia, and 4.2 million are articles, stubs and 
disambiguation pages) 

#### Downloads
* All data from inception to 2008: https://snap.stanford.edu/data/wiki-meta.html
* Latest dump: https://dumps.wikimedia.org/enwiki/latest/

#### Fields
* REVISION article_id rev_id article_title timestamp [ip:]username user_id
* CATEGORY list of categories
* IMAGE list of images (each listed as many times as it occurs)
* MAIN through OTHER cross-references to pages in other namespaces
* EXTERNAL hyperlinks to pages outside Wikipedia
* TEMPLATE list of all templates (each listed as many times as it occurs)
* COMMENT contains the comments as entered by the author
* MINOR whether the edit was marked as minor by the author
* TEXTDATA word count of revision's plain text
