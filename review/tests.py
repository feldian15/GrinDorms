from django.test import TestCase
from browse.models import Room, Building, Floors, Regions
from .models import Review, Image
from django.db.utils import IntegrityError
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
from selenium.common.exceptions import NoSuchElementException
import random
from django.core.management import call_command

# Create your tests here.
class ReviewPageTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        # Uncomment the next line to run tests headlessly (no GUI)
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

    def setUp(self):    
        # Create a test user
        self.test_username = "testuser"
        self.test_password = "testpasswordfortestuser"
        User.objects.create_user(username=self.test_username, password=self.test_password, is_active=True)

        #Set up test DB
        building_csv_path = 'Grinnell College Buildings Test Data.csv'
        room_csv_path = 'Grinnell College Dorms Test Data.csv'
        call_command('import_buildings', '--file', building_csv_path)
        call_command('import_rooms', '--file', room_csv_path)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
    
    def tearDown(self):
        self.driver.delete_all_cookies()  # Clear session between tests

    def login(self):
        # Navigate to main page
        self.driver.get(self.live_server_url)

        sign_in_link = self.driver.find_element(By.ID, "sign_in_link")
        sign_in_link.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))  # assuming 'username' is a field in the form
        )

        # Find the username and password fields and fill them in
        username_field = self.driver.find_element(By.NAME, 'username')
        password_field = self.driver.find_element(By.NAME, 'password')

        # Fill in the test user's credentials
        username_field.send_keys(self.test_username)
        password_field.send_keys(self.test_password)

        # Find and click the submit button
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        submit_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.live_server_url + "/home/")
        )

    def logout(self):
        logout_button = self.driver.find_element(By.LINK_TEXT, 'Logout')
        logout_button.click()
