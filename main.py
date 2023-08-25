from modules import api_request, formater, read_csv

def chunk_list(lst: list, chunk_size: int) -> list:
    """
    Returns a generator object that yields chunks of the given list with the specified size.

    Args:
        lst (list): The list to be chunked.
        chunk_size (int): The size of each chunk.

    Yields:
        list: A chunk of the list with the specified size.
    """
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

csv_data = read_csv.read_csv('items.csv')
payload = formater.request_formater(csv_data)

url_base = 'https://api.instabuy.com.br/store'
token = 'Mq1EWAXiHwraLIQgfq4stmUxKiM6VpC5Xd9o3wuX1Go'
batch_size = 500

payload_batches = list(chunk_list(payload, batch_size))

for batch in payload_batches:
    api_request.request_products(batch, url_base, token)
token = 'Mq1EWAXiHwraLIQgfq4stmUxKiM6VpC5Xd9o3wuX1Go'
batch_size = 500

payload_batches = list(chunk_list(payload, batch_size))

for batch in payload_batches:
    api_request.request_products(batch, url_base, token)