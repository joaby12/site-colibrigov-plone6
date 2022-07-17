from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import plone_site


class PLONE_SITELayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plone_site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone_site:default")
        applyProfile(portal, "plone_site:initial")


PLONE_SITE_FIXTURE = PLONE_SITELayer()


PLONE_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_SITE_FIXTURE,),
    name="PLONE_SITELayer:IntegrationTesting",
)


PLONE_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_SITE_FIXTURE, WSGI_SERVER_FIXTURE),
    name="PLONE_SITELayer:FunctionalTesting",
)


PLONE_SITEACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="PLONE_SITELayer:AcceptanceTesting",
)
