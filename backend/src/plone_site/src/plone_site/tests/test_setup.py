"""Setup tests for this package."""
from kitconcept import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone_site.testing import PLONE_SITE_INTEGRATION_TESTING  # noqa: E501
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone_site is properly installed."""

    layer = PLONE_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if plone_site is installed."""
        self.assertTrue(self.installer.is_product_installed("plone_site"))

    def test_browserlayer(self):
        """Test that IPLONE_SITELayer is registered."""
        from plone.browserlayer import utils
        from plone_site.interfaces import IPLONE_SITELayer

        self.assertIn(IPLONE_SITELayer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("plone_site:default")[0],
            "20220716001",
        )


class TestUninstall(unittest.TestCase):

    layer = PLONE_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("plone_site")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone_site is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("plone_site"))

    def test_browserlayer_removed(self):
        """Test that IPLONE_SITELayer is removed."""
        from plone.browserlayer import utils
        from plone_site.interfaces import IPLONE_SITELayer

        self.assertNotIn(IPLONE_SITELayer, utils.registered_layers())
