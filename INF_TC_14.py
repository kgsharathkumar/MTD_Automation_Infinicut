import time

from appium.webdriver.common.touch_action import TouchAction

# By moving traction acc and traction brake seekbar give value to them and get yes or no popup action to update the value
def test_drive_settings_screen(self):

    actions = TouchAction(self.driver)
    element2 = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/seekBarTractionAcc')
    self.driver.swipe(124, 669, 300, 669, 400)
    actions.tap(element2).perform()
    update_setting = self.driver.find_element_by_id('android:id/button1')
    update_setting.click()
    time.sleep(2)

    actions = TouchAction(self.driver)
    element2 = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/seekBarTractionBrake')
    self.driver.swipe(124, 1098, 300, 1098, 400)
    actions.tap(element2).perform()
    update_setting = self.driver.find_element_by_id('android:id/button1')
    update_setting.click()
    time.sleep(2)


'''
    get_seekbar = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/seekBarTractionBrake')
    start = get_seekbar.location.get('x')
    print(start)
    ycd = get_seekbar.location.get('y')
    print(ycd)

   
    Deck_Mow_Height = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/editTextDeckLiftCommandPos')
    Deck_Mow_Height.click()
    for i in range(6):
        self.driver.press_keycode(67)
    time.sleep(5)
    #Deck_Mow_Height.send_keys(random.randrange(15,50))
    #SendToInfinicut = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/buttonSendDeckPos')
    #SendToInfinicut.click()
'''
'''   get_seekbar = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/seekBarReelRegenBrake')
    start = get_seekbar.location.get('x')
    print(start)
    ycd = get_seekbar.location.get('y')
    print(ycd)
'''