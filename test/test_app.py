from unittest import TestCase
from tornado.testing import AsyncHTTPTestCase
import mock

from tornado.web import Application
from projectname.app import start_app, MainHandler

import logging
logging.getLogger().handlers = [logging.StreamHandler()]


class TestApp(TestCase):

    @mock.patch('tornado.ioloop.IOLoop.instance')
    def test_start_app(self, ioloop_instance_mock):
        start_app()


class TestMainHandler(AsyncHTTPTestCase):

    def get_app(self):
        return Application([('/', MainHandler)])

    def test_get(self):
        response = self.fetch('/', method="GET")
        assert response.code == 200
        assert response.body == 'Hello, world'
