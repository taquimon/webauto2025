# Automation Testing Technologies


## Record and Play
Record and playback testing is the process where testers record their actions as they manually perform a test on the application’s user interface. As such, it is a form of automated testing since this process is performed by an automated testing tool.

### Where is Record and Playback Testing Today?

- Limited scope
- Fragile scripts
- Lack of integration
- Cross-browser issues
- Limited programming logic
- UI dependency


## Libraries
Libraries are collections of pre-written code that can be used to perform specific tasks. They are used to reduce the amount of code that needs to be written and to make the code more reusable.

Python libraries for testing:

* Robot
* PyTest
* Unittest
* DocTest
* Nose2
* Testify


## Frameworks
- Selenium
- Playwright
- Cypress
- TestCafe
- Robotframework
  

## Architecture and Structure

Basic Architecture of Automation Examples

<img src="img/basic_arch.png" width="800" height="600">

<img src="img/image0004small.webp" width="800" height="600">

## Folder Structure (Python)

The **“flat layout”** refers to organising a project’s files in a folder or repository, such that the various configuration
files and import packages are all in the top-level directory


<pre style="color:rgb(17, 184, 58);">
├── README.md
├── noxfile.py
├── pyproject.toml
├── setup.py
├── awesome_package/
│   ├── __init__.py
│   └── module.py
│   └── tests/
│       └── test_module.py
│       └── test_module2.py
└── tools/
    ├── generate_awesomeness.py
    └── decrease_world_suck.py
</pre>


The **“src layout”** deviates from the flat layout by moving the code that is intended to be importable (i.e. import
awesome_package, also known as import packages) into a subdirectory. This subdirectory is typically named src/, hence
“src layout”.

<pre style="color:rgb(17, 184, 58);">
├── README.md
├── noxfile.py
├── pyproject.toml
├── setup.py
├── src/
│    └── awesome_package/
│       ├── __init__.py
│       └── module.py
│       └── tests/
│           └── test_module.py
│           └── test_module2.py
└── tools/
    ├── generate_awesomeness.py
    └── decrease_world_suck.py
</pre>


## Setting Up Web Automation with Python

Python is a popular and versatile programming language. Combining pytest, nose2 with Python allows for efficient and readable
test scripts, making
it a preferred choice for API test automation.

## Setup Environment

> create venv

```shell
python3.12 -m venv venv
```

> activate venv

```shell
. venv/bin/activate
```

> verify you are in virtual environment

```shell
(venv) predator@avp ~/p/playpy>
```



# Ref.:

> Layouts: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

> Test Architecture: https://blog.testproject.io/2020/06/29/design-patterns-in-test-automation/

> Why no-code test dont work: https://testrigor.com/blog/why-no-code-low-code-test-automation-tools-dont-work/

> Record and playback testing: https://testrigor.com/blog/record-and-playback-testing/