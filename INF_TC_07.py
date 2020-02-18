import random
import time
def test_foc_value_field(self):
    # Click on editable FOC field
    foc_field_value = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/textViewFOC')
    foc_field_value.click()
    #time.sleep(5)
    # Delete the previous FOC value by pressing backspace button of android
    for i in range(4):
        self.driver.press_keycode(67)

    # Give Some value within range of 1 to 40
    foc_field_value.send_keys("4")
    #foc_field_value.send_keys(random.randrange(1, 10))
    self.driver.press_keycode(4)
    time.sleep(5)

