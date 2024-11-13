# django-patent-api
 Rest API for the patent analysis.


# Patent API Documentation

This project provides a Django-based API for managing and querying patent data. Below are the instructions on how to run the API both locally and using Docker-Compose, as well as example API requests and responses.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Run the API Locally](#run-the-api-locally)
- [Run the API with Docker-Compose](#run-the-api-with-docker-compose)
- [API Endpoints](#api-endpoints)
  - [GET /summary](#get-summary)
  - [GET /query](#get-query)
- [Example Requests & Responses](#example-requests--responses)
  - [GET /summary](#get-summary-example)
  - [GET /query](#get-query-example)

---

## Prerequisites

Before running the API, make sure you have the following installed:

- **Python 3.12** or higher
- **Docker** and **Docker-Compose** (for Docker setup)
- **PostgreSQL** (for local setup if you choose not to use Docker)

---

## Run the API Locally

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-patent-api.git
cd django-patent-api
````

### 2\. Create a virtual environment:

```bash
python3 -m venv venv
```

### 3\. Activate the virtual environment:

*   On **Windows**:
    
    ```bash
    venv\Scripts\activate
    ```
    
*   On **Mac/Linux**:
    
    ```bash
    source venv/bin/activate
    ```
    

### 4\. Install dependencies:

```bash
pip install -r requirements.txt
```

### 5\. Set up the database:

Make sure PostgreSQL is installed and running. Create a database named `patent_data` or use the credentials from the `settings.py` file to connect to your PostgreSQL instance.

### 6\. Apply database migrations:

```bash
python manage.py migrate
```

### 7\. Load data into the database:

You can load patent data into the database by running the custom data loading script (e.g., `load_patents.py`).

### 8\. Start the Django development server:

```bash
python manage.py runserver
```

Your API should now be running locally at `http://127.0.0.1:8000/`.

* * *

Run the API with Docker-Compose
-------------------------------

To run the API using Docker and Docker-Compose:

### 1\. Ensure Docker is installed:

Make sure Docker and Docker-Compose are installed on your machine.

### 2\. Clone the repository:

```bash
git clone https://github.com/ISZM13/django-patent-api.git
cd django-patent-api
```

### 3\. Build and start the services:

```bash
docker-compose up --build
```

This will:

*   Build the Docker image for your Django app.
*   Set up the PostgreSQL container.
*   Start the Django web service and the database service.

The API will be available at `http://127.0.0.1:8000/` once the containers are running.

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
  },
  ...
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
  },
  ...
]
```

* * *

Example Requests & Responses
----------------------------

### GET /summary Example:

**Request:**

```http
GET /summary/
```

**Response:**

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

### GET /query Example:

**Request:**

```http
GET /query?country_code=US&assignee=State%20Farm
```

**Response:**

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

*   **Database connection error:** Ensure PostgreSQL is running and configured correctly. Check the `DATABASES` settings in `settings.py`.
*   **Package installation failure:** Ensure the correct versions of required packages are listed in `requirements.txt`.

* * *

Folder Structure
----------------

```bash
/django-patent-api
│
├── /pics                    # Folder for project-related images (e.g., screenshots)
│
├── /mysite                  # Django project folder
│   ├── /api                 # Django app folder
│   ├── /db.sqlite3          # SQLite database (if using SQLite locally)
│   ├── Dockerfile           # Dockerfile for building the image
│   ├── docker-compose.yml   # Docker Compose configuration
│   └── requirements.txt     # Python dependencies
│
├── README.md                # Project documentation
```

* * *

License
-------

MIT License

Copyright (c) 2024 Ishtveer Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---
