## CI/CD (Continuous Integration and Continuous Delivery/Deployment)

## jenkins

* freestyle

### plugins required

* python
* allure

### env variables

1. global properties

2. using Envinject plugin
   - Properties Content

## Build Steps

### Execute Shell

```shell
  python3.12 -V
  python3.12 -m venv venv
  . venv/bin/activate
  export PYTHONPATH="$WORKSPACE:$WORKSPACE/src"
  echo $PYTHONPATH
  pip install -r requirements.txt
  python3.12 -m pytest tests...

```

### Post build actions

- Allure Reports
- junit reports
- html reports

### Selenium docker

Example:

```yml
# To execute this docker compose yml file use `docker compose -f docker-compose-v3-beta-channel.yml up`
# Add the `-d` flag at the end for detached execution
# To stop the execution, hit Ctrl+C, and then `docker compose -f docker-compose-v3-beta-channel.yml down`
services:
  chrome:
    image: selenium/node-chrome:beta
    shm_size: 2gb
    depends_on:
      - selenium-hub
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub

  edge:
    image: selenium/node-edge:beta
    shm_size: 2gb
    depends_on:
      - selenium-hub
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub

  firefox:
    image: selenium/node-firefox:beta
    shm_size: 2gb
    depends_on:
      - selenium-hub
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub

  selenium-hub:
    image: selenium/hub:latest
    container_name: selenium-hub
    ports:
      - "4442:4442"
      - "4443:4443"
      - "4444:4444"

## Pre-commit

Install pre-commit

```bash
pip install pre-commit
pre-commit install
```
Run pre-commit

```bash
pre-commit run --all-files
```

## GitLab

> Example

```yaml
stages:
  - test

selenium-docker-tests:
  stage: test
  image: python:3
  services:
    - docker:dind # Docker-in-Docker service to manage other containers
  variables:
    DOCKER_HOST: tcp://docker:2375
    DOCKER_TLS_CERTDIR: "" # Disable TLS for Docker-in-Docker for simplicity in this example
    SELENIUM_HUB_HOST: selenium-hub # Hostname for the Selenium Hub container
    PYTHONPATH: "$CI_PROJECT_DIR:$CI_PROJECT_DIR/src"
  before_script:
    - apt-get update && apt-get install -y docker-compose # Install docker-compose
    - sleep 30
    - docker info
    - docker-compose up -d # Start Selenium Grid using docker-compose
    - pip install -r requirements.txt # Install Python dependencies
    - echo $PYTHONPATH
  script:
    - pytest tests/demoqa/selenium -vs #sun your Python Selenium tests
  after_script:
    - docker-compose down # Stop and remove Selenium Grid containers

```


```

## Final Task

* Deploy your WEB Automation frameworks on any CI/CD (jenkins, docker, gitlab)
* Execution should have any technology that we have learned in the course (selenium, selenium+pagefactory, playwright, screenpy)
* Tests should include data-driven
* Tests should be executed on any browser (chrome, firefox, edge)


> selenium docker https://github.com/SeleniumHQ/docker-selenium

> jenkins https://www.jenkins.io/doc/book/installing/linux/

> pre-commit https://pre-commit.com/
