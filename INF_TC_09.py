import random
import time
# Click on editable HOC field value
def test_hoc_field_value(self):
    hoc_value = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/hocvalue')
    hoc_value.click()
    time.sleep(5)
# Delete the previous value of HOC using android backspace button
    for i in range(3):
        self.driver.press_keycode(67)
    hoc_value.send_keys("4")
    #hoc_value.send_keys(random.randrange(1, 10))
    # Click on Calculate Button using its resource id
    calculate_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/foccalc')
    calculate_button.click()
    #time.sleep(5)
    # Click on return button using its resource id
    # On clicking return button will go back to the main Dashboard
    return_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/return_back')
    return_button.click()

    time.sleep(5)