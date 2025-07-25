import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import unittest
from unittest.mock import patch, MagicMock

import nuvolo_xdome as nx


class TestNuvoloClient(unittest.TestCase):
    def test_url_building(self):
        client = nx.NuvoloCMMSClient("https://nuvolo.example.com", "u", "p")
        url = client._url("table", "id")
        self.assertEqual(url, "https://nuvolo.example.com/api/now/table/table/id")

    @patch("nuvolo_xdome.clients.requests.Session")
    def test_search_assets(self, session_cls):
        session = session_cls.return_value
        session.get.return_value.json.return_value = {"result": [1]}
        session.get.return_value.raise_for_status = lambda: None

        client = nx.NuvoloCMMSClient("https://n.com", "u", "p")
        result = client.search_assets("t")
        self.assertEqual(result, [1])
        session.get.assert_called()


class TestXDomeClient(unittest.TestCase):
    @patch("nuvolo_xdome.clients.requests.Session")
    def test_headers_added(self, session_cls):
        session = session_cls.return_value
        client = nx.ClarotyXDomeClient("https://x.com", "KEY")
        session.headers.update.assert_any_call({
            "Authorization": "Bearer KEY",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    @patch("nuvolo_xdome.clients.requests.Session")
    def test_search_assets(self, session_cls):
        session = session_cls.return_value
        session.request.return_value.json.return_value = [1]
        session.request.return_value.raise_for_status = lambda: None

        client = nx.ClarotyXDomeClient("https://x.com", "KEY")
        result = client.search_assets()
        self.assertEqual(result, [1])
        session.request.assert_called_with("get", "https://x.com/assets", params={})


if __name__ == "__main__":
    unittest.main()
