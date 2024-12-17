import csv
from collections import defaultdict


class DataLoader:
    @staticmethod
    def load_data(file_name):
        data = defaultdict(lambda: defaultdict(dict))
        with open(file_name) as csvfile:
            # It ittrated over each row from the CSV file and once the variable is used the method gets exhausted.
            reader = csv.DictReader(csvfile)
            #print(reader.fieldnames)
            for row in reader:
                #print(row)
                cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
                try:
                    product = cleaned_row["Product"]
                    origin_year = int(cleaned_row["Origin Year"])
                    dev_year = int(cleaned_row["Development Year"])
                    value = float(cleaned_row["Incremental Value"])
                    data[product][origin_year][dev_year] = value
                except (ValueError, KeyError) as error:
                    raise ValueError(f"Invalid data: {error}")
            return data

