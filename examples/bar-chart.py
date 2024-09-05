# Copied from matlibplot examples: https://matplotlib.org/stable/gallery/lines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py
# First install matplotlib and numpy by running: pip install matplotlib numpy

# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# # np.random.seed(19680801)

# # fig, ax = plt.subplots()

# # # Example data
# # people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# # y_pos = np.arange(len(people))
# # print(y_pos)
# # performance = 3 + 10 * np.random.rand(len(people))
# # error = np.random.rand(len(people))

# # ax.barh(y_pos, performance, xerr=error, align='center')
# # ax.set_yticks(y_pos, labels=people)
# # # ax.invert_yaxis()  # labels read top-to-bottom
# # ax.set_xlabel('Performance')
# # ax.set_title('How fast do you want to go today?')

# # plt.show()
# plt.style.use('_mpl-gallery')

# # make data
# x2 = np.linspace(0, 10, 25)
# y2 = 4 + 1 * np.sin(2 * x2)

# # plot
# fig, ax = plt.subplots()

# ax.plot(x2, y2, 'o-', linewidth=2)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10 Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots()
axs.plot(t, s1, t, s2)
axs.set_xlim(0, 2)
axs.set_xlabel('Time (s)')
axs.set_ylabel('s1 and s2')
axs.grid(True)

plt.show()



ax.xaxis.set_minor_locator(dates.HourLocator(interval=4))   # every 4 hours
ax.xaxis.set_minor_formatter(dates.DateFormatter('%H:%M'))  # hours and minutes