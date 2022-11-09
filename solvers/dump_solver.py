from benchopt import BaseSolver


class Solver(BaseSolver):
    name = 'Dump solver'

    parameters = {
        'dumpiness': ['very-dump', 'pretty-smarter'],
    }

    def __init__(self, dumpiness):
        self.dumpiness = dumpiness

    def set_objective(self, a, b):
        self.a, self.b = a, b

    def run(self, n_iter):
        self.x = 0.
        for _ in range(n_iter):
            if self.dumpiness == 'very-dump':
                self.x -= 1
            elif self.dumpiness == 'pretty-smarter':
                self.x -= self.a

    def get_result(self):
        return self.x
