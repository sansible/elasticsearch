import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users(host):
    assert host.user('elasticsearch').group == 'elasticsearch'


def test_listening(host):
    assert host.socket('tcp://127.0.0.1:9200').is_listening


def test_elasticsearch(host):
    es = host.process.get(user='elastic+', comm='java')
    es_limits = host.file('/proc/%i/limits' % es.pid).content_string
    assert re.search(r'Max open files\s+65535\s+65535\s+', es_limits)
