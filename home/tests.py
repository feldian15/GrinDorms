from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create your tests here.
class HomePageTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        #chrome_options.add_argument("--headless")  # run without opening a window
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
    
    def test_homepage(self):
        # Go to the website
        self.driver.get(self.live_server_url + '/home/')

        # Wait until the page title is not empty (max 5 seconds)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.title != ""
        )

        # Check that we are on the right page
        title = self.driver.title
        self.assertIn("GrinDorms", title)

        # Check for the presence of the browse link:
        browse_link = self.driver.find_element(By.ID, "browse_link")
        self.assertIs(browse_link.is_displayed(), True)

        # Check that the browse link navigates correctly
        browse_link.click()
        self.assertEqual(self.driver.current_url, self.live_server_url + "/browse/")
