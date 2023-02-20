import time
import pytest
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_Login_DDT():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    path=os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"


    def test_login_ddt(self,setup):
        self.logger.info("*********starting test_003_login_ddt*********")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.lp=LoginPage(self.driver)
        self.ma=MyAccountPage(self.driver)

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()
            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password=XLUtils.readData(self.path,"Sheet1",r,2)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.ma.clicklogout()
        self.driver.close()



