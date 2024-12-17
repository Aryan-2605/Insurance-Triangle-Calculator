class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.biggest_year = float('-inf')
        self.smallest_year = float('inf')
        self.comp = []
        self.non_comp = []
        self.non_comp_placeholder = []
        self.comp_placeholder = []
        self.final_comp = []
        self.final_non_comp = []

    def sort_data(self):
        for product, origin_years in self.data.items():
            #print(f"Product: {product}")
            for origin_year in origin_years:
                #print(f"  Origin Year: {origin_year}")
                if product == 'Comp':
                    self.comp.append(origin_year)
                else:
                    self.non_comp.append(origin_year)
                if origin_year < self.smallest_year:
                    self.smallest_year = origin_year
                if origin_year > self.biggest_year:
                    self.biggest_year = origin_year

        all_years = sorted(set(self.comp + self.non_comp))
        for year in all_years:
            if year in self.non_comp:
                self.non_comp_placeholder.append(year)
            else:
                self.non_comp_placeholder.append(0)
            if year in self.comp:
                self.comp_placeholder.append(year)
            else:
                self.comp_placeholder.append(0)

    def add_cumulative_years(self):
        output_data = {}
        for product, origin_years in self.data.items():
            output_data[product] = []
            for origin_year, dev_years in sorted(origin_years.items()):
                cumulative = 0.0
                for dev_year in range(origin_year, max(dev_years.keys()) + 1):
                    value = dev_years.get(dev_year, 0.0)
                    cumulative += value
                    output_data[product].append((origin_year, cumulative))
        return output_data

    def placeholder_amount(self, output_data, indexed, product):
        all_years = sorted(set(self.comp + self.non_comp))
        placeholders = {}
        last_year = None
        count = 0
        for year, _ in output_data[product]:
            if year != last_year:
                count = 0
            for index in indexed:
                if year == all_years[index]:
                    count += 1
                    placeholders[year] = count
            last_year = year
        return placeholders

    @staticmethod
    def append_placeholders(placeholders, output_data, type_of_comp):
        for year, times in placeholders.items():
            for i in range(int(times)):
                output_data[type_of_comp].append((year, 0))
        return output_data

    def split_array(self, ordered_data):
        for product, dev_year in ordered_data.items():
            for dev_years, cum_val in dev_year:
                if product == 'Comp':
                    self.final_comp.append(cum_val)
                else:
                    self.final_non_comp.append(cum_val)
