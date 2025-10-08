# Playwright

# Playwright

> Install Playwright
```bash 
  pip install pytest-playwright playwright
```

> Install browsers
```bash
  playwright install
```

> Install dependencies
```bash
  playwright install-deps
``` 

> Update playwright to latest version:

```bash
  pip install pytest-playwright playwright -U

```

> Run 
```bash
  python -m pytest

```
```bash
  python -m pytest --browser firefox --headed

```


> Generate code
```bash
  playwright codegen demoqa.com
```

> Example

```python
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/")
    page.get_by_role("heading", name="Elements").click()
    page.get_by_text("Text Box").click()
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Edwin Taquichiri")
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Name:Edwin Taquichiri").click()

``` 

## Actions

### Navigation
Most of the tests will start with navigating page to the URL. After that, test will be able to interact with the page elements.

```python
page.goto("https://playwright.dev/")
```


### Interactions
Performing actions starts with locating the elements. Playwright uses Locators API for that. Locators represent a way to find element(s) on the page at any moment, learn more about the different types of locators available. Playwright will wait for the element to be actionable prior to performing the action, so there is no need to wait for it to become available.

### Create a locator.
```python
get_started = page.get_by_role("link", name="Get started")
```

### Click it.
```python
get_started.click()
```

In most cases, it'll be written in one line:

```python
page.get_by_role("link", name="Get started").click()
```


## Basic actions
This is the list of the most popular Playwright actions. Note that there are many more, so make sure to check the Locator API section to learn more about them.

| Action	| Description |
| --- | --- |
| locator.check() | Check the input checkbox |
| locator.click() | Click the element |
| locator.uncheck() | Uncheck the input checkbox |
| locator.hover() | Hover mouse over the element |
| locator.fill() | Fill the form field, input text |
| locator.focus() | Focus the element |
| locator.press() | Press single key |
| locator.set_input_files() | Pick files to upload |
| locator.select_option() | Select option in the drop down |


## Assertions

Playwright includes assertions that will wait until the expected condition is met. Using these assertions allows making the tests non-flaky and resilient. For example, this code will wait until the page gets the title containing "Playwright":

```python
import re
from playwright.sync_api import expect

expect(page).to_have_title(re.compile("Playwright"))
```

Here is the list of the most popular async assertions. Note that there are many more to get familiar with:

| Assertion	| Description |
| --- | --- |
| expect(locator).to_be_checked() | Checkbox is checked |
| expect(locator).to_be_enabled() | Control is enabled |
| expect(locator).to_be_visible() | Element is visible |
| expect(locator).to_contain_text() | Element contains text |
| expect(locator).to_have_attribute() | Element has attribute |
| expect(locator).to_have_count() | List of elements has given length |
| expect(locator).to_have_text() | Element matches text |
| expect(locator).to_have_value() | Input element has value |
| expect(page).to_have_title() | Page has title |
| expect(page).to_have_url() | Page has URL |

## Wait Strategies

### Auto-waiting

Playwright performs a range of actionability checks on the elements before making actions to ensure these actions behave as expected. It auto-waits for all the relevant checks to pass and only then performs the requested action. If the required checks do not pass within the given timeout, action fails with the TimeoutError.

For example, for locator.click(), Playwright will ensure that:

- locator resolves to exactly one element
- element is Visible
- element is Stable, as in not animating or completed animation
- element Receives Events, as in not obscured by other elements
- element is Enabled

## Refs.:

> Playwright https://playwright.dev/python/docs/writing-tests
> 