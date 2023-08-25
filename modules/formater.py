from datetime import datetime
import locale

def is_valid_date(year, month, day):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def last_valid_day(year, month):
    for day in range(31, 0, -1):
        if is_valid_date(year, month, day):
            return day
    return None

def format_date(date_str):
    """
    Formats a date string to the ISO 8601 standard.

    Args:
        date_str (str): The date string to be formatted.

    Returns:
        str: The formatted date string in the ISO 8601 standard. If the input date string is empty or cannot be converted, an empty string is returned.
    """
    if date_str:
        try:
            date_split = date_str.split("-")
            if len(date_split[2]) == 2:
                date_split[2] = f'20{date_split[2]}'
            date_str = "-".join(date_split)
            
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            date_localed = datetime.strptime(date_str, '%d-%b-%Y')
            
            year = date_localed.year
            month = date_localed.month
            day = min(date_localed.day, last_valid_day(year, month))
            
            formatted_date = datetime(year, month, day).isoformat()
            return formatted_date
        except:
            print(f"Couldn't convert: {date_str}")
            return ''
    else:
        return ''

def format_price(price_value):
    """
    Formats a price value by removing leading and trailing whitespace, replacing commas with periods, and rounding to two decimal places.

    Args:
        price_value (str or float): The price value to be formatted.

    Returns:
        str or float: The formatted price value, rounded to two decimal places. If the input is invalid or empty, an empty string is returned.
    """
    conv_price = str(price_value).strip()
    if not conv_price: 
        return '' 
    
    conv_price = conv_price.replace(',', '.')
    try:
        return round(float(conv_price), 2)
    except ValueError:
        return ''

def format_promo_price(price, promo_desc=''):
    """
        Formats the promotional price of a product.
        
        Args:
            conv_price (str): A string representing the promotional price of a product.
        
        Returns:
            str: A formatted string representing the promotional price of a product.
    """
    if promo_desc:
        return format_price(price - promo_desc)
    else:
        return ''

def request_formater(request_data):
    """
    Formats a list of request data into a list of dictionaries representing products.

    Args:
        request_data (list): A list of request data. Each element in the list is a list containing the following information about a product: internal code, barcodes, name, price, promotional price, promotional end date, stock, and visibility.

    Returns:
        list: A list of dictionaries representing products. Each dictionary contains the following keys: "internal_code", "visible", "stock", "name", "barcodes", "price", "promo_price", and "promo_end_at". The values of these keys are the formatted data from the request_data input.
    """
    products = []

    for line in request_data:
        internal_code, barcodes, name, price, promo_price, promo_end_date, stock, visible = line

        price = format_price(price)
        promo_price = format_promo_price(promo_price)
        promo_end_at = format_date(promo_end_date)

        if barcodes and len(barcodes) not in [8, 12, 13]:
            barcodes = []

        product = {
            "internal_code": internal_code,
            "visible": visible,
            "stock": stock,
            "name": name,
            "barcodes": barcodes,
            "price": price,
            "promo_price": promo_price,
            "promo_end_at": promo_end_at
        }
        products.append(product)

    return products