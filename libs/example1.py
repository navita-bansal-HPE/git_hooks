def add_two_numbers(num1, num2):
    """
    Add two numbers and return their sum.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    # Adding two numbers
    total = num1 + num2

    # Returning the result
    return total

# Example usage
num1 = 15
num2 = 12
result = add_two_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is {result}")

"""
Clouds Detail page object model.
"""

import logging

from hpe_glcp_automation_lib.libs.commons.utils.pwright.pwright_utils import (
    PwrightUtils,
    TableUtils,
)
from hpe_pc_automation_lib.morpheus.ui.commons.navigation.nav_bar import (
    MorpheusNavigationBar,
)
from hpe_pc_automation_lib.morpheus.ui.infrastructure.locators import (
    CloudDetailsSelectors,
)
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)


class CloudsDetails:
    """
    Clouds Details page object model class.
    """

    def __init__(self, page: Page, cluster: str):
        """
        Initialize Clouds Details page under Infrastructure section.

        :param page: page.
        :param cluster: cluster url.
        """
        log.info("Initializing Clouds details page object.")
        self.page = page
        self.url = f"{cluster}/infrastructure/clouds"
        self.pw_utils = PwrightUtils(page=page)
        self.tb_utils = TableUtils(page=page)
        self.nav_bar = MorpheusNavigationBar(page=page)

    def should_have_clusters(self, cluster_name: str) -> None:
        """
        The method is used to check value of the field in cloud clusters tab.

        :param cluster_name: name of the cluster.
        """
        log.info(f"Playwright: Checking {cluster_name} in clusters tab.")
        expect(
            self.page.locator(CloudDetailsSelectors.CLOUD_CLUSTERS.format(cluster_name))
        ).to_be_visible()

    def should_have_hosts(self, host_name: str) -> None:
        """
        The method is used to check value of the field in cloud hosts tab.

        :param host_name: name of the host.
        """
        log.info(f"Playwright: Checking {host_name} in host tab.")
        expect(
            self.page.locator(CloudDetailsSelectors.CLOUD_HOSTS.format(host_name))
        ).to_be_visible()

    def should_have_vms(self, vm_name: str) -> None:
        """
        The method is used to check value of the field in cloud vms tab.

        :param vm_name: name of the vm.
        """
        log.info(f"Playwright: Checking {vm_name} in vms tab.")
        expect(
            self.page.locator(CloudDetailsSelectors.CLOUD_VMS.format(vm_name))
        ).to_be_visible()

