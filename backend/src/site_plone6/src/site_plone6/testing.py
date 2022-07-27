from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import site_plone6


class SITE_PLONE6Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=site_plone6)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "site_plone6:default")
        applyProfile(portal, "site_plone6:initial")


SITE_PLONE6_FIXTURE = SITE_PLONE6Layer()


SITE_PLONE6_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SITE_PLONE6_FIXTURE,),
    name="SITE_PLONE6Layer:IntegrationTesting",
)


SITE_PLONE6_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SITE_PLONE6_FIXTURE, WSGI_SERVER_FIXTURE),
    name="SITE_PLONE6Layer:FunctionalTesting",
)


SITE_PLONE6ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SITE_PLONE6_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="SITE_PLONE6Layer:AcceptanceTesting",
)
