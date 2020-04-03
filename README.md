# Elasticsearch

Master: [![Build Status](https://travis-ci.org/sansible/elasticsearch.svg?branch=master)](https://travis-ci.org/sansible/elasticsearch)  
Develop: [![Build Status](https://travis-ci.org/sansible/elasticsearch.svg?branch=develop)](https://travis-ci.org/sansible/elasticsearch)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Elasticsearch.
The default version is 2.4.1.

For more information on Elasticsearch please visit
[elastic elasticsearch](https://www.elastic.co/products/elasticsearch).


## Installation and Dependencies

To install run `ansible-galaxy install sansible.elasticsearch` or add this to your
`roles.yml` and `sansible.java` for installing java.

```YAML
- name: sansible.elasticsearch
  version: v2.2.x
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Elasticsearch and all it's dependencies.
* `configure` - Configure and ensures that the Elasticsearch service is running.


## Examples

To install default version with default settings:

```YAML
- name: Install and configure ElasticSearch
  hosts: somehost

  roles:
    - role: sansible.elasticsearch
```

To install v5 with x-pack:

```YAML
- name: Install and configure ElasticSearch
  hosts: somehost

  roles:
    - role: sansible.elasticsearch
      sansible_elasticsearch_family: 5.x
      sansible_elasticsearch_plugins:
        - plugin_name: x-pack
          plugin_dir: x-pack
      sansible_elasticsearch_version: 5.0.0
```

With the AWS EC2 plugin:

```YAML
- name: Install and configure ElasticSearch
  hosts: somehost

  roles:
    - role: sansible.elasticsearch
      sansible_elasticsearch_additional_config:
        bootstrap.mlockall: yes
        index.number_of_shards: 6
        index.number_of_replicas: 2
        discovery.zen.ping.multicast.enabled: no
        script.disable_dynamic: yes
        cloud.aws.region: yes
        cloud.node.auto_attributes: yes
        discovery.type: ec2
        discovery.ec2.ping_timeout: 30s
        discovery.ec2.tag.Stack: services-dev-elasticsearch-v2
      sansible_elasticsearch_plugins:
        - plugin_name: mobz/elasticsearch-head
          plugin_dir:  head
        - plugin_name: cloud-aws
          plugin_dir: cloud-aws
```
