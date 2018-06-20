class Admixture:
    def __init__(self, key, value):
        admixtures = {'001': 'suspended solids', '002': 'sulfur dioxide', '004': 'carbon monoxide',
                      '005': 'nitrogen dioxide', '012': 'solid fluorides', '013': 'hydrogen fluoride'}
        self.name = admixtures[key]
        self.value = value

    def __repr__(self):
        return 'name: {0.name}, value: {0.value}'.format(self)
