from selenium import webdriver
from selenium.webdriver.common.by import By
import timeit


if __name__ == '__main__':

    xpath_locator = '//*[@id="item-0"]/span'
    css_locator = 'li[id="item-0"] span'

    repetitions = 1000

    driver = webdriver.Chrome()
    driver.get('http://demoqa.com/elements')

    css_time = timeit.timeit("driver.find_element(By.CSS_SELECTOR, css_locator)",
                    number=repetitions, globals=globals())
    xpath_time = timeit.timeit('driver.find_element(By.XPATH, xpath_locator)',
                    number=repetitions, globals=globals())

    driver.quit()

    print("CSS total time {} repeats: {:.2f} ms, per find".
        format(repetitions, css_time))
    print("XPATH total time for {} repeats: {:.2f} ms, per find".
        format(repetitions, xpath_time))