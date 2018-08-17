import unittest
from pyramid import testing
from tz_pyramid.ui.views.RESTView import RESTView

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'tz_pyramid')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from tz_pyramid import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)

    def test_root2(self):
        rest = RESTView('/')
        rest.get()

