* * *

Django Patent API
=================

A RESTful API for managing and querying patent data, built with Django.

* * *

Table of Contents
-----------------

*   [Overview](#overview)
*   [Prerequisites](#prerequisites)
*   [Installation](#installation)
    *   [Run Locally](#run-locally)
    *   [Run with Docker\-Compose](#run-with-docker-compose)
*   [API Endpoints](#api-endpoints)
    *   [GET /summary](#get-summary)
    *   [GET /query](#get-query)
*   [Example Requests & Responses](#example-requests--responses)
*   [Troubleshooting](#troubleshooting)
*   [Folder Structure](#folder-structure)
*   [License](#license)

* * *

Overview
--------

This project provides a Django-based API for managing and querying patent data. It supports Docker for simplified deployment and includes example API requests and responses for better understanding.

* * *

Prerequisites
-------------

Before running the API, ensure you have the following installed:

*   **Python 3.12** or higher
*   **Docker** and **Docker-Compose** (if using Docker)
*   **PostgreSQL** (for local setup if not using Docker)

* * *

Installation
------------

### Run Locally

#### 1\. Clone the repository:

```bash
git clone https://github.com/ISZM13/django-patent-api.git
cd django-patent-api
```

#### 2\. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

#### 3\. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 4\. Set up the database:

*   Ensure PostgreSQL is installed and running.
*   Create a database named `patent_data` or use the settings from `settings.py`.

#### 5\. Load patent data into your local Postgres dataset:

```bash
cd mysite
python manage.py load_patents  
```
#### 6\. Change DATABASES values in mysite/mysite/settings.py
From the root folder `django-patent-api`

```bash
cd mysite/mysite
# Go to settings.py file and make changes in it, it should look like 
# remove host key-value if it exists
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'patent_data',
        'USER': 'your_postgres_username',
        'PASSWORD': 'your_postgres_pass',
        'PORT': 'your_postgres_port(default=5432)',
    }
}
```

#### 7\. Apply migrations:
Inside the `django-patent-api/mysite` folder.

```bash
python manage.py makemigrations
python manage.py migrate
```


#### 8\. Run the server:
Inside the djnago project folder, here `django-patent-api/mysite` rin:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

* * *

### Run with Docker-Compose

#### 1\. Ensure Docker is installed and running.

#### 2\. Clone the repository:

```bash
git clone https://github.com/ISZM13/django-patent-api.git
cd django-patent-api
```

#### 3\. Make sure PostgreSQL server is running:
Also, it should have a database with the name of `patent_data`.
Change the `DATABASES` in `mysite/mysite/settings.py`, it should look like this:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'mydb'),
        'USER': os.getenv('POSTGRES_USER', 'myuser'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'mypassword'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

```

#### 4\. Build and start the services:
Go to the django project folder `(/mysite)` to start the services.

```bash
cd mysite
docker-compose build   # build the container using build 
docker-compose up      # and start it using up
```

This will:

*   Build the Docker image for the Django app.
*   Set up a PostgreSQL container.
*   Start the Django web service and the database service.

Once the containers are running, the API will be available at `http://127.0.0.1:8000/`.

#### 5\. Ending Services:
You can use the API  at `http://127.0.0.1:8000/`.
To close the running server, press `Ctrl + C` in the server. and then to remove the container from the docker write the code:
```bash
docker-compose down     # to remove the container
```


* * *

API Endpoints
-------------

### GET /summary

Returns summary statistics (mean, median, etc.) for numerical columns in the patent dataset.

#### Example Request:

```http
GET /summary/
```

#### Example Response:

```json
{
  "priority_date": {
    "min": "2010-01-01T00:00:00Z",
    "max": "2022-12-31T23:59:59Z"
  },
  "creation_date": {
    "min": "2012-01-01T00:00:00Z",
    "max": "2023-01-01T00:00:00Z"
  }
}
```

### GET /query

Filters patent data based on query parameters like `patent_id` or `country_code`.

#### Example Request:

```http
GET /query?country_code=US&assignee=State%20Farm
```

#### Example Response:

```json
[
  {
    "patent_id": "US-11238538-B1",
    "country_code": "US",
    "title": "Autonomous vehicle component maintenance and repair",
    "assignee": "State Farm Mutual Automobile Insurance Company",
    "creation_date": "2016-01-22T00:00:00Z",
    "publ_date": "2022-12-13T00:00:00Z",
    "grant_date": "2022-12-13T00:00:00Z",
    "result_link": "https://patents.google.com/patent/US11238538B1/en",
    "fig_link": "https://patentimages.storage.googleapis.com/7b/3d/34/bef86af9dbc..."
  }
]
```

* * *

Troubleshooting
---------------

### Common Issues:

*   **Database connection error**: Ensure PostgreSQL is running and configured correctly. Verify the database settings in `settings.py`.
*   **Package installation failure**: Ensure the correct versions of required packages are listed in `requirements.txt`.

* * *

Folder Structure
----------------

```bash
/django-patent-api
│
├── /date_preprocessing      # Folder which inclues the .ipynb file used for cleaning
├── /dataset                 # Folder for storing raw and cleaned datasets used
├── /mysite                  # Django project folder
│   ├── /api                 # Django app folder
│   ├── /mysite              # Django project folder
│   ├── db.sqlite3           # SQLite database (if using SQLite locally)
│   ├── Dockerfile           # Dockerfile for building the image
│   ├── docker-compose.yml   # Docker Compose configuration
│   ├── cleaned-dataset.csv  # Cleaned dataset to be uploaded to PostgreSQL Server.
│   └── requirements.txt     # Python dependencies
│
├── README.md                # Project documentation
```

* * *

License
-------

MIT License

© 2024 Ishtveer Singh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

* * *
