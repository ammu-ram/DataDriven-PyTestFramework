def test_login(self):
    self.logger.info("Driver initialized")
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get(self.baseUrl)
    self.driver.implicitly_wait(2)
    test1 = LoginPage(self.driver)
    test1.login(self.username, self.password)
    if self.driver.title == "Swag Labs":
        assert True
    else:
        self.driver.save_screenshot(self.path_test1)
        # ../screenshots/test_login.png
        assert False