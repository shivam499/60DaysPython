from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebAutomation:

    def __init__(self):
        download_path = "D:\\02-Learning\\Python\\Udemy\\60DaysPython\\App15-Automation-Selenium"

        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
    def login(self, username, passweod):
        self.driver.get('https://demoqa.com/login')
        # locate username, password and login
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

        # Fill username and password
        username_field.send_keys(username)
        password_field.send_keys(passweod)
        login_button.click()
    def fill_form(self, name, email, curr_address, per_address):
        # locate elements dropdown and text box
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()
        textbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        textbox.click()
        # locate form fields
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        per_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))
        # fill the form fields

        fullname_field.send_keys(name)
        email_field.send_keys(email)
        current_address_field.send_keys(curr_address)
        per_address_field.send_keys(per_address)

        submit_button.click()

    def download(self):
        # Locate the Upload and Download section and Button
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()
        download_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'downloadButton')))
        download_button.click()
    def close(self):
        self.driver.quit()


#if __name__ == "__main__":
 #   webAutomation = WebAutomation()
  #  webAutomation.login("doe4499","John@Doe123")
   # webAutomation.fill_form("John Doe","john@gmail.com","Street 1","Street 2")
    #webAutomation.download()
    #webAutomation.close()

