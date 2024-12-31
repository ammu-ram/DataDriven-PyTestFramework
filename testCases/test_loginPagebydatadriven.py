from turtle import TurtleGraphicsError

import pytest
from selenium  import webdriver
from utitlities.customLogger import logGeneration
from utitlities.readProperties import ReadConfiguration
from pageObjects.loginPagebydatadriven import LoginPageDataDriven
from utitlities.excelutils import datadriven

class Testlogin():
    baseUrl= ReadConfiguration.url()
    logger = logGeneration.logGen()
    path_test1 = '../screenshots/test_logindataDriven.png'
    path_excel = 'C:/Users/Admin/PycharmProjects/DataDriven-PyTestFramework/datadriven/testdata/logindata.xlsx'

    @pytest.mark.regression
    def test_logindataDriven(self):
        self.logger.info("Driver initialized")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(2)
        self.rows = datadriven.getRowCount(self.path_excel,'Sheet1')
        test2 = LoginPageDataDriven(self.driver)
        for r in range(1,self.rows+1):
            username1 = datadriven.readData(self.path_excel,'Sheet1',r,1)
            password1 = datadriven.readData(self.path_excel,'Sheet1',r,2)
            test2.passCredentials(username1,password1)
            test2.submittinguserCredentials()
            if self.driver.title == "Swag Labs":
                datadriven.writeData(self.path_excel,'Sheet1',r,3,"PASS")
                assert True
            else:
                datadriven.writeData(self.path_excel,'Sheet1',r,3,"FAIL")
                self.driver.save_screenshot(self.path_test1)
                assert False
