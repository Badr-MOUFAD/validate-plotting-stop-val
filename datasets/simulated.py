from benchopt import BaseDataset, safe_import_context


class Dataset(BaseDataset):

    name = "Simulated"

    parameters = {
        'a, b': [
            (2, -5),
            (4, 3),
        ]
    }

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_data(self):
        return dict(a=self.a, b=self.b)
