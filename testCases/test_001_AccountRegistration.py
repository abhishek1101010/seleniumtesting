from PageObjects.HomePage import HomePage
from PageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
import os
from utilities.customLogger import LogGen


class Test_001_AccountReg:

    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()


    def test_account_reg(self,setup):
        self.logger.info("*****test_001 started*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("clicking on myaccount and register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("providing cuctomer details for registration")
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("john")
        self.regpage.setLastName("kennedy")
        self.email=randomeString.random_string_generator()+'gmail.com'

        self.regpage.setEmail(self.email)
        self.regpage.setPassword("fhajksk")
        self.regpage.setPrivatePolicy()
        self.regpage.clickContinue()
        self.driver.close()

        self.logger.info("******test_01 ended*****")

