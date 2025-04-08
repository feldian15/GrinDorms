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
        chrome_options.add_argument("--headless")  # run without opening a window
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
        self.assertEqual("GrinDorms", title)

        # Check for the presence of the browse link:
        browse_link = self.driver.find_element(By.ID, "browse_link")
        self.assertIs(browse_link.is_displayed(), True)

        # Check that the browse link navigates correctly
        browse_link.click()
        self.assertEqual(self.driver.current_url, self.live_server_url + "/browse/")

        # Go back to the homepage for the next test
        self.driver.get(self.live_server_url + "/home/")

        # Check that the review link is displayed on the page
        review_link = self.driver.find_element(By.ID, "review_link")
        self.assertIs(review_link.is_displayed(), True)

        # check that the review link navigates to the correct location
        review_link.click()
        self.assertEqual(self.driver.current_url, self.live_server_url + "/review/")

        # Go back to the homepage for the next test
        self.driver.get(self.live_server_url + "/home/")

        # Check that the my reviews link is displayed on the page
        my_reviews_link = self.driver.find_element(By.ID, "my_reviews_link")
        self.assertIs(my_reviews_link.is_displayed(), True)

        # check that the my reviews link navigates to the correct location
        my_reviews_link.click()
        self.assertEqual(self.driver.current_url, self.live_server_url + "/review/my_reviews/")

