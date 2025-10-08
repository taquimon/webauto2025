## Secrets

1. using env variables

```shell
$ export variable_name=value
$ export username=dummy_usernmae
```

```python
import os

# Get the secret key from the environment
secret_username = os.environ.get('username')
print(secret_username)
```

2. Using dotenv
   first install python-dotenv

```shell
pip install python-dotenv
```

create .env file

```shell
  username=test-username
  password=test-password
```

then load the content of file like this example

```python
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")

print("USERNAME: ", username)
print("PASSWORD: ", password)
```

## Config files
Here are some of the commonly used configuration files in Python:

- Python Configuration Files
> pyhon config
```python
drivers_config = {
    "URL": "localhost.com",
    "FileName": "name.json",
}
```
> python script
```python
import config as cfg
 
driver = webdriver.Firefox()
driver.get(cfg.drivers_config["URL"])
```

- JSON Configuration Files
> JSON file
```json
{
    "drivers_config":{
        "URL":"localhost.com",
        "FileName" : "file.json"
      }
}
```
> python script
```python
# reading config file
file = open("config.json",)
data = json.load(file)
 
# using config file
print(data["drivers_config"]["URL"])
```

- YAML Configuration Files
> YAML file
```yaml
drivers_config:
	URL: localhost.com
	FileName: file.json
other:
     Variable: data
```
> python script
```python
file = open("config.yml", "r") 
cfg = yaml.load(file)

print(cfg["drivers_config"]["URL"])
# this will print "localhost.com" 
 
print(cfg["drivers_config"])
# this will print 
```

- INI Configuration Files
> .ini file 
```editorconfig
[drivers_config]
URL=localhost.com
FileName=file.json
```
> python script

```python
import configparser
file = open("../pytest.ini", "r")

config = configparser.RawConfigParser(allow_no_value=True)
config.read_file(file)

print(config.get("drivers_config", "URL"))
```
- XML Configuration Files



## Refs.:

> Config files : https://www.lambdatest.com/blog/how-to-read-configuration-files-in-python-using-selenium/