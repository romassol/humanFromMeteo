from Patient import Patient
from WeatherMeasurements import WeatherMeasurements
from AtmosphericPhenomena import AtmosphericPhenomena
from WeatherHour import WeatherHour


class ExcelDataTransformer:

    @staticmethod
    def get_patients(data):
        result = []
        patient_data = []
        patient_count = len(data[0])
        for j in range(patient_count):
            patient_data.clear()
            for i in range(len(data)):
                patient_data.append(data[i][j])
            result.append(Patient(*patient_data))
        return result

    @staticmethod
    def set_meteo_data(meteo_data, weather_data, atmospheric_phenomena, snow, year, month):
        weather_records_count = len(weather_data[0])
        weather_measurements = []
        day = 0
        hour = 0
        for j in range(weather_records_count):
            weather_measurements.clear()
            for i in range(len(weather_data)):
                if i == 0:
                    day = int(weather_data[i][j])
                elif i == 1:
                    hour = int(weather_data[i][j])
                else:
                    weather_measurements.append(weather_data[i][j])
            if day in meteo_data.measurements[year][month]:
                meteo_data.measurements[year][month][day].set_weather(hour, *weather_measurements)
                continue
            atmospheric_phenomena_data = atmospheric_phenomena[day - 1].split()
            if len(atmospheric_phenomena_data) % 2 != 0:
                raise ValueError('Error in atmospheric phenomena in {0} in day {1}'
                                 .format(atmospheric_phenomena_data, day))
            phenomens = []
            for k in range(len(atmospheric_phenomena_data)):
                if k % 2 != 0:
                    phenomens.append(
                        AtmosphericPhenomena(atmospheric_phenomena_data[k - 1], atmospheric_phenomena_data[k]))
            if len(snow) > day - 1:
                snow_measurements = snow[day - 1]
            else:
                snow_measurements = 0

            meteo_data.measurements[year][month][day] = WeatherMeasurements()
            meteo_data.measurements[year][month][day].set_weather(hour, *weather_measurements)
            meteo_data.measurements[year][month][day].set_atmospheric_phenomena(phenomens)
            meteo_data.measurements[year][month][day].set_snow(snow_measurements)
