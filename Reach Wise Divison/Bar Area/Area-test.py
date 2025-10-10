import pandas as pd
import os

# Set directory path where Excel files are stored
# path = 'F:\\One Drive\\OneDrive - Indian Institute of Science Education and Research Bhopal\\Excel data for Various Parameters\\Reach Wise Divison\\Excel Table'
# output_path = 'F:\\One Drive\\OneDrive - Indian Institute of Science Education and Research Bhopal\\Excel data for Various Parameters\\Reach Wise Divison'
# List all Excel files in the directory
files = os.listdir(path)
excel_files = [f for f in files if f.endswith(".xls")]

# Create an empty DataFrame to store the output
output = pd.DataFrame()

# Loop through each Excel file
for file in excel_files:
    # Read Excel file into a DataFrame
    df = pd.read_excel(os.path.join(path, file))
    # Calculate the sum of the Area column
    sum_area = df["Area"].sum()
    # Create a new DataFrame with a single row and column for the sum of the Area column
    sum_area_df = pd.DataFrame({"Sum Area": [sum_area]})
    print(sum_area_df)
    # Write the new DataFrame to the Excel file below the existing data
    writer = pd.ExcelWriter(os.path.join(path, file),
                            engine='openpyxl', mode='a')
    sum_area_df.to_excel(writer, index=False, header=False,
                         startrow=df.shape[0]+2)
    writer.save()
