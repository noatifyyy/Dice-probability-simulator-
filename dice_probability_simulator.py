import random
import matplotlib.pyplot as plt

rolls = 1000
results = [0] * 6

for _ in range(rolls):
    results[random.randint(1, 6) - 1] += 1

experimental = [x / rolls for x in results]
theoretical = [1/6] * 6

faces = [1, 2, 3, 4, 5, 6]

plt.bar(faces, theoretical, alpha=0.6, label="Theoretical")
plt.bar(faces, experimental, alpha=0.6, label="Experimental")
plt.xlabel("Dice Face")
plt.ylabel("Probability")
plt.title("Dice Probability Simulator")
plt.legend()
plt.show()
