import requests

def request_products(data_payload, url_base, token):
    """
    Sends a PUT request to a specified URL with a payload containing a list of products.
    
    Args:
        data_payload (list): A list of products to be sent in the request payload.
        url_base (str): The base URL to which the request will be sent.
        token (str): The API token used for authentication.
    
    Returns:
        None
    """
    headers = {
        'api-key': token,
        'Content-Type': 'application/json'
    }
    
    payload = {
        "products": data_payload
    }
    
    url = f"{url_base}/products"
    
    response = requests.put(url, json=payload, headers=headers)
    print(f'Request response: {response.text}')