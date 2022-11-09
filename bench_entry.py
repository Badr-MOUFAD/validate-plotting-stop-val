from benchopt.benchmark import Benchmark
from benchopt import run_benchmark


bench = Benchmark('./')

run_benchmark(bench, max_runs=25,
              n_jobs=1, n_repetitions=1,
              dataset_names=['simulated'])
