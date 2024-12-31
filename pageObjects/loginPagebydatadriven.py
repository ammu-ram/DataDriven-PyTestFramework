from selenium.webdriver.common.by import By

class LoginPageDataDriven:
    name_id = "user-name"
    pass_id = "password"
    login_id = "login-button"
    menu_xpath="//button[.='Open Menu']"
    logout_id="logout_sidebar_link"

    def __init__(self,driver):
        self.driver=driver
    def passCredentials(self,username1,password1):
        self.driver.find_element(By.ID,self.name_id).send_keys(username1)
        self.driver.find_element(By.ID,self.pass_id).send_keys(password1)

    def submittinguserCredentials(self):
        self.driver.find_element(By.ID,self.login_id).click()


    def logout(self):
        self.menu = self.driver.find_element(By.XPATH, self.menu_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", self.menu)
        self.menu.click()
        self.logout_id=self.driver.find_element(By.ID,self.logout_id)
        self.driver.execute_script("arguments[0].scrollIntoView()",self.logout_id)
        self.logout_id.click()


