## How to run Pytest scripts on physical machine
This example shows you to run on your Computer.

### Prerequisites
[Install Python 3.x](https://www.python.org/downloads/)
install pytest, allure-pytest, pytest-xdist
```console
pip install pytest
pip install allure-pytest
pip install pytest-xdist
```

### Example commands to run locally
```console
pytest .
pytest
pytest -k add_remove_elements
pytest -m "not error" 
pytest -m high_priority
pytest -m sanity_tests

pytest -n 5 --browser "chrome" --executor "remote"
pytest -n 2 --browser "firefox"
pytest --browser="chrome" --executor="remote" tests/test_form_authentication.py
```

## How to run using Docker Compose
This example shows you to run this pytest script using docker compose.

### Prerequisites
Need to have docker installed. Linux users make sure you have docker compose is installed(which needs to be installed seperatly)

Start Docker Compose
```console
docker-compose up -d --scale chrome=5 --scale firefox=0
```

Build a docker image localy which contain source code
```console
docker build -t pytest-with-src -f pytest.Dockerfile .
```
Execute the automation script
```console
docker run --network="host" --rm pytest-with-src --browser "chrome" --executor "remote"
```
(Teardown) Delete the image once the execution completes
```console
docker rmi pytest-with-src
```
(Teardown) Exit Docker Compose
```console
docker-compose down --rmi local
```
## How to run using Docker Swarm
This example helps to run this pytest script on Docker Swarm.
### Prerequisites
Docker swarm should be initiated also if you have multiple nodes, workers and managers has to be setup. 

#### Start Swarm services using stack
```console
docker stack deploy -c selenium-swarm-stack.yml grid
```
Scale up if required
```console
docker service scale grid_chrome=10
docker service scale grid_firefox=10
```
Copy the python scrips and create an image locally
```console
docker build -t pytest-with-src -f pytest.Dockerfile .
```
Execute the automation script
```console
docker run --network="host" --rm pytest-with-src --browser "chrome" --executor "remote"
```
(Teardown) Delete the image once the execution completes
```console
docker rmi pytest-with-src
```
(Teardown) Exit stack
```console
docker stack rm grid
```
