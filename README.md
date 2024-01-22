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
4. Access your application at http://localhost:8000.

### Stopping the Application
To stop the Docker containers, use the following command:

```bash
docker-compose down
```