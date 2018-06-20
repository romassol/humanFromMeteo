class FinalDiagnosis:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    def __str__(self):
        return 'id: {0.id}, description: {0.description}'.format(self)

    def __eq__(self, other):
        return self.id == other.id and self.description == other.description

    def __hash__(self):
        return hash(self.id) * hash(self.id) + hash(self.description)
