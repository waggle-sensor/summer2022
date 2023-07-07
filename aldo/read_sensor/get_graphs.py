import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data_1sec_soil_temp.csv", delimiter=',', dtype=float)
interval = 1
x = np.arange(0, data.shape[0]*interval, interval)

fig, (axs1, axs2) = plt.subplots(2)
fig.suptitle('Buried Sensor in Soil and Added Iced Water', fontweight='bold')
fig.subplots_adjust(left=0.08, right=0.835, bottom=0.075, top=0.88, wspace=0.2, hspace=0.3)

axs1.plot(x, data[:, 0])
axs1.set_title('Moisture vs Time')
axs1.set_xlabel('Time (seconds)')
axs1.set_ylabel('Moisture (mV)')

axs2.plot(x, data[:, 1], '+')
axs2.set_title('Temperature vs Time')
axs2.set_xlabel('Time (seconds)')
axs2.set_ylabel('Temperature (mV)')


## Illustrative Details
# axs1.axvline(x=900, ls=':', color='pink', label='15 minutes')
# axs1.axvline(x=2700, ls=':', color='green', label='45 minutes')
# axs1.axvline(x=4500, ls=':', color='purple', label='75 minutes')
# axs1.axvline(x=6300, ls=':', color='red', label='105 minutes')
# axs1.axvline(x=8100, ls=':', color='black', label='135 minutes')

# axs2.axvline(x=900, ls=':', color='pink', label='15 minutes')
# axs2.axvline(x=2700, ls=':', color='green', label='45 minutes')
# axs2.axvline(x=4500, ls=':', color='purple', label='75 minutes')
# axs2.axvline(x=6300, ls=':', color='red', label='105 minutes')
# axs2.axvline(x=8100, ls=':', color='black', label='135 minutes')

# plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')

plt.show()
