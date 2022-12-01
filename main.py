from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class At_Project_1:
    def __init__(self,url):
        self.url=url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

    def login_(self,username,pword):
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(username)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(pword)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(3)

    def create_user_using_PIM(self,first_name,Mid_name,last_name):
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(5) #need to implimeent expilict wait

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(5)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys(first_name)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys(Mid_name)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys(last_name)
        time.sleep(5)


        # if we need to add Create_login_details

        '''self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span').click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys(usernameNew)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys(PwordNew)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys(PwordNew)'''

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() #add click meathod to this line
        time.sleep(7)

        PageUrl=self.driver.current_url
        if PageUrl.__contains__("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/"):
            WebDriverWait(self.driver,10).until(EC.visibility_of(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6')))
            return True
        else:
            return False




    def create_user_in_Admi_Tab(self,EmployeNameNew1,UserNameNew1,PwordNew1,UserRoleStr):
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(3)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(EmployeNameNew1)

        listbox_1=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]')

        WebDriverWait(self.driver,10).until(EC.visibility_of(listbox_1))

        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(listbox_1).click().perform()


        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys(UserNameNew1)
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys(PwordNew1)
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys(PwordNew1)
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
        statusListBox=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(statusListBox))
        action.move_to_element(statusListBox)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(2)

        userRole = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')
        userRole.click()
        userRoleListBox1= self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(userRoleListBox1))

        userRoleListBox1content = self.driver.find_elements(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]/div')
        for i in userRoleListBox1content:
            print(i.text+"**")
            print(i.tag_name)
        print(len(userRoleListBox1content))


        action.move_to_element(userRoleListBox1)
        time.sleep(10)

        if (UserRoleStr == "ESS"):
          action.move_to_element(userRoleListBox1content[2]).click().perform()
          print("ESS")
        elif (UserRoleStr == "Admin"):
            action.move_to_element(userRoleListBox1content[1]).click().perform()
            print("Admin")
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click() # impliment the click action
        time.sleep(5)

    def search_using_Admin_tab(self, username, Employeename, UserRole):
        action = ActionChains(self.driver)
        time.sleep(3)

        WebDriverWait(self.driver,10).until(EC.visibility_of(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')))
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        time.sleep(2)


        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys(username)
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').click()
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').send_keys(Employeename)

        pr = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').text
        print(pr)


        EmployeenameListbox=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(EmployeenameListbox))
        time.sleep(2)
        action.move_to_element(EmployeenameListbox)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(2)

        contentsofemployeelistbox = self.driver.find_elements(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
        print(contentsofemployeelistbox)
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        userRoleList = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(userRoleList))

        userRoleListcontent = self.driver.find_elements(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div')

        for i in userRoleListcontent:
            print(i.text+"**")
            print(i.tag_name)
        print(len(userRoleListcontent))

        action.move_to_element(userRoleList)
        if UserRole == "Admin":
            action.move_to_element(userRoleListcontent[1]).click().perform()
            print("Admin")
        elif UserRole == "ESS":
            action.move_to_element(userRoleListcontent[2]).click().perform()
            print("ESS")
            time.sleep(2)


        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').click()
        statuslistbox = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]')
        WebDriverWait(self.driver,10).until(EC.visibility_of(statuslistbox))
        action.move_to_element(statuslistbox)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(2)


        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(2)

        usname = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div').text
        usrole = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div').text
        empname= self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div').text
        empstatus= self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div').text

        print(usname+","+username)
        print(usrole+","+UserRole)
        print(empname+","+Employeename)
        print(empstatus)

        if usname == username and usrole == UserRole and empname == Employeename and empstatus == "Enabled":
            return True
        else:
            return False

    def logpout_of_the_Websight(self):
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
        time.sleep(2)

        logoutlist = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul')
        WebDriverWait(self.driver,10).until(EC.visibility_of(logoutlist))
        action = ActionChains(self.driver)
        action.move_to_element(logoutlist)
        action.move_to_element(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')).click().perform()






url="https://opensource-demo.orangehrmlive.com/"
username1= "Admin"
pword_1 = "admin123"
fname = input("enter the First name: ")
mname = input("enter the Middle name: ")
lname = input("enter the Last name: ")
UserRole = input("choose the user role(Admin / ESS): ")
username = input("enter the user name: ")
Password=input("enter the password: ")
employeename =""
if mname !="" and lname !="":
    employeename= fname+" "+mname+" "+lname
elif mname =="" and lname !="":
    employeename = fname+" "+lname
elif mname !="" and lname =="":
    employeename = fname+" "+mname
elif mname == "" and lname == "":
    employeename = fname



AT1 = At_Project_1(url)
AT1.login_(username1,pword_1)
AT1.create_user_using_PIM(fname,mname,lname)
usercreation = AT1.create_user_in_Admi_Tab(employeename,username,Password,UserRole)
print(usercreation)
accountcreation = AT1.search_using_Admin_tab(username,employeename,UserRole)
print(accountcreation)
if accountcreation is True:
    AT1.logpout_of_the_Websight()
    AT1.login_(username, Password)
else:
    print("check the code for creation")


