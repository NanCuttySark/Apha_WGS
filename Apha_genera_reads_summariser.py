import os
import pandas as pd
import csv

# paths for cluster version

primary_path = '/home/ishtar/Glycines'
sec_path = '_Gly/vs_all_bact_'

# for local run (and don't forget to comment full_path):

# full_path = '/home/ishtar/PycharmProjects/Aphids/Data'

table_list = []

for i in range(1, 22):
    file_name = str('bowtie_summary_Gly_' + str(i) + '_ext_all_mpq1_unique')

    full_path = os.path.join(primary_path, str(i) + sec_path + str(i))
    input_file_path = os.path.join(full_path, file_name)

    genera_list = []
    reads_number_list = []
    with open(input_file_path, 'r') as _filehandler:
        csv_file_reader = csv.reader(_filehandler, delimiter='\t')
        for row in csv_file_reader:
            reads_number = int(row[1])
            if reads_number < 500:
                break

            reads_number_list.append(row[1])
            genera_list.append(row[0])

    sample_dict = {'Genera': genera_list, 'Reads_count': reads_number_list}
    sample = str('Gly_' + str(i))

    globals()['df{}'.format(i)] = pd.DataFrame(sample_dict).T
    globals()['df{}'.format(i)].columns = globals()['df{}'.format(i)].iloc[0]
    globals()['df{}'.format(i)] = globals()['df{}'.format(i)][1:]
    idx_rename = {'Reads_count': sample}
    globals()['df{}'.format(i)] = globals()['df{}'.format(i)].rename(index=idx_rename)


    # output_file_name = str('genera_counts_bowtie_all_bact' + str(i) + '_Gly.csv')
    # output_file_path = os.path.join(full_path, output_file_name)
    #
    # genera_abundance_table.to_csv(output_file_path, sep='\t')


# all_samples_abundance_table = pd.concat([df1, df2])


all_samples_abundance_table = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10,
                                         df11, df12, df13, df14, df15, df16, df17, df18, df19,
                                         df20, df21])

all_samples_abundance_table = all_samples_abundance_table.fillna(0)
output_file_name = 'genera_abundance_table_all_Gly.csv'
output_file_path = os.path.join(primary_path, output_file_name)
all_samples_abundance_table.to_csv(output_file_path, sep='\t')
