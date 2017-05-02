# vcf-miner.client
Python client for VCF-Miner

## How to get started
Go to a directory of you choice and clone this repository:
```
git clone https://github.com/ratzeni/vcf-miner.client.git
cd vcf-miner.client
```

Install vcf-miner.client
```
python setup.py install
```

## Examples
###Connection
```python
from vcfminerclient import VCFMinerClient
from alta.utils import a_logger, LOG_LEVELS

logger = a_logger('main',level='INFO')
conf=dict(host='http://localhost:8888',
          username='Admin',
          password='temppass',
          appkey='VcfMiner')

client = VCFMinerClient(conf=conf, logger=logger)
```
```text
2017-04-28 12:35:16|INFO    |main |Connecting to http://localhost:8888 
2017-04-28 12:35:22|INFO    |main |User Admin is authenticated
```
### Show Auth Details
```python
result = client.get_authentication()
```
```python
{'errors': None,
 'result': {u'isAuthenticated': True,
            u'userToken': u'7c2f7227-1cfe-4815-90da-70dfa2fb6ca7:ea428c44-2f3d-4e07-9d68-b5ddadeef538'
            },
 'success': True,
 'warnings': None}
```
### List Users
```python
result = client.get_users()
```
```python
{'errors': None,
 'result': [{u'created': u'2014-05-30T21:19:03.000+0000',
   u'email': u'',
   u'employeeId': u'',
   u'id': 1,
   u'isAllowedToLogin': True,
   u'isLdapUser': False,
   u'lastLogin': u'2017-04-28T10:41:35.000+0000',
   u'nameFirst': u'Admin',
   u'nameLast': u'',
   u'passwordHashIfLocal': u'',
   u'passwordSaltIfLocal': u'',
   u'personId': u'',
   u'phone': u'',
   u'racfId': u'',
   u'username': u'Admin'}],
 'success': True,
 'warnings': None}
```
### Create Group
```python
result = client.create_group('myFirstGroup')
```
```python
{'errors': None,
 'result': {u'created': u'2017-04-28T10:50:26.022+0000',
  u'groupName': u'myFirstGroup',
  u'id': 1,
  u'ownerUserId': 1},
 'success': True,
 'warnings': None}
```
### Add User to Group
```python
result = client.add_user_to_group('Admin', 'myFirstGroup')
```
```python
{'errors': None,
 'result': None,
 'success': True,
 'warnings': 'No JSON object could be decoded'}
```
### List Groups (for user)
```python
result = client.get_groups(username='Admin')
```
```python
{'errors': None,
 'result': [{u'created': u'2017-04-28T10:50:26.000+0000',
   u'groupName': u'myFirstGroup',
   u'id': 1,
   u'ownerUserId': 1}],
 'success': True,
 'warnings': None}
```
### List Users in Group 
```python
result = client.get_users_in_group('myFirstGroup')
```
```python
{'errors': None,
 'result': [{u'created': u'2014-05-30T21:19:03.000+0000',
   u'email': u'',
   u'employeeId': u'',
   u'id': 1,
   u'isAllowedToLogin': True,
   u'isLdapUser': False,
   u'lastLogin': u'2017-04-28T10:41:35.000+0000',
   u'nameFirst': u'Admin',
   u'nameLast': u'',
   u'passwordHashIfLocal': u'',
   u'passwordSaltIfLocal': u'',
   u'personId': u'',
   u'phone': u'',
   u'racfId': u'',
   u'username': u'Admin'}],
 'success': True,
 'warnings': None}
```
### Upload VCF
```python
result = client.upload_vcf(vcfpath='/my/vcf/path/some.genotypes.vcf', vcfname='my_vcf')
```
```python
{'errors': None,
 'result': 'File uploaded and workspace constructed : { "owner" : "Admin" , "alias" : "my_vcf" , "ready" : 1 , "_id" :  { "$oid" : "59033ffbe4b0d97b915db706"} , "key" : "w95aba91216131373b571c1f796ce0f113aa84e95"}',
 'success': True,
 'warnings': 'No JSON object could be decoded'}
```
### Add VCF to group
```python
result = client.add_vcf_to_group('my_vcf', groupname='myFirstGroup')
```
```python
{'errors': None,
 'result': '',
 'success': True,
 'warnings': 'No JSON object could be decoded'}
```
### List VCF in Group
```python
result = client.get_vcf_for_group('myFirstGroup')
```
```python
{'errors': None,
 'result': [{u'description': u'user=Admin,name=my_vcf,date=Fri Apr 28 13:13:31 UTC 2017',
   u'id': 1,
   u'key': u'w95aba91216131373b571c1f796ce0f113aa84e95',
   u'ownerUserId': 1,
   u'type': u'WKS'}],
 'success': True,
 'warnings': None}
```
### Add VCF to User
```python
result = client.add_vcf_to_user('my_vcf', username='Admin')
```
```python
{'errors': None,
 'result': None,
 'success': True,
 'warnings': "VCF 'my_vcf already in User 'Admin'"}
```
### List VCF in User
```python
result = client.get_vcf_for_user(username="Admin")
```
```python
{'errors': None,
 'result': [{u'description': u'user=Admin,name=my_vcf,date=Tue May 02 10:32:53 UTC 2017',
   u'id': 1,
   u'key': u'w5fbd4e0de94b9d4aefc9799a9c042aaec8065bf7',
   u'ownerUserId': 1,
   u'type': u'WKS'}],
 'success': True,
 'warnings': None}
```
### Delete VCF
```python
result = client.delete_vcf(vcfname='my_vcf')
```
```python
{'errors': None,
 'result': {u'status': u'workspace= w5fbd4e0de94b9d4aefc9799a9c042aaec8065bf7 deleted'},
 'success': True,
 'warnings': None}
```
### Remove User from Group
```python
result = client.remove_user_from_group(username='Admin', groupname='myFirstGroup')
```
```python
{'errors': None,
 'result': None,
 'success': True,
 'warnings': 'No JSON object could be decoded'}
```
### Delete Group
```python
result = client.delete_group(groupname='myFirstGroup')
```
```python
{'errors': None,
 'result': None,
 'success': True,
 'warnings': 'No JSON object could be decoded'}
```