## Parallel Execution

> Install library
```shell
pip install pytest-xdist
```

> Command Execution
```shell
 python -m pytest tests/demoqa/selenium/ -vs -n 3
```

for increment nodes in docker compose
```yaml
SE_NODE_MAX_SESSIONS=10
```

> Playwright option example
```shell
python -m pytest tests/demoqa/playwright/ -vs --numprocesses 2
```


### Attach image on failures
```python
try:
    assert <condition>, <message on failure>
except AssertionError as e:
    allure.attach(driver.get_screenshot_as_png(), name=request.node.name, attachment_type=AttachmentType.PNG)
    logger.error(e)
    raise e
```

```yml
RUN wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
RUN dpkg -i allure_2.18.1-1_all.deb
```

>Docker file Example
```yml
# image with python
FROM python:3

# label del maintainer
LABEL maintainer="edwin.taquichiri@jalasoft.com"

# copy the code to /opt/app folder
COPY . /opt/app
WORKDIR /opt/app

# update system
RUN apt-get update

# install java always add -y option
RUN apt-get install -y default-jre
RUN java -version

# install allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
RUN dpkg -i allure_2.18.1-1_all.deb

# install/upgrade pip
RUN python3 -m pip install --upgrade pip

# install virtualenv librarary/package
RUN python3 -m pip install --user virtualenv

# create virtualenv for the framework
RUN python3 -m venv env

# activate virtual environment
RUN . env/bin/activate

# install requirements
RUN python3 -m pip install -r requirements.txt
```
