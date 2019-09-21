import unittest
from selenium_assert_registration import registration_form_check

class TestRegistration(unittest.TestCase):
    message = "Congratulations! You have successfully registered!"
    failed = "Text should be: Congratulations! You have successfully registered!"
    
    def test_first_link(self):
        self.assertEqual(registration_form_check("http://suninjuly.github.io/registration1.html"), self.message, self.failed)
        
    def test_second_link(self):
        self.assertEqual(registration_form_check("http://suninjuly.github.io/registration2.html"), self.message, self.failed)    
        
if __name__ == "__main__":
    unittest.main()