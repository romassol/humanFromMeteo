from AirTemperature import AirTemperature
from WindSpeed import WindSpeed
from WeatherHour import WeatherHour
from Admixture import Admixture


class WeatherMeasurements:
    def __init__(self, hour=None, atmosphere_pressure=None, temperature_on_time=None, temperature_min_for_3_hours=None,
                 temperature_max_for_3_hours=None, partial_pressure_of_water_vapor_in_air=None,
                 relative_humidity=None, saturation_deficit=None, dew_point_temperature=None,
                 underlying_surface_temperature=None, wind_direction=None, wind_average=None, wind_max_for_3_hours=None,
                 precipitation_amount=None, atmospheric_phenomena=None, snow=None):
        if hour is None:
            self.hour_measurements = {}
        else:
            self.hour_measurements = {hour: WeatherHour(atmosphere_pressure, temperature_on_time,
                                                        temperature_min_for_3_hours, temperature_max_for_3_hours,
                                                        partial_pressure_of_water_vapor_in_air, relative_humidity,
                                                        saturation_deficit, dew_point_temperature,
                                                        underlying_surface_temperature, wind_direction, wind_average,
                                                        wind_max_for_3_hours, precipitation_amount)}
        self.atmospheric_phenomena = atmospheric_phenomena
        self.snow = snow

    def set_admixture(self, key, value, hour):
        if hour in self.hour_measurements:
            self.hour_measurements[hour].set_admixture(key, value)
        else:
            weather_hour = WeatherHour()
            weather_hour.set_admixture(key, value)
            self.hour_measurements[hour] = weather_hour

    def set_weather(self, hour, atmosphere_pressure, temperature_on_time, temperature_min_for_3_hours,
                    temperature_max_for_3_hours, partial_pressure_of_water_vapor_in_air, relative_humidity,
                    saturation_deficit, dew_point_temperature, underlying_surface_temperature, wind_direction,
                    wind_average, wind_max_for_3_hours, precipitation_amount):
        if hour in self.hour_measurements:
            self.hour_measurements[hour].set_weather(atmosphere_pressure, temperature_on_time, temperature_min_for_3_hours,
                    temperature_max_for_3_hours, partial_pressure_of_water_vapor_in_air, relative_humidity,
                    saturation_deficit, dew_point_temperature, underlying_surface_temperature, wind_direction,
                    wind_average, wind_max_for_3_hours, precipitation_amount)
        else:
            weather_hour = WeatherHour()
            weather_hour.set_weather(atmosphere_pressure, temperature_on_time, temperature_min_for_3_hours,
                    temperature_max_for_3_hours, partial_pressure_of_water_vapor_in_air, relative_humidity,
                    saturation_deficit, dew_point_temperature, underlying_surface_temperature, wind_direction,
                    wind_average, wind_max_for_3_hours, precipitation_amount)
            self.hour_measurements[hour] = weather_hour

    def set_snow(self, snow):
        self.snow = snow if type(snow) is not str else 0

    def set_atmospheric_phenomena(self, atmospheric_phenomena):
        self.atmospheric_phenomena = atmospheric_phenomena

    def __repr__(self):
        return 'atmospheric_phenomena: {0.atmospheric_phenomena}\n' \
               'snow: {0.snow}\n' \
               'hour_measurements: {0.hour_measurements}'.format(self)
