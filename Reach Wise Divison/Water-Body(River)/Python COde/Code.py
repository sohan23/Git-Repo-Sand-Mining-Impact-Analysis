import os
import pandas as pd

folder_path = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Water-Body(River)\scratch'
output_file = 'output.xlsx'

area_sums = {}

for file in os.listdir(folder_path):
    if file.endswith('.xls'):
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        area_sum = df['Area'].sum()
        area_sums[file] = area_sum

output_df = pd.DataFrame(list(area_sums.items()), columns=['Filename', 'Area Sum'])
output_df.to_excel(output_file, index=False)