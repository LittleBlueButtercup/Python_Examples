# Import numpy and set seed
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Simulate random walk 20 times to plot a picture of what will roughly happen
all_walks = []
for i in range(20) :
    random_walk = [0]
	# Roll dice 100x
	for x in range(100) :
		# Set step: last element in random_walk
		step = random_walk[-1]

		# Roll the dice
		dice = np.random.randint(1,7)

		# Determine next step
		if dice <= 2:
			# Use max to make sure step can't go below 0
			step = max(0, step - 1)
		elif dice <= 5:
			step = step + 1
		else:
			step = step + np.random.randint(1,7)

		# Implement clumsiness
			if np.random.rand() <= 0.005 :
				step = 0
		
		# append next_step to random_walk
		random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

plt.clf()

#Now going to run the simulation 500x to obtain odds of winning (Step 60 and over)

all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

count = 0
for i in ends :
    if i >= 60 :
        count = count + 1
print("Over 60: " + str(count))
print("Percentage: " + str(count/500))

# Plot histogram of ends, display plot
plt.hist(ends)
plt.xlabel("Final Step")
plt.ylabel("# of occurances")
plt.show()