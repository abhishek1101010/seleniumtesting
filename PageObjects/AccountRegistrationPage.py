from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name="email"
    txt_password_name="password"
    checkbox_policy_css=".d-inline-block.pt-2.pd-2.w-100 input[name='agree']"
    button_continue_xpath="//button[text()='Continue']"

    def __init__(self,driver):
        self.driver=driver

    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setPrivatePolicy(self):
        self.driver.execute_script("document.getElementsByClassName('form-check-input')[2].click()")

    def clickContinue(self):
        self.driver.execute_script("document.getElementsByClassName('btn btn-primary')[0].click()")


        

