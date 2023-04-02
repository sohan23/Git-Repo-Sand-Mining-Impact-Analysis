import pandas as pd
import openpyxl
# Define the folder names and their corresponding final column names
folder_a = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Bar Area\Plot'
folder_b = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Water-Body(River)\Plot'
name_a = 'Exposed-Bar'
name_b = 'Water'

# Read in the Excel files
df_a = pd.read_excel(f'{folder_a}/Bar-Area-Final-Updated.xlsx')
print(df_a)
df_b = pd.read_excel(f'{folder_b}/Water-Area-Final_All.xlsx')

# Rename the columns
df_a.columns = [f'{col}-{name_a}' for col in df_a.columns]
df_b.columns = [f'{col}-{name_b}' for col in df_b.columns]

# Concatenate the dataframes
df_concatenated = pd.concat([df_a, df_b], axis=1)
print(df_concatenated)
# Define the path to the output folder
output_folder = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\BAvsWA'

# Write the concatenated dataframe to an Excel file in the output folder
df_concatenated.to_excel(
    f'{output_folder}/concatenated_file.xlsx', index=False)
