# Logstash Sender

This repo setup elasticsearch, kibana and logstash. The message guy file will send a example message to logtash by a socket tcp connection and logstash will process an output to elasticsearch. 

ELK stack requires java. Oracle JDK is recommended, so:

``` 
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer
$ java -version
  java version "1.8.0_151"
  Java(TM) SE Runtime Environment (build 1.8.0_151-b12)
  Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)
```

Configure the environment variable $JAVA_HOME:
```
$ sudo vim /etc/environment
```

Add this to the end of the file and save: JAVA_HOME="/usr/lib/jvm/java-8-oracle"

```$ echo $JAVA_HOME
  /usr/lib/jvm/java-8-oracle
```

### Installing Elasticsearch

if something got wrong, go to  official site: https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

```
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install elasticsearch
```

# configurting elastisearch:

```
$ sudo vim /etc/elasticsearch/elasticsearch.yml
```

Uncomment line 55, and change to: network.host: 0.0.0.0
Uncomment line 59, and change to: http.port: 9200

# running elastisearch

``` $ sudo systemctl start elasticsearch.service ```

Go to http://localhost:9200/, you should get this:

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

### Installing kibana

if something got wrong, go to the official website: https://www.elastic.co/guide/en/kibana/current/deb.html

```
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install kibana
```

# Running kibana:

```$ sudo systemctl start kibana.service```

Go to http://localhost:5601, you should get home page of kibana

# Installing Logstash

if something got wrong, go to official website https://www.elastic.co/guide/en/logstash/current/installing-logstash.html
```
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install logstash
```

### Configuring logstash

logstash is a bridge between our applications and elasticsearch. Before running logstash, we need to configure how the input will works (how our apps will communcate with logstash, by a tcp socket, for example) and where would be the output, a instance of elasticsearch.

```
$ cd /etc/logstash/conf.d
$ sudo vim base.conf
```
 
Put this on the file:

```
input {
        tcp {
                port => 9201
                codec => json
        }
}
output {
        elasticsearch {
                hosts => "http://0.0.0.0:9200"
        }
}
```

```$ sudo vim /etc/logstash/logstash.yml```

Uncommentline 190, and change to: ```http.host: 0.0.0.0```
Uncomment 207, and change to: ```log.level: debug```

```$ sudo systemctl start logstash.service ```

Now, run the message_guy.py file, this will send a message error to logstash
```$ python message_guy.py```

If you want to watch logstash logs in real time, open a terminal and:
```$ tail -f /var/log/logstash/logstash-plain.log```

When you run the message_guy.py, you sould see this at logstash-plain.log:
```
[2017-12-20T21:20:04,431][DEBUG][logstash.pipeline        ] filter received {"event"=>{"host"=>"localhost", "port"=>50406, "@metdata"=>{"ip_address"=>"127.0.0.1"}, "@tags"=>["test"], "@message"=>"python test message", "@timestamp"=>2017-12-20T23:20:04.420Z, "@version"=>"1"}}
[2017-12-20T21:20:04,433][DEBUG][logstash.pipeline        ] output received {"event"=>{"host"=>"localhost", "port"=>50406, "@metdata"=>{"ip_address"=>"127.0.0.1"}, "@tags"=>["test"], "@message"=>"python test message", "@timestamp"=>2017-12-20T23:20:04.420Z, "@version"=>"1"}}
```

Now just go to kibana, go to management page and create a logstash-* index pattern. Go to discover page, you should see a beaultiful and cool error messsage! :)








