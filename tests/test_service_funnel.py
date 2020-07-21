"""
Module testing the funtionality of Service Funnel
"""
import unittest
from unittest.mock import patch

from faker import Faker

from main import ServiceFunnel

from tests.factory.html_text import HTMLText

faker = Faker


class TestServiceFunnel(unittest.TestCase):

    def test_scrape_html(self):
        html_text_class = HTMLText()
        text_input = html_text_class.get_string()

        service_funnel = ServiceFunnel()
        result = service_funnel.scrape_html(text_input)
        assert isinstance(result, dict)
        assert len(result) > 1

    @patch('main.FunnelRequestHandler')
    @patch('main.FunnelResponseHandler')
    def test_handle_request(self, mock_response_class, mock_request_class):
        request = {"selected_tags": [
            {"name": "Kündigung"}, {"name": "Mobilfunkvertrag"}]}
        service_funnel = ServiceFunnel()
        service_funnel.handle_request(request)

        mock_request_class.return_value.get_request_type.assert_called_once()
        mock_response_class.return_value.get_response.assert_called_once()
