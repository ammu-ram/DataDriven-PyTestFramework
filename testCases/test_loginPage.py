import pytest
from selenium  import webdriver
from pageObjects.loginPage import LoginPage
from utitlities.customLogger import logGeneration
from utitlities.readProperties import ReadConfiguration
from pageObjects.loginPagebydatadriven import LoginPageDataDriven
from utitlities.excelutils import datadriven

class Testlogin():
    baseUrl= ReadConfiguration.url()
    username=ReadConfiguration.username()
    password=ReadConfiguration.password()
    logger = logGeneration.logGen()
    path_test1 = '../screenshots/test_login.png'
    path_excel = '../testdata/logindata.xlsx'

    @pytest.mark.regression
    def test_login(self):
        self.logger.info("Driver initialized")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(2)
        test1 = LoginPage(self.driver)
        test1.login(self.username,self.password)
        if self.driver.title=="Swag Labs":
            assert True
        else:
            self.driver.save_screenshot(self.path_test1)
            #../screenshots/test_login.png
            assert False


