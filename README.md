# Goal International Backend API

This is the backend api for goal international database system

### Follow the instructions below to run the project.

Clone the repository to your local machine:
shell

git clone <repository_url>


Change into the project directory:
shell

cd <project_directory>


Create a virtual environment (optional but recommended):
shell

python -m venv myenv
```

Activate the virtual environment:

    For Windows:
    shell

myenv\Scripts\activate

For macOS/Linux:
shell

    source myenv/bin/activate

Install the required packages from the requirements.txt file:
shell

pip install -r requirements.txt
```

Run database migrations:
shell

python manage.py migrate
```

Start the development server:
shell

    python manage.py runserver
    ```

    Access the API endpoints and explore the documentation:
        API endpoints: http://localhost:8000/api/
        Obtain JWT token: http://localhost:8000/api/token/
        Refresh JWT token: http://localhost:8000/api/token/refresh/
        API documentation (Swagger UI): http://localhost:8000/api/docs/
        API documentation (Redoc): http://localhost:8000/api/redoc/

That's it! You have successfully set up and started the Django backend API. You can now interact with the API endpoints and explore the documentation using the provided URLs.

Please note that these instructions assume you have Python and Git installed on your machine. If not, make sure to install them before proceeding.