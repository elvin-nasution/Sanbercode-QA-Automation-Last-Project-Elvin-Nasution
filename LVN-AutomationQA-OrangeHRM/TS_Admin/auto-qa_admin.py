from os import name
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TestAdmin(unittest.TestCase):
    
    #Note!!! Wajib ganti username setiap melakukan sekali test
    name = "Kevin Mathews"
    username = "aavintest1"
    password = "admin123"

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_add_user(self):
        #inisiasi variable
       
        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        #Line Code Navigasi ke Menu Add User
        b_admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        b_user_m = driver.find_element(By.ID,"menu_admin_UserManagement")
        b_view_user = driver.find_element(By.ID,"menu_admin_viewSystemUsers")

        a = ActionChains(driver)
        a.move_to_element(b_admin).perform()
        a.move_to_element(b_user_m).perform()
        a.click(b_view_user).perform()
        time.sleep(1)

        driver.find_element(By.ID,"btnAdd").click() # klik tombol add
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_employeeName_empName").send_keys(TestAdmin.name)
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_userName").send_keys(TestAdmin.username)
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_password").send_keys(TestAdmin.password)
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_confirmPassword").send_keys(TestAdmin.password)
        time.sleep(1)

        driver.find_element(By.ID,"btnSave").click() # klik tombol save
        time.sleep(1)

        #validasi
        response_message = driver.find_element(By.TAG_NAME,'body').text
        self.assertIn('Successfully Saved', response_message)

    def test_delete_user (self):


        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        #Line Code Navigasi ke Menu Add User
        b_admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        b_user_m = driver.find_element(By.ID,"menu_admin_UserManagement")
        b_view_user = driver.find_element(By.ID,"menu_admin_viewSystemUsers")

        a = ActionChains(driver)
        a.move_to_element(b_admin).perform()
        a.move_to_element(b_user_m).perform()
        a.click(b_view_user).perform()
        time.sleep(1)

    
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys(TestAdmin.username)
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(1)
        driver.find_element(By.NAME,"chkSelectRow[]").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(1)
        
        #Tombol OK
        driver.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(1)

        #validasi
        response_message = driver.find_element(By.TAG_NAME,'body').text
        self.assertIn('Successfully Deleted', response_message)    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()