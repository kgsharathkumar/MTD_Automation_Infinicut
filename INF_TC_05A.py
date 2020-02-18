import time
def test_save_to_database_screen(self):
    # click on name of setup to give a name for that setup
    name_of_setup = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/nameforsetup')
    name_of_setup.click()

    # Give name to the saved setup as "ABC"
    name_of_setup.send_keys("ABC")

    # Click on setup notes to write some description about saved setup
    setup_notes = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/setupnotes')
    setup_notes.click()

    # Write some description about saved setup
    setup_notes.send_keys("Works Fine All Good")

    #press Back button
    self.driver.press_keycode(4)
    #time.sleep(5)

    #Click Done button after giving setup name and setup notes
    done_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/btnDone')
    done_button.click()
    #time.sleep(5)