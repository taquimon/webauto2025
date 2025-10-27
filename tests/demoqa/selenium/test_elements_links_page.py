import pytest
from pages.demoqa.selenium.landing_page import LandingPage
from soft_assert import check
from soft_assert import verify

from utils.logger import get_logger

logger = get_logger(__name__)


class TestDemoQAElementsLinksPage:
    def test_elements_links_page(self, driver, env, log_test_name):
        """
        Test that the response message is displayed correctly for created link
        """

        # create the page object
        landing_page = LandingPage(driver, env)

        # click on the elements option
        elements_page = landing_page.click_elements_option()

        elements_links_page = elements_page.click_links_option()

        elements_links_page.click_created_link()

        expected_message = elements_links_page.get_response_message()

        status_message = "201 and status text Created"
        # assert that the text box page is displayed
        assert f"Link has responded with staus {status_message}" in expected_message, (
            "Wrong message response"
        )

    @pytest.mark.parametrize(
        "link, status_message",
        [
            ("created", "201 and status text Created"),
            ("no-content", "204 and status text No Content"),
            ("moved", "301 and status text Moved Permanently"),
            ("bad-request", "400 and status text Bad Request"),
            ("unauthorized", "401 and status text Unauthorized"),
            ("forbidden", "403 and status text Forbidden"),
            ("not-found", "404 and status text Not Found"),
        ],
    )
    def test_elements_links_page_2(self, driver, env, link, status_message):
        """
        Test that the response message is displayed correctly for all links
        """

        # create the page object
        landing_page = LandingPage(driver, env)

        # click on the elements option
        elements_page = landing_page.click_elements_option()

        elements_links_page = elements_page.click_links_option()

        elements_links_page.click_link_option(link)

        expected_message = elements_links_page.get_response_message()

        # assert that the text box page is displayed
        assert f"Link has responded with staus {status_message}" in expected_message, (
            "Wrong message response"
        )

    @pytest.mark.parametrize("read_data", ["links"], indirect=True)
    @pytest.mark.xfail(
        reason="Bug #11493: Incorrect status code displayed",
        strict=True,
    )
    def test_elements_links_page_3(self, driver, env, read_data, log_test_name):
        """
        Test that the response message is displayed correctly for all links
        """

        # create the page object
        landing_page = LandingPage(driver, env)

        # click on the elements option
        elements_page = landing_page.click_elements_option()

        elements_links_page = elements_page.click_links_option()

        with verify():
            for data in read_data:
                elements_links_page.click_link_option(data["link"])

                expected_message = elements_links_page.get_response_message()
                logger.info(f"Expected message: {expected_message}")
                logger.info(
                    f"Actual message: Link has responded with staus {data['status_message']}",
                )
                error_message = (
                    f"Link has responded with staus {data['status_message']}"
                )
                # assert that the text box page is displayed
                # assert f"Link has responded with staus {data['status_message']}" in expected_message, error_message
                check(
                    f"Link has responded with staus {data['status_message']}"
                    in expected_message,
                    error_message,
                )
