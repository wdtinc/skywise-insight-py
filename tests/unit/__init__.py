import requests_mock
from unittest import TestCase

from skywiseinsight import InsightResource


class InsightTest(TestCase):

    def setUp(self):
        InsightResource.set_site('http://my.skywise.host')
        InsightResource.set_user('my-skywise-user')
        InsightResource.set_password('my-skywise-password')
        InsightResource.set_use_session_for_async(True)

        self.adapter = requests_mock.Adapter()
        session = InsightResource.get_session()
        session.mount('http://my.skywise.host', self.adapter)
