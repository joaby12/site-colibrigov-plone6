"""Setup tests for this package."""
from kitconcept import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer
from site_plone6.testing import SITE_PLONE6_INTEGRATION_TESTING  # noqa: E501

import unittest


class TestSetup(unittest.TestCase):
    """Test that site_plone6 is properly installed."""

    layer = SITE_PLONE6_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if site_plone6 is installed."""
        self.assertTrue(self.installer.is_product_installed("site_plone6"))

    def test_browserlayer(self):
        """Test that ISITE_PLONE6Layer is registered."""
        from plone.browserlayer import utils
        from site_plone6.interfaces import ISITE_PLONE6Layer

        self.assertIn(ISITE_PLONE6Layer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("site_plone6:default")[0],
            "20220726001",
        )


class TestUninstall(unittest.TestCase):

    layer = SITE_PLONE6_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("site_plone6")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if site_plone6 is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("site_plone6"))

    def test_browserlayer_removed(self):
        """Test that ISITE_PLONE6Layer is removed."""
        from plone.browserlayer import utils
        from site_plone6.interfaces import ISITE_PLONE6Layer

        self.assertNotIn(ISITE_PLONE6Layer, utils.registered_layers())
