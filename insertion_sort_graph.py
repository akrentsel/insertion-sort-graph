import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random

def plot_cont(gen):
    y_vals, red_index = next(gen)
    xmax = len(y_vals) ** 2
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    def update(i):
        y_vals, red_index = next(gen)
        red_bar = [0] * len(y_vals)
        red_bar[red_index] = y_vals[red_index]

        x = range(len(y_vals))
        ax.clear()
        ax.bar(x, y_vals, width=1)
        ax.bar(x, red_bar, width =1, color="red")
        print('Iteration: ', i)

    a = anim.FuncAnimation(fig, update, frames=xmax, repeat=False)
    plt.show()



def insertion_sort_step_generator(ls):
	assert len(ls) > 1, "Length of list must be greater than 1 to sort"
	curr = 1;

	def swap(pos1, pos2):
		nonlocal ls
		ls[pos1], ls[pos2] = ls[pos2], ls[pos1]

	while curr < len(ls):
		temp = curr
		while curr > 0 and ls[curr] < ls[curr - 1]:
			swap(curr, curr - 1)
			curr = curr - 1
			yield ls, curr


		if curr != temp:
			curr = temp + 1
		else:
			curr = curr + 1
			yield ls, curr
	yield ls, len(ls) - 1

number_of_elements_in_list = 25 # Change this number to change the number of elements in the list to be sorted

rand_ls = []
for _ in range(number_of_elements_in_list):
	rand_ls += [random.randrange(1, 200)]

# rand_ls = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]        # Worst case senario - reverse order given. θ(n^2)

plot_cont(insertion_sort_step_generator(rand_ls))
