import os.path
import pytest

# @pytest.mark.parametrize('driver_with_option', [("--incognito","--headless")], indirect=True)
def test_take_screen_shot(
    driver, tmp_file
):
    driver.get("http://play2.automationcamp.ir")
    # driver.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot(tmp_file)
    assert os.path.exists(tmp_file)
