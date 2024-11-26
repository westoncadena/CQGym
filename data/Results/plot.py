import matplotlib.pyplot as plt

# File path
file_path = "train09_58_28.rwd"

# Read the rewards from the file
with open(file_path, "r") as file:
    rewards = [float(line.strip()) for line in file]

# Plot the rewards
plt.figure(figsize=(10, 6))
plt.plot(rewards, label="Reward", marker="o", linestyle="-", markersize=5)
plt.title("Rewards Over Time", fontsize=16)
plt.xlabel("Step", fontsize=14)
plt.ylabel("Reward", fontsize=14)
plt.grid(True)
plt.legend()
plt.show()
