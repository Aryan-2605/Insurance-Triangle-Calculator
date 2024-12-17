import csv
import os


class ValidateCSV:
    headers = ['Product', 'Origin Year', 'Development Year', 'Incremental Value']

    @staticmethod
    def validate_file(filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"{filename} is not a file. Make sure it's in the correct directory.")
        if not filename.endswith(".csv"):
            raise FileNotFoundError(f"{filename} is not a CSV file.")

        with open(filename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            actual_headers = [header.strip() for header in (reader.fieldnames or [])]
            if actual_headers != ValidateCSV.headers:
                raise ValueError(
                    f"CSV file does not have the expected headers.\n"
                    f"Expected headers: {ValidateCSV.headers}\n"
                    f"Found headers: {reader.fieldnames}\n"
                    f"Please ensure the file includes all required columns."
                )
