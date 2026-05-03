import matplotlib.pyplot as plt

def plot_fp(p_values, measured, theoretical):
    plt.figure()

    plt.plot(p_values, measured, marker='o', label='Measured FP')
    plt.plot(p_values, theoretical, marker='x', linestyle='--', label='Theoretical FP')

    plt.xlabel("Target False Positive Rate (p)")
    plt.ylabel("Actual False Positive Rate")
    plt.title("Bloom Filter: Theoretical vs Measured FP Rate")

    plt.legend()
    plt.grid()

    plt.show()