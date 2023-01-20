from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def setup():

    # ignore certificate errors
    # options = Options()
    # options.add_argument('--allow-running-insecure-content')
    # options.accept_insecure_certs = True
    # options.add_argument('ignore-certificate-errors')

    driver= webdriver.Chrome()
    print("Launching chrome browser...")
    return driver


