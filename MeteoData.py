from WeatherMeasurements import WeatherMeasurements
import datetime
import math
import inspect


class MeteoData:
    def __init__(self):
        self.measurements = {2015: {}}
        for i in range(12):
            self.measurements[2015][i] = {}

    def _get_measurement(self, measurements, measurement_name, measurement_field=None):
        if measurement_field is None:
            return vars(measurements)[measurement_name]
        return vars(vars(measurements)[measurement_name])[measurement_field]

    def _get_average_measurements(self, start_date, end_date, day_offset, measurement_name, measurement_field=None):
        meteo = self._get_meteo_data(start_date, end_date, day_offset)
        result = 0
        for m in meteo:
            average_measurement = 0
            count = 0
            if m is None:
                return None
            for h in m.hour_measurements:
                measurement = self._get_measurement(m.hour_measurements[h], measurement_name, measurement_field)
                if measurement is not None:
                    count += 1
                    average_measurement += measurement
            average_measurement = average_measurement/count if count != 0 else None
            result += average_measurement if average_measurement is not None else 0
        return result / len(meteo) if result != 0 else None

    def _get_max_difference_measurements(self, start_date, end_date, day_offset, measurement_name, measurement_field=None):
        meteo = self._get_meteo_data(start_date, end_date, day_offset)
        result = 0
        current = 0
        for m in meteo:
            if m is None:
                return None
            for h in m.hour_measurements:
                measurement = self._get_measurement(m.hour_measurements[h], measurement_name, measurement_field)
                if current == 0 or current is None:
                    current = measurement
                    continue
                if measurement is not None and result < math.fabs(measurement - current):
                    result = math.fabs(measurement - current)
                current = measurement
        return result

    def get_average_air_temperature(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'air_temperature', 'on_time')

    def get_max_difference_air_temperature(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'air_temperature', 'on_time')

    def get_average_atmosphere_pressure(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'atmosphere_pressure')

    def get_max_difference_atmosphere_pressure(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'atmosphere_pressure')

    def get_average_partial_pressure_of_water_vapor_in_air(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset,
                                             'partial_pressure_of_water_vapor_in_air')

    def get_max_difference_partial_pressure_of_water_vapor_in_air(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset,
                                                    'partial_pressure_of_water_vapor_in_air')

    def get_average_relative_humidity(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'relative_humidity')

    def get_max_difference_relative_humidity(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'relative_humidity')

    def get_average_saturation_deficit(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'saturation_deficit')

    def get_max_difference_saturation_deficit(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'saturation_deficit')

    def get_average_dew_point_temperature(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'dew_point_temperature')

    def get_max_difference_dew_point_temperature(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'dew_point_temperature')

    def get_average_underlying_surface_temperature(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'underlying_surface_temperature')

    def get_max_difference_underlying_surface_temperature(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'underlying_surface_temperature')

    def get_average_wind_direction(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'wind_direction')

    def get_max_difference_wind_direction(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'wind_direction')

    def get_average_wind_speed(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'wind_speed', 'average')

    def get_max_difference_wind_speed(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'wind_speed', 'average')

    def get_average_precipitation_amount(self, start_date, end_date, day_offset):
        return self._get_average_measurements(start_date, end_date, day_offset, 'precipitation_amount')

    def get_max_difference_precipitation_amount(self, start_date, end_date, day_offset):
        return self._get_max_difference_measurements(start_date, end_date, day_offset, 'precipitation_amount')

    def _get_admixtures(self, start_date, end_date, day_offset):
        meteo = self._get_meteo_data(start_date, end_date, day_offset)
        result = []
        for m in meteo:
            if m is None:
                return None
            for h in m.hour_measurements:
                measurement = self._get_measurement(m.hour_measurements[h], 'admixture')
                if measurement is not None:
                    result.append(measurement)
        return result

    def _get_average_admixture(self, start_date, end_date, day_offset, admixture_name):
        admixtures = self._get_admixtures(start_date, end_date, day_offset)
        result = 0
        counter = 0
        if admixtures is None:
            return None
        for admixture in admixtures:
            for adm in admixture:
                if adm.name == admixture_name and adm.value is not None:
                    result += adm.value
                    counter += 1
                    break
        return result/counter if counter != 0 else result

    def _get_max_difference_admixture(self, start_date, end_date, day_offset, admixture_name):
        admixtures = self._get_admixtures(start_date, end_date, day_offset)
        result = 0
        last = None
        if admixtures is None:
            return None
        for admixture in admixtures:
            for adm in admixture:
                if adm.name == admixture_name and adm.value is not None:
                    if last is None:
                        last = adm.value
                        break
                    if result < math.fabs(adm.value - last):
                        result = math.fabs(adm.value - last)
                    last = adm.value
        return result

    def get_average_suspended_solids(self, start_date, end_date, day_offset):
        return self._get_average_admixture(start_date, end_date, day_offset, 'suspended solids')

    def get_max_difference_suspended_solids(self, start_date, end_date, day_offset):
        return self._get_max_difference_admixture(start_date, end_date, day_offset, 'suspended solids')

    def get_average_sulfur_dioxide(self, start_date, end_date, day_offset):
        return self._get_average_admixture(start_date, end_date, day_offset, 'sulfur dioxide')

    def get_max_difference_sulfur_dioxide(self, start_date, end_date, day_offset):
        return self._get_max_difference_admixture(start_date, end_date, day_offset, 'sulfur dioxide')

    def get_average_carbon_monoxide(self, start_date, end_date, day_offset):
        return self._get_average_admixture(start_date, end_date, day_offset, 'carbon monoxide')

    def get_max_difference_carbon_monoxide(self, start_date, end_date, day_offset):
        return self._get_max_difference_admixture(start_date, end_date, day_offset, 'carbon monoxide')

    def get_average_nitrogen_dioxide(self, start_date, end_date, day_offset):
        return self._get_average_admixture(start_date, end_date, day_offset, 'nitrogen dioxide')

    def get_max_difference_nitrogen_dioxide(self, start_date, end_date, day_offset):
        return self._get_max_difference_admixture(start_date, end_date, day_offset, 'nitrogen dioxide')

    def get_average_solid_fluorides(self, start_date, end_date, day_offset):
        return self._get_average_admixture(start_date, end_date, day_offset, 'solid fluorides')

    def get_max_difference_solid_fluorides(self, start_date, end_date, day_offset):
        return self._get_max_difference_admixture(start_date, end_date, day_offset, 'solid fluorides')

    def get_average_hydrogen_fluoride(self, start_date, end_date, day_offset):
        return self._get_average_admixture(start_date, end_date, day_offset, 'hydrogen fluoride')

    def get_max_difference_hydrogen_fluoride(self, start_date, end_date, day_offset):
        return self._get_max_difference_admixture(start_date, end_date, day_offset, 'hydrogen fluoride')

    def get_average_snow(self, start_date, end_date, day_offset):
        meteo = self._get_meteo_data(start_date, end_date, day_offset)
        result = 0
        for m in meteo:
            if m is None:
                return None
            result += m.snow
        result /= len(meteo)
        return result

    def get_max_difference_snow(self, start_date, end_date, day_offset):
        meteo = self._get_meteo_data(start_date, end_date, day_offset)
        result = 0
        last = None
        for m in meteo:
            if m is None:
                return None
            if last is None:
                last = m.snow
                continue
            if result < math.fabs(last - m.snow):
                result = math.fabs(last - m.snow)
            last = m.snow
        return result

    def _get_meteo_data(self, start_date, end_date, day_offset):
        result = []
        i = 0
        current_date = start_date + datetime.timedelta(days=i)
        while end_date >= current_date:
            if current_date.year in self.measurements and \
                    current_date.month - 1 in self.measurements[current_date.year] and \
                    current_date.day in self.measurements[current_date.year][current_date.month - 1]:
                result.append(self.measurements[current_date.year][current_date.month - 1][current_date.day])
            else:
                result.append(None)
            i += 1
            current_date = start_date + datetime.timedelta(days=i + day_offset)
        return result

    # def get_atmospheric_phenomena(self, year, month, day):
    #     return self.measurements[year][month][day].atmospheric_phenomena
    #
    # def get_snow(self, day):
    #     return self.measurements[year][month][day].snow
    #
    # def get_air_temperature(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].air_temperature
    #
    # def get_partial_pressure_of_water_vapor_in_air(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].partial_pressure_of_water_vapor_in_air
    #
    # def get_relative_humidity(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].relative_humidity
    #
    # def get_saturation_deficit(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].saturation_deficit
    #
    # def get_dew_point_temperature(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].dew_point_temperature
    #
    # def get_underlying_surface_temperature(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].underlying_surface_temperature
    #
    # def get_wind_direction(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].wind_direction
    #
    # def get_wid_speed(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].wid_speed
    #
    # def get_precipitation_amount(self, year, month, day, hour):
    #     return self.measurements[year][month][day].hour_measurements[hour].precipitation_amount

    def __repr__(self):
        result = ''
        for y in self.measurements:
            result += 'year: ' + str(y) + '\n'
            for m in self.measurements[y]:
                result += 'month: ' + str(m) + '\n'
                for d in self.measurements[y][m]:
                    result += 'day: ' + str(d) + ' ' + str(self.measurements[y][m][d])
                    result += '\n'
            result += '\n'
        return result


if __name__ == '__main__':
    m = MeteoData()
    method_list = [func[1] for func in inspect.getmembers(m, predicate=inspect.ismethod) if not func[0].startswith('_')]
    print(method_list)
