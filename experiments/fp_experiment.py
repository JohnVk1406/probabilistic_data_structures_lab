import random
import string

from src.bloom_filter import BloomFilter
from . import plot_fp as plot

random.seed(42)

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def run_experiment(n=1000, fp_rate=0.01, test_queries=5000, use_mmh3=False):
    bf = BloomFilter(n=n, fp_rate=fp_rate, use_mmh3=use_mmh3)

    inserted = set()

    for _ in range(n):
        s = random_string()
        inserted.add(s)
        bf.add(s)

    false_positives = 0
    total_tests = 0

    while total_tests < test_queries:
        s = random_string()

        if s in inserted:
            continue  # skipping true positives

        total_tests += 1

        if bf.contains(s):
            false_positives += 1

    measured_fp = false_positives / total_tests
    print(f"m (bit array size): {bf.size}")
    print(f"k (num hashes): {bf.num_hashes}")
    print(f"Theoretical FP rate: {fp_rate}")
    print(f"Measured FP rate: {measured_fp}")

    return measured_fp, fp_rate

p_values = [0.1, 0.05, 0.01, 0.005, 0.001]

measured = []
theoretical = []

for p in p_values:
    m_fp, t_fp = run_experiment(n=1000, fp_rate=p, test_queries=20000)
    measured.append(m_fp)
    theoretical.append(t_fp)

plot.plot_fp(p_values, measured, theoretical)