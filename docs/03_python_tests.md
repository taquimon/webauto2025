## Unittest

Unit Test Framework features:

- **test fixture**. A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
- **test case**. A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
- **test suite**. A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
- **test runner**. A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.

**Example**

```python
import unittest


class TestProject(unittest.TestCase):

    # fixture
    def setUp(self):
        print("Setup")

    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")

    def test_three(self):
        print("test three")

    # fixture
    def tearDown(self):
        print("tearDown")
```

## Pytest

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

**Installation**

```shell
  pip install pytest
```

Advantages of pytest

* Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
* Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
* Pytest allows us to skip a subset of the tests during execution.
* Pytest allows us to run a subset of the entire test suite.
* Pytest is free and open source.
* Because of its simple syntax, pytest is very easy to start with.

## Anatomy of an automated test

In the simplest terms, a test is meant to look at the result of a particular behavior, and make sure that result aligns with what you would expect. Behavior is not something that can be empirically measured, which is why writing tests can be challenging.
“Behavior” is the way in which some system acts in response to a particular situation and/or stimuli. But exactly how or why something is done is not quite as important as what was done.

You can think of a test as being broken down into four steps:

* **Arrange**. is where we prepare everything for our test. This means pretty much everything except for the “act”. It’s lining up the dominoes so that the act can do its thing in one, state-changing step. This can mean preparing objects, starting/killing services, entering records into a database, or even things like defining a URL to query, generating some credentials for a user that doesn’t exist yet, or just waiting for some process to finish.
* **Act**. is the singular, state-changing action that kicks off the behavior we want to test. This behavior is what carries out the changing of the state of the system under test (SUT), and it’s the resulting changed state that we can look at to make a judgement about the behavior. This typically takes the form of a function/method call.
* **Assert**. is where we look at that resulting state and check if it looks how we’d expect after the dust has settled. It’s where we gather evidence to say the behavior does or does not aligns with what we expect. The assert in our test is where we take that measurement/observation and apply our judgement to it. If something should be green, we’d say assert thing == "green".
* **Cleanup**. is where the test picks up after itself, so other tests aren’t being accidentally influenced by it.

At its core, the test is ultimately the act and assert steps, with the arrange step only providing the context. Behavior exists between act and assert.

## Fixtures

“Fixtures”, in the literal sense, are each of the arrange steps and data. They’re everything that test needs to do its thing.

### unittests fixtures

```python
        @classmethod
        def setup_class(cls):

        def setup_method(self):

        def test_one(self):

        def test_two(self):

        def test_three(self):

        def teardown_method(self):

        @classmethod
        def teardown_class(cls):
```

### pytest fixtures

Example

```python
# Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def order(first_entry):
    return first_entry
```

### Levels of fixture scopes

* **Function** (Set up and tear down once for each test function) (default)
* **Class** (Set up and tear down once for each test class)
* **Module** (Set up and tear down once for each test module/file)/
* **Session** (Set up and tear down once for each test session i.e comprising one or more test files)


### addoption

The pytest adoption feature extends the flexibility of command-line arguments in pytest by dynamically passing them to unit tests. This feature allows you to define custom command line arguments for tests.

Example

```python
def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='dev', help="Environment where the tests are executed"
    )
```

## References


> unittests: https://docs.python.org/3/library/unittest.html


> pytest: https://docs.pytest.org/en/stable/

