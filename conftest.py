from datetime import datetime
from pathlib import Path

import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl = "https://www.saucedemo.com"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("reports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime("%Y%m%d%H%M")}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title="Test report - sample application"
