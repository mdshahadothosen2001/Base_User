# Base_User

This project is jwt token authentication system. Provides bearer token for authentication and communication with other projects.

Tech stack: Python, Django, DRF, JWT, Simple-JWT, Docker.


## Local development installation
1. At first pull the repository.


2. Create a virtual environment then activate it.

```bash
py -m venv venv
```
```bash
venv/Scripts/activate.bate
```

3. Install the required packages.

```bash
pip install -r backend/requirements/development.txt
```


4. Run docker containers:

```bash
python manage.py runserver
```

click here [URL](http://localhost:8000)  for check this project working or not
If you see interface page with path detail then it is working.

## See all user APIs
1. GET: http://localhost:8000 api hit for see all user APIs.

## Access token and authentication

If you set email and email-app password in email_host_data then sent otp and recovery password to user email. Otherwise can see at terminal.

1. POST: http://localhost:8000/user/register/ api hit for user account register, use body --> JSON form.
```bash
{
    "phone_number":01.........,
    "email":"....",
    "first_name":"...",
    "last_name":"...."
}
```
2. PATCH: http://localhost:8000/user/activate/ api hit for user account activation, use body --> JSON form.
```bash
    "email":"..",
    "otp":...
```

3. POST: http://localhost:8000/user/token/ api hit for get token, use body --> JSON form
```bash
{
  "phone_number":"01...",
  "password":"..."
}
```

4. POST: http://localhost:8000/user/token/refresh/ api hit for get token, use body --> JSON form
```bash
{
  "refresh":"...."
}
```
5. GET: http://localhost:8000/user/home/ api hit for get token, use Auth -->  placing the token in Bearer Token body
```bash
.....
```

6. PATCH: http://localhost:8000/user/reset/ api hit for change password, use body --> JSON form
```bash
    "new_password":".."
```
7. PATCH: http://localhost:8000/user/forgotten/ api hit for recover password, use body --> JSON form
```bash
    "phone_number":"...",
    "email":".."
```
