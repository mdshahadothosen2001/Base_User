# Base_User

This project is JWT token authentication system service which is obtain access token and refresh token for authentication and communication with other related projects in this distribution services.

Tech stack: Python, Django, DRF, JWT, Simple-JWT, Docker.


## Local development installation
1. Begin with pull the repository.

```bash
git clone https://github.com/mdshahadothosen2001/Base_User.git
```

2. Run docker:

```bash
docker compose up --build
```

> `Remember must full fill dev.env file and if want to send OTP to email must set email and email app password at email_host_data file otherwise print OTP at terminal.`
 

 #
 #
 #
 #
 #
 #
## See all Base_User provides APIs
0. GET method `http://localhost:8000` API for see all APIs.

If you set email and email-app password in email_host_data then sent otp and recovery password to user email. Otherwise can see at terminal.

1. POST method `http://localhost:8000/user/register/` API for create user account with:
```bash
{
    "phone_number":01.........,
    "email":"....",
    "first_name":"...",
    "last_name":"....",
    "password":"....."
}
```
2. PATCH method `http://localhost:8000/user/activate/` API for user account activation with:
```bash
    "email":"..",
    "otp":...
```

3. POST method `http://localhost:8000/user/token/` API for obtain access token with:
```bash
{
  "phone_number":"01...",
  "password":"..."
}
```

4. POST method `http://localhost:8000/user/token/refresh/` API for obtain access token with:
```bash
{
  "refresh":"...."
}
```
5. GET method `http://localhost:8000/user/home/` API for authentication with token:

6. PATCH method `http://localhost:8000/user/reset/` API for change password when user is login with:
```bash
    "new_password":".."
```
7. PATCH method `http://localhost:8000/user/forgotten/` API for recover password when forgotten password recover with:
```bash
    "phone_number":"...",
    "email":".."
```
8. POST method `http://localhost:8000/otp/resend/` API for resend OTP when timeout of previous OTP then resend with:
```bash
    "email":"....."
```
9. PATCH method `http://localhost:8000/user/update-profile/` API for update user profile with changeable field or fields:
```bash
    "first_name":"..."
```
or
```bash
    "first_name":"....",
    "last_name":"....."
```
