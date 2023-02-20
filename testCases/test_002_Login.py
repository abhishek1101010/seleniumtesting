import pytest

from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    user=ReadConfig.getPassword()
    password=ReadConfig.getUseremail()

    def test_login(self,setup):
        self.logger.info('*****starting test_002_login*****')
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.driver.close()
        self.logger.info("********end of test_002_login")
        


