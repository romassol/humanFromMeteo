from FinalDiagnosis import FinalDiagnosis
import datetime
from dateutil.relativedelta import relativedelta


class TreatmentOutcome:
    def __init__(self, outcome):
        outcomes = {'Без перемен': 0, 'Улучшение': 1, 'Ухудшение': 2, 'Выздоровление': 3}
        self.outcome = outcomes[outcome]


class Patient:
    def __init__(self, id, final_diagnosis_id, final_diagnosis_description, birthdate,
                 treatment_start_date, statement_date, icd, ib_number, treatment_outcome,
                 result, retirement_rankine, admission_rankine):
        self.id = id
        self.final_diagnosis = FinalDiagnosis(final_diagnosis_id, final_diagnosis_description)
        self.birthdate = get_date(birthdate)
        self.treatment_start_date = get_date(treatment_start_date)
        self.statement_date = get_date(statement_date)
        self.icd = icd
        self.ib_number = ib_number
        self.treatment_outcome = TreatmentOutcome(treatment_outcome).outcome
        self.result = result
        self.retirement_rankine = retirement_rankine
        self.admission_rankine = admission_rankine
        ages = {20: 0, 40: 1, 60: 2, 300: 3}
        for age in ages:
            if self.birthdate > years_ago(age):
                self.age = ages[age]
                break

    def to_array(self):
        return [self.final_diagnosis.id[1:], self.age,
                (self.statement_date - self.treatment_start_date).total_seconds()]

    def __repr__(self):
        return 'id: {0.id}\n' \
               'final_diagnosis: {0.final_diagnosis}\n' \
               'birthdate: {0.birthdate}\n' \
               'treatment_start_date: {0.treatment_start_date}\n' \
               'statement_date: {0.statement_date}\n' \
               'icd: {0.icd}\n' \
               'ib_number: {0.ib_number}\n' \
               'treatment_outcome: {0.treatment_outcome}\n' \
               'result: {0.result}\n' \
               'retirement_rankine: {0.retirement_rankine}\n' \
               'admission_rankine: {0.admission_rankine}'.format(self)


def get_date(input_date):
    if type(input_date) is str:
        date = input_date.split('.')
        return datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    return datetime.datetime(1899, 12, 30) + datetime.timedelta(days=int(input_date))


def years_ago(years, from_date=None):
    if from_date is None:
        from_date = datetime.datetime.now()
    return from_date - relativedelta(years=years)

