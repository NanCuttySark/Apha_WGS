# -*- coding: utf-8 -*-
import os


# paths for IITP cluster:
# pri_path = '/home/ishtar/Glycines'
# sec_path = '_Gly/vs_all_bact_'

# path for Roma's cluster:
pri_path = '~/Yulya/Glycines'
sec_path = '_Gly/vs_all_bact_'

for i in range(1, 21):
    input_file_name = str('Gly_' + str(i) + '_vs_all_bact_global_k5_bowtie.sam')
    output_file_name = str('shorten_Gly_' + str(i) + '_vs_all_bact_k5_bowtie.pseudosam')
    outFile = open(output_file_name, "w")

    full_path = os.path.join(pri_path, str(i) + sec_path + str(i) + '_Gly')
    input_file_path = os.path.join(full_path, input_file_name)
    output_file_path = os.path.join(full_path, output_file_name)

    inFile = open(input_file_name, "r")
    # print(fileName)
    count = 0
    for line in inFile:
        count += 1
        if line[0] == "@":
            continue
        temp = line.split("\t")
        if temp[2] != "*":
            outFile.write(line)
    outFile.close()

    # outFile=open("apha_extract_unique_alignments.pseudosam","w")
    # outFile.close()
