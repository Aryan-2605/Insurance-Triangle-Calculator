import csv


class OutputWriter():
    @staticmethod
    def write_to_csv(filename, comp, non_comp, smallest_value, total_dev_years):
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([smallest_value, total_dev_years])
            writer.writerow(['Comp'] + comp)
            writer.writerow(['Non-Comp'] + non_comp)
