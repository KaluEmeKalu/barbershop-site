from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

class NewVisitorTest(FunctionalTest):

    def get_input_by_name(self, name):
        self.browser.get(self.live_server_url)
        inputs = self.browser.find_elements_by_tag_name('input')
        
        for the_input in inputs:
            if the_input.get_attribute("name") == name:
                return the_input
        raise Exception("No input element with name == {}".format(name))


    def can_make_appointment(self):
        # Edith stsarts a new to-do list
        self.browser.get(self.live_server_url)
        try:
            inputbox = self.get_input_by_name('time')
        except Exception as e:
            msg = "\nfailed can make appointment test with error {}.\n".format(e)
            self.tests_failed += 1
            self.tests_failed_list.append(msg)
            return
        inputbox.send_keys("3:30pm")
        inputbox.send_keys(Keys.ENTER)
        self.check_text_in_page("3:30pm")

    def contains_restaurant_intro(self):
        text = "Amazing Amy's barbershop".lower()
        self.check_text_in_page(text)
        

            
    def get_images_for_200_response(self):
        self.browser.get(self.live_server_url)
        example_images = self.browser.find_elements_by_tag_name('img')
        picture_count = 0
        for image in example_images:
            current_link = image.get_attribute("src")
            r = requests.get(current_link)
            try: 
                self.assertEqual(r.status_code, 200)
                picture_count += 1
                print("\nFound {} pictures!\n".format(picture_count))
            except AssertionError as e:
                self.verificationErrors.append(current_link + ' delivered response code of ' + r.status_code)
        return picture_count


    def has_at_least_three_pictures(self):
        picture_count = self.get_images_for_200_response()
        if picture_count >= 3:
            msg = "{} pictures found! Test passed!".format(picture_count)
            self.tests_passed += 1
            self.tests_passed_list.append(msg)
        else:
            msg = "Sorry. You did not pass this test. Only {} pictures found.".format(picture_count)
            self.tests_failed += 1
            self.tests_failed_list.append(msg)


    def test_main(self):
        self.has_at_least_three_pictures()
        self.can_make_appointment()
        self.contains_restaurant_intro()











        # # She notices that her list has a unique URL
        # edith_list_url = self.browser.current_url
        # self.assertRegex(edith_list_url, 'lists/.+')

        # # Now a new user, Francis comes along to the site.

        # ## We use a new browser session to make sure that no information
        # ## of Edith's is coming through from cookies etc
        # self.browser.quit()
        # self.browser = webdriver.Firefox()

        # # Francis visits the home page. There is no sign of Edith's 
        # # list
        # self.browser.get(self.live_server_url)
        # page_text = self.browser.find_element_by_tag_name('body').text
        # self.assertNotIn("Buy peacock feathers", page_text)
        # self.assertNotIn("make a fly", page_text)

        # # Francis starts a new list by entering a new item.
        # inputbox = self.browser.find_element_by_id("id_new_item")
        # inputbox.send_keys("Buy milk")
        # inputbox.send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table("1: Buy milk")

        # # Francis gets his own unique URL
        # francis_list_url = self.browser.current_url
        # self.assertRegex(francis_list_url, '/lists/.+')
        # self.assertNotEqual(francis_list_url, edith_list_url)

        # # Again, there is no trace of Edith's list
        # page_text = self.browser.find_element_by_tag_name('body').text
        # self.assertNotIn("Buy peacock feathers", page_text)
        # self.assertNotIn("make a fly", page_text)

        # # Satisfied, they both go back to sleep.        




















