# Elasticsearch

Master: [![Build Status](https://travis-ci.org/sansible/elasticsearch.svg?branch=master)](https://travis-ci.org/sansible/elasticsearch)  
Develop: [![Build Status](https://travis-ci.org/sansible/elasticsearch.svg?branch=develop)](https://travis-ci.org/sansible/elasticsearch)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Elasticsearch.
The default version is 2.4.1.

For more information on Elasticsearch please visit [elastic elasticsearch](https://www.elastic.co/products/elasticsearch).




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

To install run `ansible-galaxy install sansible.elasticsearch` or add this to your
`roles.yml` and `sansible.java` for installing java.

```YAML
- name: sansible.elasticsearch
  version: v1.2
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
  hosts: "somehost"

  roles:
    - role: sansible.elasticsearch
```

To install v5 with x-pack:

```YAML
- name: Install and configure ElasticSearch
  hosts: "somehost"

  roles:
    - role: sansible.elasticsearch
      elasticsearch:
        version: 5.0.0
        family: 5.x
        plugins:
          - plugin_name: x-pack
            plugin_dir: x-pack
```

With AWS EC2 plugin:

```YAML
- name: Install and configure ElasticSearch
  hosts: "somehost"

  roles:
    - role: sansible.elasticsearch
      elasticsearch:
        config:
          bootstrap.mlockall: "true"
          index.number_of_shards: 6
          index.number_of_replicas: 2
          discovery.zen.ping.multicast.enabled: "false"
          script.disable_dynamic: "true"
          cloud.aws.region: "true"
          cloud.node.auto_attributes: "true"
          discovery.type: ec2
          discovery.ec2.ping_timeout: "30s"
          discovery.ec2.tag.Stack: services-dev-elasticsearch-v2
        plugins:
          - plugin_name: mobz/elasticsearch-head
            plugin_dir:  head
          - plugin_name: royrusso/elasticsearch-HQ
            plugin_dir:  HQ
          - plugin_name: cloud-aws
            plugin_dir: cloud-aws
```




## Test

To run the test locally, run `make test`. This requires `ansible-lint` to be present. You can install `ansible-lint` with `pip install ansible-lint`.
You may consider using a virtual python environment (i.e. use `virtualenv`). Review the `Makefile` to discover the other related `make` commands.
