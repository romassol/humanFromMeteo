import os


def get_all_file_names(dir):
    result = os.listdir(dir)
    for i, f in enumerate(result):
        result[i] = dir + '\\' + result[i]
    return result

class Constants:
    patients_file = "data\\ONMK2015nevr.xls"
    ekb_meteo_file = "data\\Meteo\\Екатеринбург-метеоданные 2015 Лист Microsoft Excel 97-2003.xls"
    ku_meteo_file = "data\\Meteo\\Каменск-Ур-метеоданные-2015 Лист Microsoft Excel 97-2003.xls"

    ekb_admixture_dir = 'C:\\учеба\\курсовая 2 курс\\data\\Gidromet_dannye_2017\\Екатеринбург'
    ekb_admixtures_files = get_all_file_names(ekb_admixture_dir)


if __name__ == '__main__':
    print(Constants.disease_file_name)