# STOCK VOLATILITY CALCULATOR
API to upload closing prices of stock and calculate Daily and Anual Volatility

## Getting Started
These instructions will help you set up and run your Django project using Docker.

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

- [Docker Installation](https://docs.docker.com/get-docker/)
- [Docker Compose Installation](https://docs.docker.com/compose/install/)

### Running the Application
1. Clone the repository:
    ```bash
    git clone https://github.com/vasudeogaichor/finzome-python-assignment
    ```

2. Navigate to the project directory:
    ```bash
    cd finzome-python-assignment
    ```
3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```
4. Access your application at http://127.0.0.1:8000.

### Stopping the Application
To stop the Docker containers, use the following command:

```bash
docker-compose down
```
<br>
<br>

## To run without docker:

1. Install virtualenv to create a virtual environment for your project. Open a terminal and run:
    ```bash
    pip install virtualenv
    ```
2. Clone the repository:
    ```bash
    git clone https://github.com/vasudeogaichor/finzome-python-assignment
    ```
3. Navigate to the project directory:
    ```bash
    cd finzome-python-assignment
    ```
4. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
5. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
6. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
7. Make migrations and apply them to the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Start the Django development server:
    ```bash
    python manage.py runserver
    ```
Access your application at http://127.0.0.1:8000.

### Stopping the Server:
To stop the Django development server, press Ctrl + C in the terminal.