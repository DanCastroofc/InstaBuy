import csv

def read_csv(file_name: str) -> csv.reader:
    """
    Reads a CSV file and returns its contents as a list of rows, excluding the header row.

    Args:
        file_name (str): The name of the CSV file to be read.

    Returns:
        list: A list of rows from the CSV file, excluding the header row. Each row is represented as a list of values.
    """
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        
        return list(csv_reader)