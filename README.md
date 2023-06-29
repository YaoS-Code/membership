<h1>Membership</h1>
<hr>
<h2>Jun 28, 2023</h2> 

1. Create Database, 6 tables.
   - UserInfo
   - Membership
   - MembershipPayment
   - MemberConsume
   - ConsumeItem
   - ServiceRecord
   

2. add Env Variables
   - install python library ```pip install pydotenv```
   - create a .env file at the root direction
     - ```
       DATABASE_NAME=xxxx
       ....
       ```
   - setting.py (You should set these values from your own database)

```

import dotenv
dotenv.load_dotenv()

...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_URL'),  
        'PORT': os.getenv('DATABASE_PORT'),
    }
}
```

<hr>

<h2>Jun 29, 2023</h2> 

1. For backend app, add login & signup page, no database yet.
2. add some animation
```
localhost:8000/backend/login
localhost:8000/backend/signup
```
