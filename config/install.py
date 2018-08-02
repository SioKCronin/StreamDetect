# Basic Provisioning
peg up master.yml
peg up workers.yml
peg fetch calvarado-spark-cluster
peg install calvarado-spark-cluster ssh
peg install calvarado-spark-cluster aws
peg install calvarado-spark-cluster hadoop
peg install calvarado-spark-cluster spark
peg ssh calvarado-spark-cluster 1

# Elasticsearch
# https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-targz.html
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.2.tar.gz
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.2.tar.gz.sha512
shasum -a 512 -c elasticsearch-6.3.2.tar.gz.sha512
tar -xzf elasticsearch-6.3.2.tar.gz
cd elasticsearch-6.3.2/

# Lucene
Instructions: https://lucene.apache.org/core/2_9_4/demo.html 
Download: http://www.apache.org/dyn/closer.cgi/lucene/java/

# PyLucene
Requires JDK: https://medium.com/coderscorner/installing-oracle-java-8-in-ubuntu-16-10-845507b13343
JCC: http://lucene.apache.org/pylucene/jcc/install.html

# Setuptools
https://pypi.org/project/setuptools/

