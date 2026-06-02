import random
import csv
import statistics
import matplotlib.pyplot as plt


# ==================================================
# Dice Probability Simulator Project
# Author: Aatif Hussain Bhat
# Language: Python
# ==================================================


def display_title():
    print("=" * 50)
    print("        DICE PROBABILITY SIMULATOR")
    print("=" * 50)
    print()


def get_number_of_rolls():
    while True:
        try:
            rolls = int(input("Enter number of dice rolls: "))
            if rolls > 0:
                return rolls
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter an integer.")


def simulate_dice_rolls(total_rolls):
    frequencies = [0, 0, 0, 0, 0, 0]
    roll_history = []

    for _ in range(total_rolls):
        roll = random.randint(1, 6)
        frequencies[roll - 1] += 1
        roll_history.append(roll)

    return frequencies, roll_history


def calculate_theoretical_probability():
    return [1 / 6] * 6


def calculate_experimental_probability(frequencies, total_rolls):
    probabilities = []

    for frequency in frequencies:
        probabilities.append(frequency / total_rolls)

    return probabilities


def calculate_percentage(probabilities):
    percentages = []

    for probability in probabilities:
        percentages.append(probability * 100)

    return percentages


def display_frequencies(frequencies):
    print("\nFrequency Distribution")
    print("-" * 40)

    for i in range(6):
        print(f"Face {i+1} : {frequencies[i]}")


def display_probabilities(theoretical, experimental):
    print("\nProbability Comparison")
    print("-" * 40)

    for i in range(6):
        print(
            f"Face {i+1} "
            f"| Theoretical = {theoretical[i]:.4f} "
            f"| Experimental = {experimental[i]:.4f}"
        )


def display_percentages(percentages):
    print("\nExperimental Percentages")
    print("-" * 40)

    for i in range(6):
        print(f"Face {i+1}: {percentages[i]:.2f}%")


def calculate_statistics(history):
    mean_value = statistics.mean(history)
    median_value = statistics.median(history)

    try:
        mode_value = statistics.mode(history)
    except:
        mode_value = "No Unique Mode"

    return mean_value, median_value, mode_value


def display_statistics(mean_value, median_value, mode_value):
    print("\nStatistical Analysis")
    print("-" * 40)
    print("Mean   :", mean_value)
    print("Median :", median_value)
    print("Mode   :", mode_value)


def save_results_to_csv(
    frequencies,
    theoretical,
    experimental,
    percentages
):
    filename = "simulation_results.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "Face",
                "Frequency",
                "Theoretical",
                "Experimental",
                "Percentage"
            ]
        )

        for i in range(6):
            writer.writerow(
                [
                    i + 1,
                    frequencies[i],
                    theoretical[i],
                    experimental[i],
                    percentages[i]
                ]
            )

    print("\nResults saved to", filename)


def plot_bar_chart(theoretical, experimental):
    faces = [1, 2, 3, 4, 5, 6]

    width = 0.35

    x1 = [x - width / 2 for x in faces]
    x2 = [x + width / 2 for x in faces]

    plt.figure(figsize=(10, 6))

    plt.bar(
        x1,
        theoretical,
        width=width,
        label="Theoretical Probability"
    )

    plt.bar(
        x2,
        experimental,
        width=width,
        label="Experimental Probability"
    )

    plt.xlabel("Dice Face")
    plt.ylabel("Probability")
    plt.title("Dice Probability Comparison")
    plt.xticks(faces)
    plt.legend()
    plt.grid(True)

    plt.show()


def plot_frequency_chart(frequencies):
    faces = [1, 2, 3, 4, 5, 6]

    plt.figure(figsize=(10, 6))

    plt.bar(
        faces,
        frequencies
    )

    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.title("Frequency Distribution of Dice Rolls")

    plt.grid(True)

    plt.show()


def display_summary(total_rolls):
    print("\nProject Summary")
    print("-" * 40)
    print("Total Dice Rolls:", total_rolls)
    print("Simulation Completed Successfully")


def main():

    display_title()

    total_rolls = get_number_of_rolls()

    frequencies, history = simulate_dice_rolls(
        total_rolls
    )

    theoretical = calculate_theoretical_probability()

    experimental = calculate_experimental_probability(
        frequencies,
        total_rolls
    )

    percentages = calculate_percentage(
        experimental
    )

    display_frequencies(
        frequencies
    )

    display_probabilities(
        theoretical,
        experimental
    )

    display_percentages(
        percentages
    )

    mean_value, median_value, mode_value = (
        calculate_statistics(history)
    )

    display_statistics(
        mean_value,
        median_value,
        mode_value
    )

    save_results_to_csv(
        frequencies,
        theoretical,
        experimental,
        percentages
    )

    plot_bar_chart(
        theoretical,
        experimental
    )

    plot_frequency_chart(
        frequencies
    )

    display_summary(
        total_rolls
    )

if __name__ == "__main__":
    main()
