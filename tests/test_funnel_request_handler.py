"""
Module testing the funtionality of Funnel request Handler
"""

import unittest

from faker import Faker

from services.service_funnel.funnel_request_handler import FunnelRequestHandler

faker = Faker()


class TestFunnelRequestHandler(unittest.TestCase):

    def test_init(self):
        """
        Test init method
        """
        request = faker.pystr()
        snippet_dict = faker.pystr()
        handler = FunnelRequestHandler(request=request,
                                       snippet_dict=snippet_dict)

        assert request == handler.request
        assert snippet_dict == handler.snippet_dict

    def test_handle_first_type_request(self):
        request = {"selected_tags": [
            {"name": "Kündigung"}, {"name": "Mobilfunkvertrag"}]}
        snippet_dict = {'Kündigung,Mobilfunkvertrag': faker.pystr()}

        handler = FunnelRequestHandler(request=request,
                                       snippet_dict=snippet_dict)
        result = handler.get_request_type()

        assert result == 0

    def test_handle_second_type_request(self):
        request = {"selected_tags": [
            {"name": "Kündigung"}, {"name": "Mobilfunkvertrag"}]}
        snippet_dict = {'Kündigung,Mobilfunkvertrag,testing': faker.pystr()}

        handler = FunnelRequestHandler(request=request,
                                       snippet_dict=snippet_dict)
        result = handler.get_request_type()

        assert result == 1

    def test_handle_third_type_request(self):
        request = {"selected_tags": [
            {"name": "Kündigung"}, {"name": "Mobilfunkvertrag"}]}
        snippet_dict = {faker.pystr(): faker.pystr()}

        handler = FunnelRequestHandler(request=request,
                                       snippet_dict=snippet_dict)
        result = handler.get_request_type()

        assert result == 2
