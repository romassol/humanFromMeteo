# humanFromMeteo

### Описание

Определение зависимости исхода лечения (1. Без перемен, 2. Улучшение, 3. Ухудшение, 4. Выздоровление) от различных метеоданных, металлов и концентрации примесей в воздухе.

### Структура решения

1. Статические классы-парсеры: 

* `ExcelParser` - основа - метод `parse_worksheet`
* `WordParser` - основа - метод `parse`

2. Статические классы-трансформеры:

* `ExcelDataTransformer` - основа - метод `set_meteo_data`, который заполняет поля во входном аргументе `meteo_data` (класс `MeteoData`) данными
* `WordDataTransformer` - основа - метод `set_admixture`, который заполняет поле примесей (`admixture`)

3. Классы с метеоданными:

* Самый главный - `MeteoData` - в нем все хранится в поле `measurements`, также есть методы для вычисления каждого параметра в среднем за указанное время и вычислени максимального перепада каждого параметра за указанное время
* `WeatherMeasurements` - содержит `atmospheric_phenomena` (класс `AtmosphericPhenomena`), `snow`(класс `Snow`) и `hour_measurements` (класс `WeatherHour`)
* `WeatherHour` - содержит все остальные метеоданные: 
  * `atmosphere_pressure`
  * `air_temperature` (класс `AirTemperature`)
  * `partial_pressure_of_water_vapor_in_air`
  * `relative_humidity`
  * `saturation_deficit`
  * `dew_point_temperature`
  * `underlying_surface_temperature`
  * `wind_direction`
  * `wind_speed` (класс `WindSpeed`)
  * `precipitation_amount`
  * `admixture` (класс `Admixture`)

4. Класс с данными о пациенте:

* `Patient`:
  * `id`
  * `final_diagnosis` (класс `FinalDiagnosis`)
  * `birthdate`
  * `treatment_start_date`
  * `statement_date`
  * `icd`
  * `ib_number`
  * `treatment_outcome` (Класс `TreatmentOutcome`)
  * `result`
  * `retirement_rankine`
  * `admission_rankine`
  * `age` (несколько групп: 1. до 20, 2. 20-40, 3. 40-60, 4. старше 60)

5. Класс `Main` - загрузка всех данных, обучение нейронной сети, предсказывание результатов и запись в файл вероятности угадывания

### Поиск зависимости

Для поиска зависимости составляются различные аргументы для обучения нейронной сети: 

* статические данные - финальный диагноз, возраст, время лечения
* диннамические - различные метеоданные

Составляем все подмножества множества всех метеоданных. Добавляем одно подмножество к статическим данным и переходим к следующим шагам, связанным с нейронной сетью ↓ , и так для всех подмножеств мощностью <= 3 (это ограничение связанно лишь с ограничением времени). 

1. Берется готовая нейронная сеть scikit-learn
2. Обучается на части данных - `clf.fit(X_train, Y_train)`
3. Оставшуюся часть отдаем нейронной сети после обучения на предсказание - `clf.predict(X_test)`
4. Сравниваем результаты предсказания с реальными данными, получаем вероятность угадывания

### Результаты

Топ 3:

1. Вероятность - 0,7268292682926829

   Используемые данные:

   * средний дефицит насыщения
   * максимальный перепад диоксида азота
   * максимальный перепад парциального давления водяного пара в воздухе

2. Вероятность - 0,7134146341463414

   Используемые данные:

   * максимальный перепад диоксида азота
   * максимальный перепад парциального давления водяного пара в воздухе
   * максимальный перепад дефицита насыщения

3. Вероятность - 0,7073170731707317

   Используемые данные:

   * средние взвешенные твердые вещества
   * максимальный перепад диоксида азота
   * максимальный перепад дефицита насыщения