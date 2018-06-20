class WindSpeed:
    def __init__(self, average, max_for_3_hours):
        self.average = average
        self.max_for_3_hours = max_for_3_hours

    def __str__(self):
        return 'average: {0.average}, max_for_3_hours: {0.max_for_3_hours}'.format(self)
