# a django login app 

### 根urls.py 添加
```python
url(r'^account/',include('login.urls')),
```

### setting.py 添加
```python
INSTALLED_APPS = [
    ...
    'login',
]

...

TEMPLATES = [
    {
        ...
        'DIRS': [
                ...
                BASE_DIR+'/login/templates',
                ],
        ...
    },
]

```

url格式 
* /account/login
* /account/logout
* /account/register
* /account/info

user表
id | username | password | email | ...
-- | -------- | -------- | ----- | ---

