## Hard Assertions
Hard assertions in Python, unlike soft assertions, stop the test execution as soon as an assertion fails.

This is useful in testing scenarios where you want to stop the test execution as soon as an issue is encountered, as it helps in identifying the root cause of the failure.

Python uses assert statement for hard assertions.

Example:

```python
assert 1 == 2, "message if fails"
```


## Soft Assertions
Soft assertions in Python, unlike standard "hard" assertions, allow test execution to continue even if an assertion fails.

This is useful in testing scenarios where you want to gather all possible failures within a single test run rather than stopping at the first encountered issue

Python uses soft-assert for soft assertions.

> Example:
```python
from soft_assert import check, verify
    with verify():
        check(1 == 2, "message if fails")
```

## When to Use Each?

- Hard assertions are perfect when something must absolutely, positively be true for your code to work. They’re like the red flags that signal something’s critically wrong.

- Soft assertions are great when you want to gather more information about potential issues without stopping the entire test suite. They let you collect more errors rather than halting at the first sign of trouble.


## Mark a test as expected failure

> Example

```python
@pytest.mark.xfail(reason="Bug #11493: Negative values not supported", strict=True)
```

## Refs.:

 > [soft-assert](https://pypi.org/project/soft-assert/)
