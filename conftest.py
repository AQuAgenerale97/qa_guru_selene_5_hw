import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    print("Browser_management fixture is used")
    driver_options = webdriver.FirefoxOptions()
    driver_options.page_load_strategy = 'eager'

    browser.config.driver_options = driver_options
    browser.config.window_height = '1920'
    browser.config.window_width = '1080'
    browser.config.base_url = 'https://demoqa.com'
    yield

    browser.quit()
