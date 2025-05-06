from django.test import TestCase
from .models import Room, Building, Floors, Regions
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
from django.urls import reverse
from django.core.management import call_command

# Create your tests here.
class RoomModelTests(TestCase):
    def test_no_duplicate_floors(self):
        # Check to ensure all rooms are unique in their building
        test_building = Building(name="TESTBLD", num_floors=3, has_pit=True)
        test_building.save()

        test_room_1 = Room(building=test_building, number=1111)
        test_room_2 = Room(building=test_building, number=1111)

        test_room_1.save()

        # Should raise an IntegrityError
        try:
            test_room_2.save()
        except IntegrityError:
            caught = True
        else:
            caught = False
        
        self.assertIs(caught, True)

    def test_correct_floors(self):
        test_building = Building(name="TESTBLD", num_floors=3, has_pit=True)
        test_building.save()

        # make sure the highest floor is the second floor
        floor_list = test_building.get_floor_list()

        # top floor value should be the number of floors minus 1
        self.assertIs(floor_list[test_building.num_floors - 1][0], test_building.num_floors - 1)
    
    def test_valid_floor_number(self):
        test_building = Building(name="TESTBLD", num_floors=3, has_pit=True)
        test_building.save()

        # make a room on the third floor of a building with only 2 floors above ground
        test_third_floor_room = Room(building=test_building, number=3300)

        try:
            test_third_floor_room.save()
        except ValueError:
            caught1 = True
        else:
            caught1 = False
        
        test_building_2 = Building(name="TESTBLD2", num_floors=3, has_pit=False)
        test_building_2.save()

        # make a room in the pit of the building without a pit
        test_pit_room = Room(building=test_building_2, number=3001)

        try:
            test_pit_room.save()
        except ValueError:
            caught2 = True
        else:
            caught2 = False

        self.assertIs((caught1 and caught2), True)

# Create your tests here.
class RoomPageTest(StaticLiveServerTestCase):

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

    def test_region_filters(self):
        # Login
        self.login()

        self.driver.get(self.live_server_url + '/browse')

        # Check that we are on the browse page after login
        self.assertEqual(self.driver.current_url, self.live_server_url + "/browse/")

        # Check for presence of Region filters
        try:
            region_check = self.driver.find_element(By.ID, 'no_regions')
        except NoSuchElementException:
            # Should move to here, since there should be elements
            index = random.randint(0, 3)
            try:
                region_check = True
                random_region = Regions.values[index]
                region = self.driver.find_element(By.ID, random_region)
            except NoSuchElementException:
                region_check = False
                # fail the test
                self.assertTrue(region_check, f'no region with value {random_region}')

        region.click()

        # find the submit button
        try:
            submit = self.driver.find_element(By.ID, 'submit_filters')
        except NoSuchElementException:
            no_submit = False
            # Fail the test
            self.assertTrue(no_submit, 'no submit button')
        
        submit.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains(f'region={random_region}')
        )

        self.assertIn(f'region={random_region}', self.driver.current_url)

        # find what the correct number of rooms should be 
        total_rooms_in_region = Room.objects.filter(building__region=random_region).count()
        
        # Check if room list is present
        room_list = self.driver.find_element(By.ID, "room_list")
        room_items = room_list.find_elements(By.TAG_NAME, "li")

        # Assert that the right number of rooms shows up after filtering
        self.assertEqual(total_rooms_in_region, len(room_items), 'Expected number of rooms does not match displayed number')

    def test_building_filters(self):
        self.login()

        self.driver.get(self.live_server_url + '/browse')

        # Check that we are on the browse page after login
        self.assertEqual(self.driver.current_url, self.live_server_url + "/browse/")

        # First look for the presence of the building filters
        try:
            self.driver.find_element(By.ID, 'no_buildings')
        except NoSuchElementException:
            # Should reach here, since there should be building elements
            num_buildings = Building.objects.all().count()
            index = random.randint(0, num_buildings - 1)
            random_building_name = Building.objects.all()[index].name
            
            # Pick that building from the list
            try:
                random_building_filter = self.driver.find_element(By.ID, random_building_name)
            except NoSuchElementException:
                building_check = False
                self.assertTrue(building_check, f'no building with name {random_building_name}')
            
        # Select the building
        random_building_filter.click()

        # find the submit button
        try:
            submit = self.driver.find_element(By.ID, 'submit_filters')
        except NoSuchElementException:
            no_submit = False
            # Fail the test
            self.assertTrue(no_submit, 'no submit button')
        
        submit.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains(f'building={random_building_name}')
        )

        # Check that we reached the right url
        self.assertIn(f'building={random_building_name}', self.driver.current_url)

        total_rooms_in_building = Room.objects.filter(building__name=random_building_name).count()

        # Check if room list is present
        room_list = self.driver.find_element(By.ID, "room_list")
        room_items = room_list.find_elements(By.TAG_NAME, "li")

        # Assert that the right number of rooms shows up after filtering
        self.assertEqual(total_rooms_in_building, len(room_items), 'Expected number of rooms does not match displayed number')

