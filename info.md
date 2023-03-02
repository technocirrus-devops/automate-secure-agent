### curl syntax

`curl -i -X POST -H "Content-Type:application/json" -d "{json data}" url`

### curl cmd to login

`curl -i -X POST -H "Content-Type:application/json" -d "{\"@type\": \"login\",\"username\": \"username\",\"password\": \"password\"}" https://dm-em.informaticacloud.com/ma/api/v2/user/login`

### Headers

- Accept : application/json
- Content-Type : application/json

### JSON Data

`{"@type": "login","username": "username","password": "password"}`

### JSON Data for cmd

`{\"@type\": \"login\",\"username\": \"username\",\"password\": \"password\"}`


## Login URL Syntax

`https://<cloud provider>-<region>.informaticacloud.com/ma/api/v2/user/login`

### Login URL

`https://dm-em.informaticacloud.com/ma/api/v2/user/login`


### Token Generation syntax

{serverUrl}/api/v2/agent/installerInfo/<platform>


### Token generation

**URL :** `https://emw1.dm-em.informaticacloud.com/saas/api/v2/agent/installerInfo/win64` <br>
**Header** icSessionId : 48jHgkzYUmcfqCaAbmB8Wp
