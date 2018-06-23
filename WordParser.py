import docx2txt


class WordParser:
    @staticmethod
    def parse(file_name):
        my_text = docx2txt.process(file_name)
        return my_text.split('\n\n')
