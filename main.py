import os, uuid
from time import sleep
from os.path import join, dirname
from selenium import webdriver
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# FOR RUNNING HEADLESS
# from selenium.webdriver import FirefoxOptions
# opts = FirefoxOptions()
# opts.add_argument("--headless")
# browser = webdriver.Firefox(firefox_options=opts)


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ig_username = os.environ.get("USERNAME")
ig_password = os.environ.get("PASSWORD")
ig_channel = os.environ.get("CHANNEL_URL")
azure_connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def login(self, username, password):
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(5)


class HomePage:
    def __init__(self):
        self.browser = browser

    def go_to_login_page(self):
        # self.browser.find_element_by_xpath("//a[text()='Log in']")
        sleep(2)
        return LoginPage(self.browser)


class ChannelPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(ig_channel)

    def upload_video(self):
        upload_button = browser.find_element_by_class_name('Igw0E.IwRSH.eGOV_._4EzTm.XfCBB')
        upload_button.click()

    def add_video_and_details(self):
        title_input = browser.find_element_by_css_selector("input[placeholder='Title']")
        description_input = browser.find_element_by_css_selector("textarea[placeholder='Description']")

        title_input.send_keys("Loki's Random Cat Videos")
        description_input.send_keys("I am doing cat things!")

    def download_random_cat_video(self):
        try:
            print('ABS' + __version__)
        except Exception as ex:
            print('Exception:')
            print(ex)


    def drag_and_drop_cat_video(self):
        print('Dragging and dropping the cat video')



browser = webdriver.Firefox()
browser.implicitly_wait(5)

login = LoginPage(browser)
login.login(ig_username, ig_password)
channel = ChannelPage(browser)
channel.upload_video()
channel.add_video_and_details()
# channel.download_random_cat_video()
# channel.drag_and_drop_cat_video()
# browser.close()


'''
References: 
https://stackoverflow.com/questions/43382447/python-with-selenium-drag-and-drop-from-file-system-to-webdriver
https://stackoverflow.com/questions/29381233/how-to-simulate-html5-drag-and-drop-in-selenium-webdriver
'''