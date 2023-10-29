import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options


capabilities = dict(
    platformName="Android",
    platformVersion="10",
    automationName="uiautomator2",
    deviceName="CFM7N18925001740",
    appPackage="com.tencent.wework",
    appActivity="com.tencent.wework.launch.LaunchSplashActivity",
    noReset=True,
    newCommandTimeout=60000,
    waitforTimeout=60000,
)

appium_server_url = "http://localhost:4723"

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver: webdriver.Remote = webdriver.Remote(
            command_executor=appium_server_url, options=capabilities_options
        )
        self.driver.activate_app("com.tencent.wework")

    def test_wxwork(self) -> None:
        wxwork = WxWork(self.driver)
        wxwork.run()

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()


class WxWork:
    def __init__(self, driver: webdriver.Remote) -> None:
        self.driver = driver

    def run(self):
        self.clickHomeAddBtn()
        self.search()
        self.clickSearchResult()
        self.clickAddUser()
        self.clickSendInvite()

    def keyboard(self):
        self.driver.press_keycode(66)
        self.driver.press_keycode(66)

    def clickHomeAddBtn(self):
        time.sleep(2)
        el = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@resource-id="com.tencent.wework:id/lye"]',
        )
        el.click()

        el = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.ListView[@resource-id="com.tencent.wework:id/dk7"]/android.widget.RelativeLayout[2]',
        )
        el.click()

        el = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.FrameLayout[@resource-id="com.tencent.wework:id/k69"]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout',
        )
        el.click()

    def search(self):
        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.EditText[@resource-id="com.tencent.wework:id/k5l"]',
        )
        # el.click()

        # el.clear()
        el.send_keys("")
        self.keyboard()

    def clickSearchResult(self):
        time.sleep(5)
        el = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@resource-id="com.tencent.wework:id/jn"]',
        )
        el.click()

    def clickAddUser(self):
        el = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@resource-id="com.tencent.wework:id/el4"]',
        )
        el.click()

    def clickSendInvite(self):
        el = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@resource-id="com.tencent.wework:id/el4"]',
        )
        el.click()


if __name__ == "__main__":
    unittest.main()
