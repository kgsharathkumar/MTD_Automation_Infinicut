import time
def test_reel_width_settings(self):
    # Click on "Reel Width" dropdown box by using its xpath
    reel_width_dropdown = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='22']")
    reel_width_dropdown.click()

    # select one value of Reel Width from dropdown box
    select_reel_width = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@index='4']")
    select_reel_width.click()

    #wait for 3 seconds
    #time.sleep(3)


def test_number_of_blades_settings(self):
    # Click on "Number of Blades" dropdown box by using its xpath
    number_of_blades_dropdown = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='11']")
    number_of_blades_dropdown.click()

    # select one value of Number of Blades from dropdown box
    select_number_of_blades = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@index='3']")
    select_number_of_blades.click()

    # wait for 3 seconds
    #time.sleep(3)


def test_infinicut_model_settings(self):
    # Click on "Infinicut Model" dropdown box by using its xpath
    infinicut_model_dropdown = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Pro Rotary Battery']")
    infinicut_model_dropdown.click()

    # select one model from dropdown box
    select_infinicut_model = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@index='3']")
    select_infinicut_model.click()

    # wait for 3 seconds
    #time.sleep(3)


