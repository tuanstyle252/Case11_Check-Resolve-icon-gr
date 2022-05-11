import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    options = Options()
    driver = webdriver.Chrome(options = options, executable_path = "D:\\PycharmProjects\\cas1_gr\\drivers\\chromedriver.exe")
    return driver