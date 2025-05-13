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

NUM_RAND_TESTS = 1

# Create your tests here.
class ReviewPageTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        # # Uncomment the next line to run tests headlessly (no GUI)
        # chrome_options.add_argument("--headless=new")
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

    def test_review_step_through(self):
        # login
        self.login()

        for i in range(1, NUM_RAND_TESTS):
            # go to review page
            self.driver.get(self.live_server_url + '/review/')

            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(self.live_server_url + "/review/")
            )

            # Ensure we are on the correct page
            self.assertEqual(self.driver.current_url, self.live_server_url + '/review/')

            # make sure that every element exists
            try:
                regions = self.driver.find_element(By.ID, 'regions')
            except NoSuchElementException:
                regions_check = False
            else:
                regions_check = True

            # make sure we found regions
            self.assertTrue(regions_check)

            try:
                buildings = self.driver.find_element(By.ID, 'buildings')
            except NoSuchElementException:
                buildings_check = False
            else:
                buildings_check = True

            # make sure we found buildings
            self.assertTrue(buildings_check)

            try:
                floors = self.driver.find_element(By.ID, 'floors')
            except NoSuchElementException:
                floors_check = False
            else:
                floors_check = True

            # make sure we found floors
            self.assertTrue(floors_check)

            try:
                rooms = self.driver.find_element(By.ID, 'rooms')
            except NoSuchElementException:
                rooms_check = False
            else:
                rooms_check = True

            # make sure we found rooms
            self.assertTrue(rooms_check)

            # Now make sure only regions is displayed
            if regions.is_displayed() and not buildings.is_displayed() and not floors.is_displayed() and not rooms.is_displayed():
                display_check = True
            else:
                display_check = False
            
            self.assertTrue(display_check)

            # Select a region:
            index = random.randint(0,3)
            rand_region = Regions.values[index]

            # try to select that region and submit
            try:
                region_choice = self.driver.find_element(By.ID, rand_region)
            except NoSuchElementException:
                region_check = False
            else:
                region_check = True

            self.assertTrue(region_check)

            region_choice.click()

            #submit
            try:
                region_submit = self.driver.find_element(By.ID, 'submit_region')
            except NoSuchElementException:
                region_check = False
            else:
                region_check = True

            self.assertTrue(region_check)

            region_submit.click()

            # wait for next page to load
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(self.live_server_url + f'/review/?region={rand_region}')
            )

            # Ensure we are on the correct page
            self.assertEqual(self.driver.current_url, self.live_server_url + f'/review/?region={rand_region}')

            # make sure that every element exists again
            try:
                regions = self.driver.find_element(By.ID, 'regions')
            except NoSuchElementException:
                regions_check = False
            else:
                regions_check = True

            # make sure we found regions
            self.assertTrue(regions_check)

            try:
                buildings = self.driver.find_element(By.ID, 'buildings')
            except NoSuchElementException:
                buildings_check = False
            else:
                buildings_check = True

            # make sure we found buildings
            self.assertTrue(buildings_check)

            try:
                floors = self.driver.find_element(By.ID, 'floors')
            except NoSuchElementException:
                floors_check = False
            else:
                floors_check = True

            # make sure we found floors
            self.assertTrue(floors_check)

            try:
                rooms = self.driver.find_element(By.ID, 'rooms')
            except NoSuchElementException:
                rooms_check = False
            else:
                rooms_check = True

            # make sure we found rooms
            self.assertTrue(rooms_check)

            # Now make sure only regions and buildings is displayed
            if regions.is_displayed() and buildings.is_displayed() and not floors.is_displayed() and not rooms.is_displayed():
                display_check = True
            else:
                display_check = False
            
            self.assertTrue(display_check)

            # Select a building:
            num_buildings = Building.objects.filter(region=rand_region).count()

            # check that the right number of building options appear
            buildings = self.driver.find_element(By.ID, 'building_list')
            buildings = buildings.find_elements(By.TAG_NAME, 'option')

            self.assertEqual(num_buildings, len(buildings), 'incorrect number of building options')

            # Pick a random one
            index = random.randint(0,num_buildings - 1)
            rand_building = Building.objects.filter(region=rand_region)[index].name

            # try to select that region and submit
            try:
                building_choice = self.driver.find_element(By.ID, rand_building)
            except NoSuchElementException:
                building_check = False
            else:
                building_check = True

            self.assertTrue(building_check)

            building_choice.click()

            #submit
            try:
                building_submit = self.driver.find_element(By.ID, 'submit_building')
            except NoSuchElementException:
                building_check = False
            else:
                building_check = True

            self.assertTrue(building_check)

            building_submit.click()

            # wait for next page to load
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(self.live_server_url + f'/review/?region={rand_region}&building={rand_building}')
            )

            # Ensure we are on the correct page
            self.assertEqual(self.driver.current_url, self.live_server_url + f'/review/?region={rand_region}&building={rand_building}')

            # make sure that every element exists again
            try:
                regions = self.driver.find_element(By.ID, 'regions')
            except NoSuchElementException:
                regions_check = False
            else:
                regions_check = True

            # make sure we found regions
            self.assertTrue(regions_check)

            try:
                buildings = self.driver.find_element(By.ID, 'buildings')
            except NoSuchElementException:
                buildings_check = False
            else:
                buildings_check = True

            # make sure we found buildings
            self.assertTrue(buildings_check)

            try:
                floors = self.driver.find_element(By.ID, 'floors')
            except NoSuchElementException:
                floors_check = False
            else:
                floors_check = True

            # make sure we found floors
            self.assertTrue(floors_check)

            try:
                rooms = self.driver.find_element(By.ID, 'rooms')
            except NoSuchElementException:
                rooms_check = False
            else:
                rooms_check = True

            # make sure we found rooms
            self.assertTrue(rooms_check)

            # Now make sure only regions and buildings and floors is displayed
            if regions.is_displayed() and buildings.is_displayed() and floors.is_displayed() and not rooms.is_displayed():
                display_check = True
            else:
                display_check = False
            
            self.assertTrue(display_check)

            # Select a building:
            num_floors = Building.objects.get(name=rand_building).num_floors

            # check that the right number of floor options appear
            floors = self.driver.find_element(By.ID, 'floor_list')
            floor_options = floors.find_elements(By.TAG_NAME, 'option')

            self.assertEqual(num_floors, len(floor_options), 'incorrect number of floor options')

            # Make sure the pit is or is not displayed
            try:
                floors.find_element(By.ID, "0")
            except NoSuchElementException:
                pit = False
            else:
                pit = True
            
            self.assertEqual(pit, Building.objects.get(name=rand_building).has_pit, 'incorrect pit display')

            # Pick a random floor
            index = random.randint(0,num_floors - 1)
            rand_floor = Building.objects.get(name=rand_building).get_floor_list()[index][0]

            # try to select that floor and submit
            try:
                floor_choice = self.driver.find_element(By.ID, rand_floor)
            except NoSuchElementException:
                floor_check = False
            else:
                floor_check = True

            self.assertTrue(floor_check)

            floor_choice.click()

            #submit
            try:
                floor_submit = self.driver.find_element(By.ID, 'submit_floors')
            except NoSuchElementException:
                floor_check = False
            else:
                floor_check = True

            self.assertTrue(floor_check)

            floor_submit.click()

            # wait for next page to load
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(f'floor={rand_floor}')
            )

            # Ensure we are on the correct page
            self.assertIn(f'region={rand_region}', self.driver.current_url)
            self.assertIn(f'building={rand_building}', self.driver.current_url)
            self.assertIn(f'floor={rand_floor}', self.driver.current_url)

            # make sure that every element exists again
            try:
                regions = self.driver.find_element(By.ID, 'regions')
            except NoSuchElementException:
                regions_check = False
            else:
                regions_check = True

            # make sure we found regions
            self.assertTrue(regions_check)

            try:
                buildings = self.driver.find_element(By.ID, 'buildings')
            except NoSuchElementException:
                buildings_check = False
            else:
                buildings_check = True

            # make sure we found buildings
            self.assertTrue(buildings_check)

            try:
                floors = self.driver.find_element(By.ID, 'floors')
            except NoSuchElementException:
                floors_check = False
            else:
                floors_check = True

            # make sure we found floors
            self.assertTrue(floors_check)

            try:
                rooms = self.driver.find_element(By.ID, 'rooms')
            except NoSuchElementException:
                rooms_check = False
            else:
                rooms_check = True

            # make sure we found rooms
            self.assertTrue(rooms_check)

            # Now make sure all the dropdowns are displayed
            if regions.is_displayed() and buildings.is_displayed() and floors.is_displayed() and rooms.is_displayed():
                display_check = True
            else:
                display_check = False
            
            self.assertTrue(display_check)

            # Select a room:
            num_rooms = Room.objects.filter(building__name=rand_building, floor=rand_floor).count()

            # Error handle, since these floors have no rooms
            if (rand_building == "MAIN" or rand_building == "RENFROW") and rand_floor == 1:
                num_rooms = 1
                skip = True
            else:
                skip = False

            # check that the right number of room options appear
            rooms = self.driver.find_element(By.ID, 'room_list')
            room_options = rooms.find_elements(By.TAG_NAME, 'option')

            self.assertEqual(num_rooms, len(room_options), 'incorrect number of room options')

            if not skip:
                # Pick a random room
                index = random.randint(0,num_rooms - 1)
                rand_room = Room.objects.filter(building__name=rand_building, floor=rand_floor)[index].number

                # try to select that region and submit
                try:
                    room_choice = self.driver.find_element(By.ID, rand_room)
                except NoSuchElementException:
                    room_check = False
                else:
                    room_check = True

                self.assertTrue(room_check)

                room_choice.click()

                #submit
                try:
                    room_submit = self.driver.find_element(By.ID, 'submit_rooms')
                except NoSuchElementException:
                    room_check = False
                else:
                    room_check = True

                self.assertTrue(room_check)

                room_submit.click()

                # wait for next page to load
                WebDriverWait(self.driver, 10).until(
                    EC.url_contains(f'room={rand_room}')
                )

                # Ensure we are on the correct page
                self.assertIn(f'region={rand_region}', self.driver.current_url)
                self.assertIn(f'building={rand_building}', self.driver.current_url)
                self.assertIn(f'floor={rand_floor}', self.driver.current_url)
                self.assertIn(f'room={rand_room}', self.driver.current_url)

                # Now check that the review form displays
                try:
                    review_form = self.driver.find_element(By.ID, 'review')
                except NoSuchElementException:
                    review_check = False
                else:
                    review_check = True

                self.assertTrue(review_check)
                self.assertTrue(review_form.is_displayed())
            
    def test_full_usage(self):
        # login
        self.login()

        # navigate to the review page
        self.driver.get(self.live_server_url + '/review/')

        WebDriverWait(self.driver, 10).until(
                EC.url_to_be(self.live_server_url + "/review/")
        )

        # Now pick a random region
        index = random.randint(0,3)
        rand_region = Regions.values[index]

        # try to select that region and submit
        try:
            region_choice = self.driver.find_element(By.ID, rand_region)
        except NoSuchElementException:
            region_check = False
        else:
            region_check = True

        self.assertTrue(region_check)

        region_choice.click()

        #submit
        try:
            region_submit = self.driver.find_element(By.ID, 'submit_region')
        except NoSuchElementException:
            region_check = False
        else:
            region_check = True

        self.assertTrue(region_check)

        region_submit.click()

        # wait for next page to load
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.live_server_url + f'/review/?region={rand_region}')
        )

        self.assertIn(f'region={rand_region}', self.driver.current_url)

        # Pick a random building
        num_buildings = Building.objects.filter(region=rand_region).count()
        index = random.randint(0,num_buildings - 1)
        rand_building = Building.objects.filter(region=rand_region)[index].name

        # try to select that region and submit
        try:
            building_choice = self.driver.find_element(By.ID, rand_building)
        except NoSuchElementException:
            building_check = False
        else:
            building_check = True

        self.assertTrue(building_check)

        building_choice.click()

        #submit
        try:
            building_submit = self.driver.find_element(By.ID, 'submit_building')
        except NoSuchElementException:
            building_check = False
        else:
            building_check = True

        self.assertTrue(building_check)

        building_submit.click()

        # wait for next page to load
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.live_server_url + f'/review/?region={rand_region}&building={rand_building}')
        )

        # Ensure we are on the correct page
        self.assertEqual(self.driver.current_url, self.live_server_url + f'/review/?region={rand_region}&building={rand_building}')

        # pick a random floor
        num_floors = Building.objects.get(name=rand_building).num_floors
        index = random.randint(0,num_floors - 1)
        rand_floor = Building.objects.get(name=rand_building).get_floor_list()[index][0]

        # use a different floor in these cases, since there are no rooms on 1
        if (rand_building == 'MAIN' or rand_building == 'RENFROW') and rand_floor == 1:
            index = random.randint(1,num_floors - 1)
            rand_floor = Building.objects.get(name=rand_building).get_floor_list()[index][0]

        # try to select that floor and submit
        try:
            floor_choice = self.driver.find_element(By.ID, rand_floor)
        except NoSuchElementException:
            floor_check = False
        else:
            floor_check = True

        self.assertTrue(floor_check)

        floor_choice.click()

        #submit
        try:
            floor_submit = self.driver.find_element(By.ID, 'submit_floors')
        except NoSuchElementException:
            floor_check = False
        else:
            floor_check = True

        self.assertTrue(floor_check)

        floor_submit.click()

        # wait for next page to load
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(f'floor={rand_floor}')
        )

        # Ensure we are on the correct page
        self.assertIn(f'region={rand_region}', self.driver.current_url)
        self.assertIn(f'building={rand_building}', self.driver.current_url)
        self.assertIn(f'floor={rand_floor}', self.driver.current_url)

        # pick a random room
        num_rooms = Room.objects.filter(building__name=rand_building, floor=rand_floor).count()

        index = random.randint(0,num_rooms - 1)
        rand_room = Room.objects.filter(building__name=rand_building, floor=rand_floor)[index].number

        # try to select that region and submit
        try:
            room_choice = self.driver.find_element(By.ID, rand_room)
        except NoSuchElementException:
            room_check = False
        else:
            room_check = True

        self.assertTrue(room_check)

        room_choice.click()

        #submit
        try:
            room_submit = self.driver.find_element(By.ID, 'submit_rooms')
        except NoSuchElementException:
            room_check = False
        else:
            room_check = True

        self.assertTrue(room_check)

        room_submit.click()

        # wait for next page to load
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(f'room={rand_room}')
        )

        # Ensure we are on the correct page
        self.assertIn(f'region={rand_region}', self.driver.current_url)
        self.assertIn(f'building={rand_building}', self.driver.current_url)
        self.assertIn(f'floor={rand_floor}', self.driver.current_url)
        self.assertIn(f'room={rand_room}', self.driver.current_url)

        # Now leave the review
        index = random.randint(1,5)
        rand_rating = f'1star{index}'

        try:
            star = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{rand_rating}']")
        except NoSuchElementException:
            star_check = False
        else:
            star_check = True
        
        self.assertTrue(star_check)

        star.click()



