import re
from Bio import SeqIO
import numpy as np

inF = open("/home/ishtar/PycharmProjects/Aphids/Data/assembly_summary.txt", "r")
outFile = open("/home/ishtar/PycharmProjects/Aphids/Data/Bact_genera_genomes_med_length.csv", "w")


bacLen = {}

for line in inF:
    url = 0
    if re.search("representative|reference", line):
        temp = line.strip().split("	")
        url = temp[19]
        bacName = temp[7]
        bacName = re.sub("uncultured\s+", "", bacName)
        print(bacName)
        bN = bacName.split(" ")
        if len(bN) >= 2:
            bacNameShort = bN[0]
            bacNameShort = re.sub("\[", "", bacNameShort)
            bacNameShort = re.sub("\]", "", bacNameShort)
            fileName = str(url.split("/")[-1])
            totalLen = 0
            genome = SeqIO.parse("folder/"+str(fileName), "fasta")
            for part in genome:
                totalLen += len(part.seq)
            if bacNameShort in bacLen:
                bacLen[bacNameShort].append(totalLen)
            else:
                bacLen[bacNameShort] = [totalLen]
inF.close()

for bac in bacLen:
    outFile.write(str(bac)+"\t"+str(np.median(bacLen[bac]))+"\n")
outFile.close()
