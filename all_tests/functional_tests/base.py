import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10



class FunctionalTest(StaticLiveServerTestCase):



    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        self.tests_passed = 0
        self.tests_failed = 0
        self.tests_passed_list = []
        self.tests_failed_list = []

    def tearDown(self):
        
        if self.tests_failed == 0:
            print("\n100! Great Job!\n")
            print("Here are your Tests Passed")
            for msg in self.tests_passed_list:
                print(msg)
        elif self.tests_passed > 0:
            print("\n{} tests passed.\n".format(self.tests_passed))
            print("\n{} tests failed.\n".format(self.tests_failed))

            the_sum = self.tests_passed + self.tests_failed
            score = float(self.tests_passed  ) / the_sum
            print("\nYou got a {}.".format(score))

        self.browser.quit()

    def check_text_in_page(self, text):
        start_time = time.time()
        MAX_WAIT = 10
        while True:
            try:
                page_text = self.browser.find_element_by_tag_name('body').text.lower()
                self.assertIn(text, page_text)
                self.tests_passed += 1
                self.tests_passed_list.append('{} found in website!'.format(text))
                # time.sleep(4.5)
                return
            except Exception as e:
                if time.time() - start_time > MAX_WAIT:
                    self.tests_failed += 1
                    self.tests_failed_list.append('{} not found in website with error {}!'.format(text, e))
                    raise e
                time.sleep(0.5)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        MAX_WAIT = 10
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()  
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)