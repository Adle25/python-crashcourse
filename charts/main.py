import matplotlib.pyplot as plt
import plotly.express as px
from random_walk import RandomWalk
from die import Die


# Line plot
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# ax.set_title('Square numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Square of avlue', fontsize=14)
# ax.tick_params(labelsize=14)
# plt.show()

# Scatter plot
# x_values = range(1, 1000)
# y_values = [x**2 for x in x_values]
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)
# ax.axis([0, 1100, 0, 1_000_000])
# ax.ticklabel_format(style='plain')
# plt.show()

# Random walk
# rw = RandomWalk()
# rw.fill_walk()

# plt.style.use('classic')
# fix, ax = plt.subplots()
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
# ax.set_aspect('equal')
# ax.scatter(0, 0, c='green', edgecolors='none', s=100)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
# plt.show()

# Plotly
die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []

poss_results = range(1, die.num_sides+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = 'Results of Rolling One D6 1,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()