"""
Module testing the functionality of funnel response handler
"""
import json
import unittest

from faker import Faker

from services.service_funnel.funnel_response_handler import FunnelResponseHandler

faker = Faker()


class TestFunnelResponseHandler(unittest.TestCase):

    def test_init(self):
        request_type = faker.pystr()
        snippet_dict = faker.pystr()
        request = faker.pystr()
        response_handler = FunnelResponseHandler(request_type=request_type,
                                                 snippet_dict=snippet_dict,
                                                 request=request)

        assert request_type == response_handler.request_type

    def test_is_type_one_respone(self):
        request_type = 0
        snippet_dict = {
            'Kündigen,Mobilfunkvertrag': '<article> You are welcome </article>'}
        request = {"selected_tags": [
            {"name": "Kündigen"}, {"name": "Mobilfunkvertrag"}]}
        response_handler = FunnelResponseHandler(request_type=request_type,
                                                 snippet_dict=snippet_dict,
                                                 request=request)
        result = response_handler.get_response()

        assert result == {
            "snippet": json.dumps('<article> You are welcome </article>'),
            "next_tags": [],
            "status": {
                "code": 0,
                "msg": "Valid tags with snippet"},
            "selected_tags": [
                {
                    "name": "Kündigen"},
                {
                    "name": "Mobilfunkvertrag"}]}

    def test_is_type_two_respone(self):
        request_type = 1
        snippet_dict = {
            'Kündigen,Mobilfunkvertrag,testing': '<article> You are welcome </article>'}
        request = {"selected_tags": [
            {"name": "Kündigen"}, {"name": "Mobilfunkvertrag"}]}
        response_handler = FunnelResponseHandler(request_type=request_type,
                                                 snippet_dict=snippet_dict,
                                                 request=request)
        result = response_handler.get_response()
        assert result == {"snippet": None,
                          "next_tags": [{'name': 'testing'}],
                          "status": {"code": 1,
                                     "msg": "Valid tags but no snippet"},
                          "selected_tags": [{"name": "Kündigen"},
                                            {"name": "Mobilfunkvertrag"}]}

    def test_is_type_three_respone(self):
        request_type = 2
        snippet_dict = {faker.pystr(): '<article> You are welcome </article>'}
        request = {"selected_tags": [
            {"name": "Kündigen"}, {"name": "Mobilfunkvertrag"}]}
        response_handler = FunnelResponseHandler(request_type=request_type,
                                                 snippet_dict=snippet_dict,
                                                 request=request)
        result = response_handler.get_response()
        assert result == {"snippet": None,
                          "next_tags": [],
                          "status": {"code": 2,
                                     "msg": "Invalid tags"},
                          "selected_tags": [{"name": "Kündigen"},
                                            {"name": "Mobilfunkvertrag"}]}
