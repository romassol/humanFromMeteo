import xlrd
from Constants import Constants
from Sheet import Sheet
from Column import Column
from ExcelDataTransformer import ExcelDataTransformer


class ExcelParser:
    @staticmethod
    def parse_worksheet(file_name, sheet_index, start_col, end_col, start_row_ids, col_numbers_with_filling_gaps=None):
        file = xlrd.open_workbook(file_name)
        file_sheet = file.sheet_by_index(sheet_index)
        sheet = Sheet(sheet_index, file_sheet.name, ExcelParser.find_heading(file_sheet))
        for i, start_row_id in enumerate(start_row_ids):
            for col_number in range(start_col, end_col):
                if i == len(start_row_ids) - 1:
                    values = file_sheet.col_values(col_number, start_row_id)
                else:
                    values = file_sheet.col_values(col_number,
                                                   start_row_id, start_row_ids[i + 1] - start_row_id + 1)
                if not col_numbers_with_filling_gaps is None and col_number in col_numbers_with_filling_gaps:
                    ExcelParser.fill_gaps_in_col(values)
                sheet.data.append(values)
        return sheet

    @staticmethod
    def fill_gaps_in_col(col):
        for i, value in enumerate(col):
            if i != 0 and value == '':
                col[i] = col[i - 1]

    @staticmethod
    def find_heading(sheet):
        head = ''
        i = 0
        row = sheet.row(i)
        values = []
        while not ExcelParser.is_row_empty(row):
            for cell in row:
                values.clear()
                if cell.ctype != 0:
                    values.append(cell.value)
            head += ' '.join(values)
            i += 1
            row = sheet.row(i)
        return head

    @staticmethod
    def is_row_empty(row):
        for cell in row:
            if cell.ctype != 0:
                return False
        return True


if __name__ == '__main__':
    weather_data = ExcelParser.parse_worksheet(0, 0, 15, [4], [0]).data
    atmospheric_phenomena = ExcelParser.parse_worksheet(12, 0, 12, [5, 40]).data[1]
    snow = ExcelParser.parse_worksheet(13, 1, 2, [4]).data[0]
    weather = ExcelDataTransformer.get_meteo_data(weather_data, atmospheric_phenomena, snow)
    for (d,v) in weather.day_measurements.items():
        print('day:{0} {1}'.format(d, v))
        print()
