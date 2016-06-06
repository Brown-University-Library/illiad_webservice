# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
from . import settings_app
from django.test import Client, TestCase


class ClientV2_Test( TestCase ):
    """ Tests easyBorrow-api v2 """

    def test__check_bad_method( self ):
        """ Checks GET (api requires POST). """
        c = Client()
        response = c.get( '/v2/make_request/', {'aa': 'foo_a', 'bb': 'foo_b'} )
        self.assertEqual(
            400,
            response.status_code )
        self.assertEqual(
            'Please stop.',
            response.content )

    def test__check_bad_post_params( self ):
        """ Checks POST with bad params. """
        c = Client()
        response = c.post( '/v2/make_request/', {'aa': 'foo_a', 'bb': 'foo_b'} )
        self.assertEqual(
            400,
            response.status_code )
        self.assertEqual(
            'Please stop.',
            response.content )

    # def test__check_good_post_params__known_user( self ):
    #     """ POST with good params should submit a request and return a transaction number.
    #         This test is good, just disabled so as not to submit unnecessary real requests. """
    #     c = Client()
    #     response = c.post(
    #         '/v2/make_request/',
    #         { 'auth_key': settings_app.TEST_AUTH_KEY, 'openurl': 'foo_b', 'request_id': 'foo_c', 'username': settings_app.TEST_EXISTING_GOOD_USER }
    #         )
    #     self.assertEqual( 200, response.status_code )
    #     response_dct = json.loads( response.content )
    #     self.assertEqual( [u'status', u'transaction_number'], sorted(response_dct.keys()) )
    #     self.assertEqual( 'submission_successful', response_dct['status'] )

    # end class ClientV2_Test()
