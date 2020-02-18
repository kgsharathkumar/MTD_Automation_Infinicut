import time

from appium.webdriver.common.touch_action import TouchAction


def test_dashboard_screen(self):
    actions = TouchAction(self.driver)
    # Move Max walking speed seekbar to certain value and observe change in foc value
    element2 = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/seekBarMaxWalkingSpeed')
    self.driver.swipe(188, 1810, 800, 1810, 400)
    actions.tap(element2).perform()

    # Select Moisture Type
    moisture_select = self.driver.find_element_by_id('android:id/text1')
    moisture_select.click()

    # Select low moisture
    low_moisture = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Low' and @index='2']")
    low_moisture.click()

    # Click on moisture adjust button and observe change in foc value
    moisture_adjust = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/moisture_adj')
    moisture_adjust.click()
    time.sleep(2)


    moisture_select.click()
    # Select high moisture
    high_moisture = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='High' and @index='3']")
    high_moisture.click()
    # Click on moisture adjust button and observe change in foc value
    moisture_adjust.click()
    time.sleep(2)

    moisture_select.click()
    # Select medium moisture
    medium_moisture = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Medium' and @index='1']")
    medium_moisture.click()
    # Click on moisture adjust button and observe there is no change in foc value
    moisture_adjust.click()
    time.sleep(5)
