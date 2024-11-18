import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

from dotenv import load_dotenv
import os


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        help='Версия браузера, в котором будут запускать тесты',
        default='100.0'
    )


@pytest.fixture(scope='function', autouse=True)
def browser_management(load_env, request):
    print("Browser_management fixture is used")

    browser_version = request.config.getoption('--browser_version')

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    browser.config.window_height = '1920'
    browser.config.window_width = '1080'
    browser.config.base_url = 'https://demoqa.com'

    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.page_load_strategy = 'eager'
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, selenoid_url)

    browser.quit()
