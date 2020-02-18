import time

from appium.webdriver.common.touch_action import TouchAction

# Move seek bar using touch action library

def test_deck_settings_screen(self):
    actions = TouchAction(self.driver)
    element2 = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/seekBarReelRegenBrake')
    # swipe(start X, start Y, end X, end Y, duration)
    self.driver.swipe(124, 669, 200, 669, 400)
    actions.tap(element2).perform()
    # After sliding seekbar a popup notification comes for the confirmation for change of data( Yes/No to update the setting)
    update_setting = self.driver.find_element_by_id('android:id/button1')
    update_setting.click()
    time.sleep(3)
