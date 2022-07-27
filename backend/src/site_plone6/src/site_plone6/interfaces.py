"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ISITE_PLONE6Layer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
