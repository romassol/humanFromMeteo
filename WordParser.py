import docx2txt


class WordParser:


    @staticmethod
    def parse(file_name):
        my_text = docx2txt.process(file_name)
        return my_text.split('\n\n')
        # for i, b in enumerate(a):
        #     if 'месяц' in a[i]:
        #         month = a[i][-1:]
        #         year = a[i][-18:-14]
        #     a[i] = b
            #print(b)
        # print(month, year)


if __name__ == '__main__':
    file_name = "data\\Gidromet_dannye_2017\\Екатеринбург\\июль.docx"
    WordParser.parse(file_name)