import hashlib
import json
import logging
import os
import os.path
import random
import string
import sys
import uuid
from pathlib import Path
from typing import Tuple

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


PROJECT_ROOT_DIR = Path(__file__).parent.parent.parent.absolute()
CONFIG_FILE = PROJECT_ROOT_DIR / "config.json"

sys.path.append(PROJECT_ROOT_DIR)
python_path = sys.executable

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def load_config():
    with open(CONFIG_FILE, "r") as f:
        config = json.loads(f.read())
    return config


@pytest.fixture(scope="package")
def config():
    return load_config()

RANDOM_STRS = set()


def random_str(length):
    while True:
        rnd = "".join(random.choices(string.ascii_lowercase, k=length))
        if rnd not in RANDOM_STRS:
            RANDOM_STRS.add(rnd)
            break
    return rnd


@pytest.fixture(scope="module")
def service():
    return Service(executable_path=ChromeDriverManager().install())


@pytest.fixture(scope="module")
def driver_with_option(request, service):
    chrome_options = Options()
    #SAMPLES request.param : (--headless, --incognito):
    for option in request.param:
        chrome_options.add_argument(option)
    _driver = webdriver.Chrome(service=service, options=chrome_options)
    _driver.implicitly_wait(5)
    _driver.maximize_window()

    yield _driver
    _driver.close()


@pytest.fixture(scope="module")
def driver(request, service):
    _driver = webdriver.Chrome(service=service)
    if not hasattr(request, 'param'):
        _driver.maximize_window()
    _driver.implicitly_wait(5)
    yield _driver
    _driver.close()


@pytest.fixture(scope='module')
def actions(driver):
    return ActionChains(driver=driver)


@pytest.fixture(scope="package")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="module")
def current_path():
    return Path(__file__).parent


@pytest.fixture(scope="function")
def tmp_file(current_path):
    file_name = os.path.join(str(current_path), f'{random_str(5)}.png')
    yield file_name
    if os.path.exists(file_name):
        os.remove(file_name)


@pytest.fixture(scope="module")
def passphrase():
    return random_str(10)


@pytest.fixture(scope="module")
def username():
    return random_str(10)

