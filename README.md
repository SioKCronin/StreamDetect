# StreamDetect

Real-time anomaly detection for streaming data. 

### Business Use Cases
* Fraudelant use

### Pipeline
* S3
* Spark ML (k-means clustering training on batch data)
* Akka (stream processing layer)
* Cassandra (low-latency data store)
* Dash (viz)

### How it works
First we train our anomaly detection model by Spark. The model parameters are then sent to Akka, will process our streaming events
by scoring logs based on the provided model. Cassandra will provide a low-latency data store that will communicate between
Spark and Akka. Spark will create micro-batches to continue training the model. 

### Anomaly Detection references
* [Spark ML](https://databricks.com/session/real-time-anomaly-detection-with-spark-ml-and-akka)
* [Datastream](https://blog.ment.at/datastream-io-open-source-anomaly-detection-64db282735e0) (OSS)
* [AWS Kinesis](https://aws.amazon.com/kinesis/data-analytics/)(anomaly detection): Robust Random Cut Forest-based anomaly detection
* [Scalp](https://code.google.com/archive/p/apache-scalp/) (anomaly detection):  A smaller project, so I'll need to test this.
* [Loglizer](https://github.com/logpai/loglizer) (anomaly detection): Includes PCA and log clustering (unsupervised)
* [Splunk/SumoLogic](https://www.quora.com/Why-would-an-enterprise-choose-Sumo-Logic-over-Splunk)
* [DeepLog](https://www.cs.utah.edu/~lifeifei/papers/deeplog.pdf) (super cool, but a some overhead to implement)
* [devialog](https://sourceforge.net/projects/devialog/)
* [LogReduce](https://blogs.rdoproject.org/2017/11/anomaly-detection-in-ci-logs/)

### Data
* All Wikipedia changes from 2010-Present (3TB of uncompressed data): https://snap.stanford.edu/data/wiki-meta.html
* Eventstream: https://wikitech.wikimedia.org/wiki/EventStreams
* Recent changes feed: https://www.mediawiki.org/wiki/Manual:RCFeed

### Data structure
* RC object: https://www.mediawiki.org/wiki/Manual:Recent_changes
* RC table: https://www.mediawiki.org/wiki/Manual:Recentchanges_table
* Streaming rate of 10-20 events/second. 
* 3+TB of historical data (all updates since 2008)
* How to unszip [this](https://snap.stanford.edu/data/wiki-meta.html) data on S3? https://github.com/carloscarcamo/aws-lambda-unzip-py

### OSS Inspiration
* [Coral](http://coral-streaming.github.io/Overview-Architecture.html)
* [WikiGuardian](https://github.com/kaenyyh/Insight_project_2018b)

### Enterprise projects
* [Fluentd](https://www.fluentd.org/guides/recipes/parse-syslog)
* [Graylog](https://www.graylog.org/overview)
* [Logly](https://www.loggly.com/)

### References
* Detecting attacks of web applications from log files: https://www.sans.org/reading-room/whitepapers/logging/detecting-attacks-web-applications-log-files-2074
* k-means clustering
* decision tree ensembles
