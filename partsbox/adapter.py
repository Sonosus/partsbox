import requests
import requests.packages
from typing import List, Dict


class Adapter:
    def __init__(self, api_key: str, ssl_verify: bool = True) -> None:
        self.url = "https://api.partsbox.com/api/1/"
        self._api_key = f"APIKey {api_key}"
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method:str, endpoint: str, ep_params: Dict = None, data: Dict = None):
        full_url = self.url + endpoint
        headers = {"Authorization": self._api_key}
        response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify, headers=headers, params=ep_params, json=data)
        data_out = response.json()
        if response.status_code >= 200 and response.status_code <= 299:
            return data_out
        raise Exception(data_out)
    
    def get(self, endpoint: str, ep_params: Dict = None) -> List[Dict]:
        return self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)
    
    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None):
        return self._do(http_method="POST", endpoint=endpoint, ep_params=ep_params, data=data)
    
    
