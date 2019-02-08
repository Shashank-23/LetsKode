import pytest
from Utilities.framework_Utility import framework_Utility

#################################################### LOCATORS #########################################################
byLoc_linklogin = "link_text"
locVal_linklogin = "Login"

byLoc_txtEmail = "name"
locVal_txtEmail = "user[email]"

byLoc_txtPassword = "id"
locVal_txtPassword = "user_password"

byLoc_btnLogin = "name"
locVal_btnLogin = "commit"

################################################## //LOCATORS #########################################################



class loginPage(framework_Utility):

    def __init__(self,driver):
        super().__init__(driver)

################################################### FUNCTIONS #########################################################

    #*********************************** Click_FUNCTIONS **************************************************#
    def clickLinkLogin(self):
        self.clickElement(byLoc_linklogin,locVal_linklogin)
        self.waitforXseconds(20)

    def clickBtnLogin(self):
        self.clickElement(byLoc_btnLogin,locVal_btnLogin)

    # *********************************** //Click_FUNCTIONS ***********************************************#


    #*********************************** EntetText_FUNCTIONS **********************************************#

    def enterEmail(self,email):
        self.enterValue(byLoc_txtEmail,locVal_txtEmail,email)

    def enterPassword(self,password):
        self.enterValue(byLoc_txtPassword,locVal_txtPassword,password)

    # *********************************** //EntetText_FUNCTIONS *******************************************#

################################################# //FUNCTIONS #########################################################
