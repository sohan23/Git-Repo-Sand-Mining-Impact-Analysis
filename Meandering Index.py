import pandas as pd
import os
import matplotlib.pyplot as plt
# Set the path to the folder containing the xls files
input_folder_path = "F:\One Drive\OneDrive - Indian Institute of Science Education and Research Bhopal\Excel data for Various Parameters\Meandering Index"

# Create an empty dataframe to hold the concatenated data
result = pd.DataFrame()

# Loop through all xls files in the folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".xls"):
        file_path = os.path.join(input_folder_path, filename)

        # Load the xls file into a pandas dataframe
        df = pd.read_excel(file_path, usecols=["Length"])

        # Add the Length column to the result dataframe
        result[filename] = df["Length"]/4000
print(result)
# Add a new column containing a serial number
result.insert(loc=0, column="Serial Number", value=range(1, len(result)+1))

# Save the result to an excel file in the input folder
output_file_path = os.path.join(input_folder_path, "Meandering-Final.csv")
result.to_csv(output_file_path, index=False)

print("The Length columns from all files have been concatenated and saved to Meandering-Final.csv in the input folder.")

# Plot the results
# result.plot(kind='bar', x='Serial Number', y='result',
#                 title='Length', legend=False, fontsize=11)

# # Display the plot
plt.plot(result["Serial Number"], result['Meandering-1965_TableToExcel.xls'],marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=3,label='1965')
plt.title('Meandering Index-1965', fontsize=13)
plt.xlabel('Serial Number', fontsize=11)
plt.ylabel('Meandering Index', fontsize=11)
plt.legend()
plt.show()

plt.plot(result["Serial Number"], result['TableToExcel_Mon-2016.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Mon-2016')
plt.plot(result["Serial Number"], result['TableToExcel_Post-2016.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Post-2016')
plt.plot(result["Serial Number"], result['TableToExcel_Pre-2017.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Pre-2017')
plt.plot(result["Serial Number"], result['TableToExcel_Mon-2017.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Mon-2017')
plt.plot(result["Serial Number"], result['TableToExcel_Post-2017.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Post-2017')
plt.plot(result["Serial Number"], result['TableToExcel_Pre-2018.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Pre-2018')
plt.plot(result["Serial Number"], result['TableToExcel_Mon-2018.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Mon-2018')
plt.plot(result["Serial Number"], result['TableToExcel_Post-2018.xls'],marker='o', markerfacecolor='violet', markersize=9, color='pink', linewidth=3,label='Post-2018')
l
plt.title('Meandering Index-2016-2018', fontsize=13)
plt.xlabel('Serial Number', fontsize=11)
plt.ylabel('Meandering Index', fontsize=11)
plt.legend()
plt.show()
# plt.plot(result["Serial Number"], result['TableToExcel_Post-2016.xls'],
#          marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)

# plt.plot(result["Serial Number"], result['TableToExcel_Pre-2017.xls'],
#             marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)
# plt.text(9.09, 3877, 'Pre-2017', fontsize=11, color='blue')
# plt.plot(result["Serial Number"], result['TableToExcel_Mon-2017.xls'],
#             marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)
# plt.plot(result["Serial Number"], result['TableToExcel_Post-2017.xls'],
#             marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)
# plt.plot(result["Serial Number"], result['TableToExcel_Pre-2018.xls'],
#             marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)
# plt.plot(result["Serial Number"], result['TableToExcel_Mon-2018.xls'],
#             marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)
# plt.plot(result["Serial Number"], result['TableToExcel_Post-2018.xls'],
#             marker='s', markerfacecolor='blue', markersize=9, color='skyblue', linewidth=4)
plt.show()