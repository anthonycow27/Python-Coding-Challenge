import argparse

from bs4 import BeautifulSoup

from services.service_funnel.funnel_request_handler import FunnelRequestHandler
from services.service_funnel.funnel_response_handler\
    import FunnelResponseHandler


class ServiceFunnel:
    def __init__(self, **kwargs):
        self.snippet_dict = {}

    def scrape_html(self, html: str):
        """
        Scrape HTML, extract tags and snippet and
        store them in an appropriate data structure.

        Args:
            html (str) : Entire HTML content. Not the path to HTML document.
        """
        soup = BeautifulSoup(html, 'html.parser')
        snippet_dict = {}
        for snippet in soup.find_all('article'):
            data = snippet.get('data-tags')
            if data is not None:
                snippet_dict.update({data: snippet})
        self.snippet_dict = snippet_dict
        return snippet_dict

    def handle_request(self, request: dict) -> dict:
        """
        Find out the correct snippet that maps to a set of input tags.

        Args:
            request (dict): Request object as specified in the readme.
        Returns:
            response (dict): Response object as specified in the readme.
        """
        request_type = FunnelRequestHandler(
            request=request, snippet_dict=self.snippet_dict).get_request_type()

        response = FunnelResponseHandler(
            request=request,
            snippet_dict=self.snippet_dict,
            request_type=request_type).get_response()
        return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--html_path",
        help="path leading to the html file",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    with open(args.html_path, "r") as f:
        html_str = f.read()
    service_funnel = ServiceFunnel()
    service_funnel.scrape_html(html_str)
