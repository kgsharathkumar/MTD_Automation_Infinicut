import random
import time

from appium.webdriver.common.touch_action import TouchAction


def test_pro_rotary_deck_lift(self):
    #deck_mow_height = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/editTextDeckLiftCommandPos')
    #deck_mow_height.click()

    send_to_infinicut = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/buttonSendDeckPos')
    send_to_infinicut.click()
    time.sleep(5)



'''    for i in range(6):
        self.driver.press_keycode(67)
    deck_mow_height.click()
    self.driver.press_keycode(67)

    for i in range(2):
        deck_mow_height.send_keys(random.randrange(1,9))
'''

