import numpy as np
import pandas as pd
import os
import openpyxl
# import matplotlib as mpl
import matplotlib.pyplot as plt
# import matplotlib.ticker as tck

input_folder = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Water-Body(River)\Plot'

output_folder = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Water-Body(River)\Plot'

excel_data = pd.read_excel('Water-Area.xlsx')
excel_data

sqm_to_sqkm = excel_data.iloc[:, 1:]/1000000
print(sqm_to_sqkm)


sqm_to_sqkm.insert(loc=0, column="Reach", value=range(1, len(sqm_to_sqkm)+1))
print(sqm_to_sqkm)


output_file_path = os.path.join(
    output_folder, "Water-Area-Final-Updated.csv")
sqm_to_sqkm.to_csv('Water-Area-Final-Updated.csv', index=False)
