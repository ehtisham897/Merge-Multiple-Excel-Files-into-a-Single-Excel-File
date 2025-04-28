import pandas as pd
import os

# Folder path where Excel files are located
folder_path = 'C:\\Users\\Ehtisham\\Desktop\\Excel_Files' # Change this path accordingly

# List all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Create an empty DataFrame to store merged data
merged_data = pd.DataFrame()

# Loop through all Excel files and merge them
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    data = pd.read_excel(file_path)
    merged_data = pd.concat([merged_data, data], ignore_index=True)

# Save the merged data to a new Excel file
merged_data.to_excel('merged_file.xlsx', index=False)

print("Excel files merged successfully!")
