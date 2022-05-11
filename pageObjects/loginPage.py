from selenium.webdriver.common.by import By

class Loginpage:
    textbox_username = "//*[@id='identifierId']"
    textbox_password = "//*[@id='password']/div[1]/div/div[1]/input"
    click_login = "//*[@id='passwordNext']/div/button"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username).clear()
        self.driver.find_element(By.XPATH, self.textbox_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password).clear()
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.click_login).click()