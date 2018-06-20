class AtmosphericPhenomena:
    def __init__(self, atmospheric_phenomena_key, duration):
        atmospheric_phenomena = {'Дж': 'Дождь', 'ДЛ': 'Дождь ливневый', 'Мр': 'Морось', 'ЛД': 'Ледяной дождь',
                                 'С': 'Снег', 'СМ': 'Снег мокрый', 'СЛ': 'Снег ливневый',
                                 'СЛМ': 'Снег ливневый мокрый', 'КС': 'Крупа снежная', 'КЛ': 'Крупа ледяная',
                                 'Гд': 'Град', 'ЗС': 'Зерна снежные', 'ИЛ': 'Иглы ледяные', 'Р': 'Роса',
                                 'ИК': 'Изморозь кристаллическая', 'ИЗ': 'Изморозь зернистая', 'И': 'Иней',
                                 'Гл': 'Гололед', 'Глц': 'Гололедица', 'Дм': 'Дымка', 'Т': 'Туман',
                                 'ТП': 'Туман просвечивающий', 'МО': 'Метель общая', 'МН': 'Метель низовая',
                                 'П': 'Поземок', 'Г': 'Гроза', 'З': 'Зарница', 'Мг': 'Мгла',
                                 }
        self.atmospheric_phenomena = atmospheric_phenomena[atmospheric_phenomena_key]
        self.duration = duration

    def __repr__(self):
        return 'atmospheric_phenomena: {0.atmospheric_phenomena}, duration: {0.duration};'.format(self)
