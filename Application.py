from DataLoader import DataLoader
from DataProcessor import DataProcessor
from OutputWriter import OutputWriter
from ValidateCSV import ValidateCSV
from pprint import pprint


class Application:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        ValidateCSV.validate_file(self.input_file)
        data = DataLoader.load_data(self.input_file)
        #pprint(data)
        processor = DataProcessor(data)
        processor.sort_data()
        output_data = processor.add_cumulative_years()

        comp_indexed = [index for index in range(len(processor.comp_placeholder))
                        if processor.comp_placeholder[index] == 0]
        non_comp_indexed = [index for index in range(len(processor.non_comp_placeholder))
                            if processor.non_comp_placeholder == 0]

        comp_placeholders = (processor.placeholder_amount(output_data, comp_indexed, 'Non-Comp'))
        non_comp_placeholders = (processor.placeholder_amount(output_data, non_comp_indexed, 'Comp'))

        output_data = processor.append_placeholders(comp_placeholders, output_data, 'Comp')
        output_data = processor.append_placeholders(non_comp_placeholders, output_data, 'Non-Comp')

        #Sorts by Year
        ordered_data = {
                product: sorted(years, key=lambda x: x[0])
                for product, years in output_data.items()
            }

        processor.split_array(ordered_data)

        OutputWriter.write_to_csv(
            filename=self.output_file,
            comp=processor.final_comp,
            non_comp=processor.final_non_comp,
            smallest_value=processor.smallest_year,
            total_dev_years=processor.biggest_year - processor.smallest_year + 1
        )


if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    app = Application(input_file, output_file)
    try:
        app.run()
    except ValueError as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
