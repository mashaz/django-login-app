# a django login app 

### urls.py 添加
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
