from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #  New online to-do app. Check out its homepage:
        self.browser.get('http://localhost:8000')
        #  User will notice page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # User will be invited straight-away to enter the first to-do item.

        #  user Edith is a fly-fisherwoman and types 'Buy Peacock Feathers' into a text box.

        #  When she hits enter, the page updates, the page lists:
        #  " #1.  Buy Peacock Feathers"  as an item in a to-do list.

        #  There remains a text box that can be easily used to input another to-do item in the list.
        #  She enters 'use peacock feathers to make a fly'

        #  Page updates again, shows both items in ordered list:
        #  # 1. Buy Peacock Feathers
        #  # 2. Use Peacock Feathers to Make a Fly  <-- title cased

        #  concerned the list will not be remembered -- site generates a unique URL for edith. Site explains it
        #  will be retained for future use.  User can rest easy --- and retain access to list.

    #  !-- Always test from the POV of the user, and make sure the story is coherent.


if __name__ == '__main__':
    unittest.main()
