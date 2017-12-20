# sending_errors_to_logstash
Send your log erros to logstash and enjoy the power of ELK stack

ELK stack requires java. Oracle JDK is recommended, so:

$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer
$ java -version
  java version "1.8.0_151"
  Java(TM) SE Runtime Environment (build 1.8.0_151-b12)
  Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)


we need to configure the environment variable $JAVA_HOME:
$ sudo vim /etc/environment

Add this to the end of the file and save:
JAVA_HOME="/usr/lib/jvm/java-8-oracle"

$ echo $JAVA_HOME

should return: /usr/lib/jvm/java-8-oracle

Installing Elasticsearch

if some got wrong, check instructions on official site: https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install elasticsearch

running elastisearch

go to the browser on http://localhost:9200/, you shold get this:

```
{
  "name" : "WyRpAjH",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "UV_urK1SRkuhU910f52CIg",
  "version" : {
    "number" : "6.1.1",
    "build_hash" : "bd92e7f",
    "build_date" : "2017-12-17T20:23:25.338Z",
    "build_snapshot" : false,
    "lucene_version" : "7.1.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

congrats, elastisearch is installed

Installing kibana

$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install kibana

Running kibana:
$ sudo systemctl start kibana.service

With you browser, go to http://localhost:5601, you shold get home page of kibana


