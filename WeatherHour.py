from WindSpeed import WindSpeed
from AirTemperature import AirTemperature
from Admixture import Admixture


class WeatherHour:
    def __init__(self, atmosphere_pressure=None, temperature_on_time=None, temperature_min_for_3_hours=None,
                 temperature_max_for_3_hours=None, partial_pressure_of_water_vapor_in_air=None, relative_humidity=None,
                 saturation_deficit=None, dew_point_temperature=None, underlying_surface_temperature=None,
                 wind_direction=None, wind_average=None, wind_max_for_3_hours=None, precipitation_amount=None,
                 admixture=None):
        self.atmosphere_pressure = atmosphere_pressure
        self.air_temperature = AirTemperature(temperature_on_time,
                                              temperature_min_for_3_hours, temperature_max_for_3_hours)
        self.partial_pressure_of_water_vapor_in_air = partial_pressure_of_water_vapor_in_air
        self.relative_humidity = relative_humidity
        self.saturation_deficit = saturation_deficit
        self.dew_point_temperature = dew_point_temperature
        self.underlying_surface_temperature = underlying_surface_temperature
        self.wind_direction = wind_direction
        self.wind_speed = WindSpeed(wind_average, wind_max_for_3_hours)
        self.precipitation_amount = precipitation_amount
        self.admixture = admixture

    def set_admixture(self, key, value):
        if self.admixture is None:
            self.admixture = []
        self.admixture.append(Admixture(key, value))

    def set_weather(self, atmosphere_pressure, temperature_on_time, temperature_min_for_3_hours,
                 temperature_max_for_3_hours, partial_pressure_of_water_vapor_in_air, relative_humidity,
                 saturation_deficit, dew_point_temperature, underlying_surface_temperature,
                 wind_direction, wind_average, wind_max_for_3_hours, precipitation_amount):
        self.atmosphere_pressure = atmosphere_pressure
        self.air_temperature = AirTemperature(temperature_on_time,
                                              temperature_min_for_3_hours, temperature_max_for_3_hours)
        self.partial_pressure_of_water_vapor_in_air = partial_pressure_of_water_vapor_in_air
        self.relative_humidity = relative_humidity
        self.saturation_deficit = saturation_deficit
        self.dew_point_temperature = dew_point_temperature
        self.underlying_surface_temperature = underlying_surface_temperature
        self.wind_direction = wind_direction
        self.wind_speed = WindSpeed(wind_average, wind_max_for_3_hours)
        self.precipitation_amount = precipitation_amount if type(precipitation_amount) is not str else None

    def __repr__(self):
        return'atmosphere_pressure: {0.atmosphere_pressure}, '\
                'air_temperature: {0.air_temperature}, ' \
                'partial_pressure_of_water_vapor_in_air: {0.partial_pressure_of_water_vapor_in_air}, ' \
                'relative_humidity: {0.relative_humidity}, ' \
                'saturation_deficit: {0.saturation_deficit}, ' \
                'dew_point_temperature: {0.dew_point_temperature}, ' \
                'underlying_surface_temperature: {0.underlying_surface_temperature}, ' \
                'wind_direction: {0.wind_direction}, ' \
                'wind_speed: {0.wind_speed}, ' \
                'precipitation_amount: {0.precipitation_amount}'\
                'admixture: {0.admixture}'.format(self)
