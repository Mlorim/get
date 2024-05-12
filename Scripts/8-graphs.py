import matplotlib.pyplot as plt
import numpy as np


with open("settings.txt", 'r') as settings:
    tmp = [float(i[:-1]) for i in settings.readlines()]

dt = tmp[1]

# collecting data from data file
data_array = np.loadtxt("data.txt", dtype=int)
data_array = data_array*3.3/256
n = len(data_array)
times = np.linspace(0, dt*(n-1), n)

fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(times, data_array, color='g', label='V(t)')
ax.legend()

# set lims
min_v = data_array.min()
max_v = data_array.max()
max_t = n*dt
ax.set_ylim(min_v, 3.3)
ax.set_xlim(0, max_t)

# micro markers and grid
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')

# x, y and graph title
ax.set_title("Зарядка кондесатора", wrap=True)
ax.set_ylabel("Напряжение, B")
ax.set_xlabel("Время, с")

# placing text
y = max_v/2
x = max_t*0.75

ax.text(x, y, f'Время зарядки = {round(max_t, 3)} c')

plt.show()