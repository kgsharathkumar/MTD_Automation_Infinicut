import time
from appium.webdriver.common.touch_action import TouchAction


def test_save_to_infinicut(self):
    # Scroll down the page
    actions = TouchAction(self.driver)
    element = self.driver.find_element_by_class_name('android.widget.ScrollView')
    self.driver.swipe(475, 500, 475, 200, 400)
    actions.tap(element).perform()

    # Screen stays for 5 seconds
    #time.sleep(5)

    # Click on "Save to Ifinicut" button by using it's resource id
    # On clicking that Changes made in settings all saved in app
    save_to_infinicut_Button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/save_to_infinicut')
    save_to_infinicut_Button.click()

    # Screen stays for 5 seconds
    #time.sleep(3)

    # On clicking "Save to Infinicut" button we get pop message with note that "your Settings are saved"
    # And we have to click "OK" using its resource id
    ok_popup_msg_button = self.driver.find_element_by_id('android:id/button1')
    ok_popup_msg_button.click()

