import csv

def tsv_to_csv(inputas_tsv_file_path, outputas_csv_file_path):
    with open(inputas_tsv_file_path, 'r') as tsv_file, open(outputas_csv_file_path, 'w', newline='') as csv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        csv_writer = csv.writer(csv_file)
        for row in tsv_reader:
            csv_writer.writerow(row)

