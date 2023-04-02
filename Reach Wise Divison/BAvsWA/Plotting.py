import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import openpyxl

print = os.getcwd()

# Read the excel file
df = pd.read_excel('F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\BAvsWA\concatenated_file-Plotting.xlsx')

# Plot the 1965 Exposed Bar vs Water Area
x = df.iloc[:, 0]
Exposed_Bar = df['Mon-2020-Exposed-Bar']
Water = df['Mon-2020-Water']

bar_width = 0.35
x1 = np.arange(len(x))
x2 = [i + bar_width for i in x1]

plt.bar(x1, Exposed_Bar, width=bar_width, color='orange', label='Exposed Bar')
plt.bar(x2, Water, width=bar_width, color='blue', label='Water Area')
plt.xticks([i + bar_width/2 for i in range(len(x))], x)
plt.xlabel('Reach')
plt.ylabel('Area in sq. km')
title = 'Monsoon 2020 Exposed Bar vs Water Area'
plt.title(title, fontdict={'fontname': 'Times New Roman'})
plt.legend()
plt.show()
