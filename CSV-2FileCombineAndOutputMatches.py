import csv

def compare_and_merge_csv(file1, file1_column, file2, file2_column, output_file):
    with open(file1, mode='r', newline='', encoding='utf-8-sig') as f1:
        reader1 = csv.DictReader(f1)
        print("Columns in file 1:", reader1.fieldnames)  # Debug print
        data1 = [row for row in reader1]

    with open(file2, mode='r', newline='', encoding='utf-8-sig') as f2:
        reader2 = csv.DictReader(f2)
        print("Columns in file 2:", reader2.fieldnames)
        data2 = [row for row in reader2]

    matches = []
    for row1 in data1:
        for row2 in data2:
            if row1.get(file1_column, '').strip() == row2.get(file2_column, '').strip():
                # Combine the matching rows into one dictionary
                combined_row = {**row1, **row2}
                matches.append(combined_row)

    combined_columns = reader1.fieldnames + [col for col in reader2.fieldnames if col not in reader1.fieldnames]

    with open(output_file, mode='w', newline='') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=combined_columns)
        writer.writeheader()
        writer.writerows(matches)

file1_path = 'file1.csv'  # Update this to your first CSV file path
file2_path = 'file2.csv'  # Update this to your second CSV file path
output_file_path = 'output.csv'  # Update this to your desired output CSV file path
file1_column_name = 'CName'  # Update this to the column name in your first CSV file to compare
file2_column_name = 'CName'  # Update this to the column name in your second CSV file to compare

compare_and_merge_csv(file1_path, file1_column_name, file2_path, file2_column_name, output_file_path)

print("Merging completed. Check the output file:", output_file_path)
