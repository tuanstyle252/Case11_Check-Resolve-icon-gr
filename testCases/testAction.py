from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.loginPage import Loginpage
import time
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class Testaction:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()

    def test_action2(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        resolve = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[3]/button")
        ActionChains(self.driver).move_to_element(menu).move_to_element(resolve).perform()

        #tooltip "resolve" should be shown
        txt_resolve = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rTest-tooltip_tickets-resolve-tooltip']/div[2]")))
        assert txt_resolve.text == "Resolve"

        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")

        ActionChains(self.driver).move_to_element(menu).move_to_element(edit).perform()
        #check resolve close
        txt_resolve = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='rTest-tooltip_tickets-resolve-tooltip']/div[2]")))
        assert txt_resolve == True

        self.driver.close()

    def test_action3(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='nav-tabs-tickets']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        resolve = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[3]/button")
        ActionChains(self.driver).move_to_element(menu).click(resolve).perform()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='status']/div[1]/div[1]/div[1]/div[2]"))).click()
        #check sucees
        title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@role='table']/tbody/tr[1]/td[3]")))
        mess = f"""×
Close alert
Success! The ticket {title.text} was resolved."""
        txt = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rtest-alert-notifications']/div")))

        assert txt.text == mess

        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        resolve = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(resolve).perform()

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[1]/span[2]/a"))).click()

        self.driver.close()







