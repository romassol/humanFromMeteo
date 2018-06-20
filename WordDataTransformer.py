from Admixture import Admixture
from WordParser import WordParser


class WordDataTransformer:
    @staticmethod
    def set_admixture(meteo_data, data):
        month = -1
        year = -1
        day = -1
        hour = -1
        all_admixture_keys = ['001', '002', '004', '005', '012', '013']
        admixture_keys = []
        i = 0
        while i < len(data):
            if month < 0 and 'месяц' in data[i]:
                month = int(data[i][-2:].strip()) - 1
                year = int(data[i][-18:-14])
                i += 1
                continue
            if len(admixture_keys) == 0:
                for admixture_key in all_admixture_keys:
                    if admixture_key in data[i]:
                        admixture_keys = WordDataTransformer.get_numbers(data[i])
                        i += 4
                        break
                i += 1
                continue
            day = data[i][1:3].strip()
            hour = data[i][4:6].strip()

            if day.isdigit() and hour.isdigit():
                admixtures = WordDataTransformer.get_admixtures(data[i][32:32 + len(admixture_keys)*6 + 1])
                for k in range(len(admixture_keys)):
                    day = int(day)
                    hour = int(hour)
                    meteo_data.measurements[year][month][day].set_admixture(admixture_keys[k], admixtures[k], hour)
            i += 1

    @staticmethod
    def get_numbers(line):
        numbers = []
        j = 0
        while j < len(line):
            digit = ''
            while line[j].isdigit():
                digit += line[j]
                j += 1
            if len(digit) != 0:
                numbers.append(digit)
            j += 1
        return numbers

    @staticmethod
    def get_admixtures(line):
        admixtures = []
        j = 0
        while (j*6 + 1) < len(line):
            digit = line[j*6 + 1:j*6 + 6].strip()
            if len(digit) == 0:
                admixtures.append(None)
            else:
                admixtures.append(int(digit))
            j += 1
        return admixtures


if __name__ == '__main__':
    file_name = "data\\Gidromet_dannye_2017\\Екатеринбург\\июль.docx"
    data = WordParser.parse(file_name)
    print(data)

    WordDataTransformer.set_admixture(data)
