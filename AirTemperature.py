class AirTemperature:
    def __init__(self, on_time, min_for_3_hours, max_for_3_hours):
        self.on_time = on_time
        self.min_for_3_hours = min_for_3_hours
        self.max_for_3_hours = max_for_3_hours

    def __float__(self):
        if self.on_time is None:
            return float('nan')
        return self.on_time

    def __str__(self):
        return 'on_time: {0.on_time}, min_for_3_hours: {0.min_for_3_hours}, ' \
               'max_for_3_hours: {0.max_for_3_hours}'.format(self)
