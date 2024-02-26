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
