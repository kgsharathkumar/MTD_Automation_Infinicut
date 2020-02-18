import time
def test_casette_model_settings(self):
    model_dropdown = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='UltraGroomer']")
    model_dropdown.click()

    # select one model from dropdown box
    select_casette_model = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@index='1']")
    select_casette_model.click()
    self.driver.press_keycode(4)
    # wait for 3 seconds
    #time.sleep(3)


