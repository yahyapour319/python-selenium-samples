import time
from time import sleep
import pytest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestScrollByJS:
    def test_scroll_by_js_command(
        self, driver, tmp_file
    ):
        driver.get("http://play2.automationcamp.ir")
        # scroll to down of page(scrollHeight)
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        sleep(3)
        # Scroll to top of the page
        driver.execute_script("window.scrollTo(0,0)")
        sleep(5)
        assert True

    def test_scroll_to_element_which_find_by_driver(self, driver):
        driver.get("http://play2.automationcamp.ir")
        element = driver.find_element(By.XPATH, "//a[text()='here']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(5)

    # def test_scroll_to_element_find_by_driver_if_exist(self, driver):
    #     def scroll_to_find_element(locator, pixel):
    #         for i in range(0, 5):
    #             try:
    #                 driver.find_element(locator[0],locator[1])
    #                 return True
    #
    #             except:
    #                 driver.execute_script(f"window.scrollBy(0,{str(pixel)})")
    #                 sleep(0.5)
    #         return False
    #
    #     driver.get("https://www.imdb.com/chart/top/")
    #     assert not scroll_to_find_element(['link text', 'fwfwfqgeqrhr'], 1800)

    def test_scroll_horizontally(self, driver):
        driver.get("https://datatables.net/examples/basic_init/scroll_x.html")
        driver.execute_script("document.querySelector('table td:last-child').scrollIntoView()")


class TestScrollByActionChain:
    def test_scroll_by_action_chain(self, driver, actions):
        driver.get("http://play2.automationcamp.ir")
        elment1 = driver.find_element(By.XPATH, "//*[@name='message']")
        elment2 = driver.find_element(By.ID, "fname")
        actions.move_to_element(elment2).click_and_hold().move_to_element(elment1).release().perform()
        sleep(5)


class TestScrollByKeyboard:
    def test_scroll_by_keyboard(self, driver, actions):
        driver.get("http://play2.automationcamp.ir")
        html_element = driver.find_element('tag name', 'html')
        actions.send_keys_to_element(html_element, Keys.END).perform()
        time.sleep(2)
        actions.send_keys_to_element(html_element, Keys.HOME).perform()
        time.sleep(2)


class TestScrollUsingWebDriver:
    def test_scroll_to_element(self, driver):
        driver.get("http://play2.automationcamp.ir")

        element = driver.find_element(By.XPATH, "//*[text()='here']")
        element.location_once_scrolled_into_view
        sleep(3)

    @pytest.mark.parametrize('driver', ['not-maximize_window'], indirect=True)
    def test_scroll_horizontally(self, driver):
        driver.get("https://datatables.net/examples/basic_init/scroll_x.html")
        driver.set_window_size(480, 640)
        element = driver.find_element('xpath', '//tbody//td[last()]')
        sleep(1)
        element.location_once_scrolled_into_view
        sleep(3)


