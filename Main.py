import datetime
from sklearn import svm, preprocessing
from sklearn.preprocessing import label_binarize
import numpy as np
from itertools import chain, combinations
import inspect
from ExcelDataTransformer import ExcelDataTransformer
from ExcelParser import ExcelParser
from WordDataTransformer import WordDataTransformer
from WordParser import WordParser
from Snow import Snow
from Constants import Constants
from MeteoData import MeteoData
from datetime import timedelta


class Main:
    @staticmethod
    def get_data():
        patients = ExcelDataTransformer.get_patients(ExcelParser.parse_worksheet(
            Constants.patients_file, 0, 0, 12, [2]).data)
        atmospheric_phenomena = ExcelParser.parse_worksheet(Constants.ekb_meteo_file, 12, 0, 12, [5, 40]).data
        snow = Snow(ExcelParser.parse_worksheet(Constants.ekb_meteo_file, 13, 1, 9, [3]).data).snow_data
        meteo_data = MeteoData()
        for i in range(12):
            weather = ExcelParser.parse_worksheet(Constants.ekb_meteo_file, i, 0, 15, [4], [0]).data
            ExcelDataTransformer.set_meteo_data(
                meteo_data, weather, atmospheric_phenomena[i * 2 + 1], snow[i], 2015, i)
        for f in Constants.ekb_admixtures_files:
            WordDataTransformer.set_admixture(meteo_data, WordParser.parse(f))
        return patients, meteo_data


def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, n) for n in range(1, len(xs) + 1))


def get_input_and_target(patient_measurements, meteo_arguments, methods, day_offset, offset):
    is_None = False
    input_data = []
    target = []
    for i in range(len(meteo_arguments)):
        input_measurements = []
        for method in methods:
            measurement = method[1](meteo_arguments[i] - timedelta(day_offset), meteo_arguments[i], offset)
            if measurement is None:
                is_None = True
                break
            input_measurements.append(measurement)
        if not is_None:
            input_data.append(input_measurements)
            target.append(patient_measurements[i])
        else:
            is_None = False
    return input_data, target


def get_patient_count_and_dates(patients):
    patient_count = []
    dates = []
    counter = 1
    patients = sorted(patients, key=lambda x: x.treatment_start_date)
    current_date = None
    for i in range(len(patients)):
        if i == 0:
            current_date = patients[i].treatment_start_date
            continue
        # print(type(current_date))
        if current_date.day == patients[i].treatment_start_date.day and \
                        current_date.year == patients[i].treatment_start_date.year and \
                        current_date.month == patients[i].treatment_start_date.month:
            counter += 1
        else:
            patient_count.append(counter)
            counter = 1
            dates.append(current_date)
            current_date = patients[i].treatment_start_date
    return patient_count, dates


if __name__ == '__main__':
    data = Main.get_data()
    all_measurement_methods = [func for func in inspect.getmembers(data[1], predicate=inspect.ismethod)
                               if not func[0].startswith('_')]
    # patient_count_and_dates = get_patient_count_and_dates(data[0])
    # all_patient_measurements = patient_count_and_dates[0]
    # print([m[0] for m in all_measurement_methods])
    is_None = False

    for methods in powerset(all_measurement_methods):
        input_data = []
        target = []
        counter = [0, 0, 0, 0]
        for p in data[0]:
            input_measurements = p.to_array()
            for method in methods:
                measurement = method[1](p.treatment_start_date, p.statement_date, 0)
                if measurement is None:
                    is_None = True
                    break
                input_measurements.append(method[1](p.treatment_start_date, p.statement_date, 0))
            if not is_None:
                input_data.append(input_measurements)
                target.append(p.treatment_outcome)
            else:
                is_None = False
        input_data = np.array(input_data)
        # print(input_data, target)
        X_train = []
        Y_train = []
        X_test = []
        Y_test = []
        repetitions_number = [4, 48, 40, 3]
        for i in range(len(input_data)):
            counter[target[i]] += 1
            if counter[target[i]] <= repetitions_number[target[i]]:
                X_train.append(input_data[i])
                Y_train.append(target[i])
            else:
                if target[i] == 2:
                    for k in range(20):
                        counter[target[i]] += 1
                        X_test.append(input_data[i])
                        Y_test.append(target[i])
                X_test.append(input_data[i])
                Y_test.append(target[i])

        const = 1000
        clf = svm.SVC()
        lab_enc = preprocessing.LabelEncoder()
        Y_train = lab_enc.fit_transform(Y_train * const)
        X_train *= const

        print(clf.fit(X_train, Y_train))
        predict = clf.predict(X_test)

        coincidence = {0: 0, 1: 0, 2: 0, 3: 0}
        for i in range(len(predict)):
            if Y_test[i] == predict[i]:
                coincidence[predict[i]] += 1
        sum = 0
        for i in coincidence.values():
            sum += i
        used_methods = [m[0] for m in methods]
        work_result = sum / len(Y_test)
        with open('result.txt', 'a') as file:
            file.write(' '.join(used_methods) + '\n')
            file.write(str(work_result) + '\n')
