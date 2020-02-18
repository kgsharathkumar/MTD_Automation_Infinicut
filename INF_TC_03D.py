import time
def test_infinicut_model_settings(self):
    # Click on "Infinicut Model" dropdown box by using its xpath
    infinicut_model_dropdown = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Pro Rotary Battery']")
    infinicut_model_dropdown.click()

    # select one model from dropdown box
    select_infinicut_model = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@index='1']")
    select_infinicut_model.click()

    # wait for 3 seconds
    #time.sleep(3)


