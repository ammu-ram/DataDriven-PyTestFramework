from selenium.webdriver.common.by import By

class LoginPage:
    name_id = "user-name"
    pass_id = "password"
    login_id = "login-button"
    menu_id="react-burger-menu-btn"
    logout_id="logout_sidebar_link"

    def __init__(self,driver):
        self.driver=driver
    def login(self,username,password):
        self.driver.find_element(By.ID,self.name_id).send_keys(username)
        self.driver.find_element(By.ID,self.pass_id).send_keys(password)
        self.driver.find_element(By.ID,self.login_id).click()
        self.menu=self.driver.find_element(By.ID,self.menu_id)
        self.driver.execute_script("arguments[0].scrollIntoView()",self.menu)
        self.menu.click()
        self.logout_id=self.driver.find_element(By.ID,self.logout_id)
        self.driver.execute_script("arguments[0].scrollIntoView()",self.logout_id)
        self.logout_id.click()


