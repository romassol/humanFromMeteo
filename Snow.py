class Snow:
    def __init__(self, data):
        month = {'январь': 0,'февраль': 1, 'март': 2, 'апрель': 3, 'май': 4, 'июнь': 5, 'июль': 6, 'август': 7,
                 'сентябрь': 8, 'октябрь': 9, 'ноябрь': 10, 'декабрь': 11}
        self.snow_data = []
        for i in range(12):
            self.snow_data.append([])
        for m in data:
            if m[0] in month:
                self.snow_data[month[m[0]]] = m[1:]

    def __repr__(self):
        return str(self.snow_data)
