import matplotlib.pyplot as plt
import numpy as np

months = list(range(1,13))
total_profits = [
    211000, 183300, 224700, 222700,
    209600, 201400, 295500, 361400,
    234000, 266700, 412800, 300200
]
plt.plot(months, total_profits, "o:r", mfc='blue', ms=5, lw=3, label='Total Profits')
plt.xlabel("Month number")
plt.ylabel("Total Profits")
plt.legend(loc="lower right")
plt.show()