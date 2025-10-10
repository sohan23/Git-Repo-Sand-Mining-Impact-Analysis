import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import openpyxl

print = os.getcwd()

# # Read the excel file
# df = pd.read_excel('F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\BAvsWA\concatenated_file-Plotting.xlsx')

# # Plot the 1965 Exposed Bar vs Water Area
# x = df.iloc[:, 0]
# Exposed_Bar = df['Mon-2018-Exposed-Bar']
# Water = df['Mon-2018-Water']

# bar_width = 0.35
# x1 = np.arange(len(x))
# x2 = [i + bar_width for i in x1]

# plt.bar(x1, Exposed_Bar, width=bar_width, color='orange', label='Exposed Bar')
# plt.bar(x2, Water, width=bar_width, color='blue', label='River Channel')
# plt.xticks([i + bar_width/2 for i in range(len(x))], x)
# plt.xlabel('Reach')
# plt.ylabel('Area in sq. km')
# title = 'Monsoon 2018 Exposed Bar vs Channel Area'
# plt.title(title, fontdict={'fontname': 'Times New Roman'})
# plt.grid(True, color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
# plt.legend()
# plt.show()


#plot Density
input_folder = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\BAvsWA'
df = pd.read_excel('Density.xlsx',sheet_name='Sheet1')
df2 = pd.read_excel('Density.xlsx',sheet_name='Sheet2')
df3 = pd.read_excel('Density.xlsx',sheet_name='Sheet3')
df4 = pd.read_excel('Density.xlsx',sheet_name='Sheet4')
plt.plot(df['Reach'], df['Density-Pre-2017'], color='red', marker='o', linewidth=2, markersize=5)
plt.plot(df2['Reach'], df2['Density-Mon-2017'], color='blue', marker='o', linewidth=2, markersize=5)
plt.plot(df3['Reach'], df3['Density-Post-2017'], color='green', marker='o', linewidth=2, markersize=5)
plt.xlabel('Reach')
plt.ylabel('Density as (BA/CA)')
plt.legend()
title = 'Bar Density 2017' 
plt.title(title, fontdict={'fontname': 'Times New Roman'})
plt.grid(True, color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

plt.show()
