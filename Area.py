import os
import pandas as pd
import matplotlib.pyplot as plt
# Replace 'path/to/folder' with the path to the folder containing your XLS files
folder_path = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison\Excel Table'
output_path = 'F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Reach Wise Divison'
# Create an empty DataFrame to hold the results
results_df = pd.DataFrame(columns=['Area'])

# Loop through all xls files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xls"):
        file_path = os.path.join(folder_path, filename)

        # Load the xls file into a pandas dataframe
        df = pd.read_excel(file_path, usecols=["Area"])

    # Calculate the sum of the 'Area' column
    area_sum = df['Area'].sum()
    
    # Extract the file name from the full path and add it as a new column to the results_df
    file_name = os.path.splitext(os.path.basename(filename))[0]

    # Append the result to the results_df
    results_df = results_df.append({'File Name':filename,'Area': area_sum}, ignore_index=True)

 
print(results_df)

#Save the results_df to a CSV file in the same folder as the input XLS files
results_path = os.path.join(output_path, 'Area-all.csv')
results_df.to_csv(results_path, index=False)

# # # Plot the results
# # results_df.plot(kind='bar', x='File Name', y='Area', title='Area', legend=False, fontsize=11)

# # Display the plot
# plt.plot(results_df["File Name"], results_df['Area'],marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)

# plt.show()
