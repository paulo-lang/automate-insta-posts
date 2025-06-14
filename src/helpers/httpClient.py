import requests

class HTTPClient:
    def make_http_request(url, method='GET', headers=None, data=None, params=None, timeout=10):
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                params=params,
                timeout=timeout
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"HTTP request failed: {e}")
            return None
