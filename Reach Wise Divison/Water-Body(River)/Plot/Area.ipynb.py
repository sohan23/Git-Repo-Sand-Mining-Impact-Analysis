# %% [markdown]
# ## Starting Importing all the necessary packages for the analysis

# %%
import numpy as np
import pandas as pd
import os
import openpyxl
# import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = 'white'
# import matplotlib.ticker as tck
%matplotlib inline


# %% [markdown]
# ## Set path for input folder

# %%
input_folder = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Bar Area\Plot'

# %% [markdown]
# ## Set path for output folder

# %%
output_folder = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Bar Area\Plot'


# %% [markdown]
# ### Create empty dataset frame to hold the concatenated data

# %%
# Read the excel file
# Load the xlsx file
excel_data = pd.read_excel('Area-Final.xlsx')
excel_data.head()

# %%
sqm_to_sqkm = excel_data.iloc[:, 1:]/1000000
print(sqm_to_sqkm)

# %%
# Add a new column containing a serial number
sqm_to_sqkm.insert(loc=0, column="Reach", value=range(1, len(sqm_to_sqkm)+1))
print(sqm_to_sqkm)


# %%
# Save the excel file
output_file_path = os.path.join(
    output_folder, "Area-Final-Updated.csv")
sqm_to_sqkm.to_csv('Area-Final-Updated.csv', index=False)


# %%
Plot = pd.read_csv('Area-Final-Updated.csv')
Plot

# %%
'''
This is the sqm_to_sqkm of the exposed sand areas for the various reaches of the river Yamuna for the years 1965 vs Monsooon 2016-2020
'''
plt.bar(sqm_to_sqkm['Reach'], sqm_to_sqkm['Mon-2016'], label='Mon-2016')
plt.bar(sqm_to_sqkm['Reach'], sqm_to_sqkm['Mon-2017'], label='Mon-2017')
plt.bar(sqm_to_sqkm['Reach'], sqm_to_sqkm['Mon-2018'], label='Mon-2018')
plt.bar(sqm_to_sqkm['Reach'], sqm_to_sqkm['Mon-2019'], label='Mon-2019')
plt.bar(sqm_to_sqkm['Reach'], sqm_to_sqkm['Mon-2020'], label='Mon-2020')
plt.title("Area of Exposed Sand")

plt.xlabel("Reach")
plt.ylabel("Area (sqkm)")
plt.legend()
plt.show()

# %%
