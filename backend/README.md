# How to set up

1. Start Virtual Environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
or
$ . venv/bin/activate 
on Windows
```


2. Install requirements
```bash
$ pip install -r requirements.txt
```

3. Set up environment variables

- Create a .env.local file in the root directory of the project
- Copy the contents of the .env.example file into the .env.local file
- Fill in the values of the variables in the .env.local file

4. Migrate the database
```bash
$ python manage.py migrate
```

5. Run the server
```bash
$ python manage.py runserver
```

Voila! The server is up and running. You can now access the API at http://localhost:8000/