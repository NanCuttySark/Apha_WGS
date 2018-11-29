
# import numpy as np
import re


locNames = {}
locusFile = open("allBact_locusNames_extend", "r")
for line in locusFile:
    temp = line.strip().split("\t")
    temp2 = temp[1].split(".")[0]
    locNames[temp2] = temp[0]
locusFile.close()

bacNames = {}
bacNamesReverse = {}
bacNames_hL = {}
bacNamesReverse_hL = {}
dictFile = open("All_bact", "r")
for line in dictFile:
    line = re.sub("\[", "", line)
    line = re.sub("\]", "", line)
    line = re.sub("uncultured\s+", "", line)
    temp = line.strip().split("\t")
    temp2 = re.split("\s+", temp[1])
    temp3 = temp2[0]
    if len(temp2) >= 2:
        temp2 = temp2[0]
    else:
        temp2 = temp2[0]
    bacNames[temp[0]] = temp2
    if temp2 not in bacNamesReverse:
        bacNamesReverse[temp2]=temp[0]
    else:
        bacNamesReverse[temp2]=str(bacNamesReverse[temp2])+"\t"+str(temp[0])
    
    bacNames_hL[temp[0]]=temp3
    if temp3 not in bacNamesReverse_hL:
        bacNamesReverse_hL[temp3]=temp[0]
    else:
        bacNamesReverse_hL[temp3]=str(bacNamesReverse_hL[temp3])+"\t"+str(temp[0])
dictFile.close()
# print bacNamesReverse["Buchnera aphidicola"]
# 0/0

# quallity=[]
aligned = {}
alignedSet = {}
alignedSetMPQ = {}
# alignedSetMPQ_hL={}
readToSp20 = {}
readToSp10 = {}
not_unique20 = set()
not_unique10 = set()
# readToSp_hL = {}


for fileName in ["merg_glob_D_noxia_vs_all_bact_k5_bowtie.pseudosam"]: 
    inFile=open(fileName,"r")
    print(fileName)
    # count=0
    for line in inFile:
        # count+=1
        # if line[0]=="@":
        #    continue
        temp = line.split("\t")
        # if temp[2]!="*":
        locus=temp[2].split(".")[0]
        # quallity.append(float(temp[4]))
        if float(temp[4]) >= 20:
            if temp[0] in not_unique20:
                continue
            try:
                if bacNames[locNames[locus]] not in readToSp20[temp[0]]:
                    not_unique20.add(temp[0])
                    readToSp20.pop(temp[0])
                    not_unique10.add(temp[0])
                    if temp[0] in readToSp10:
                        readToSp10.pop(temp[0])
            except:
                readToSp20[temp[0]] = set()
                readToSp20[temp[0]].add(bacNames[locNames[locus]])
#            try:
#                readToSp_hL[temp[0]].add(bacNames_hL[locNames[locus]])
#            except:
#                readToSp_hL[temp[0]]=set()
#                readToSp_hL[temp[0]].add(bacNames_hL[locNames[locus]])
                
            try:
                alignedSet[bacNames[locNames[locus]]].add(temp[0])
                # aligned[bacNames[locNames[locus]]]+=1
            except:
                # print locNames[locus[1:]]
                alignedSet[bacNames[locNames[locus]]]=set()
                alignedSet[bacNames[locNames[locus]]].add(temp[0])
        if float(temp[4]) >= 1:
            if temp[0] in not_unique10:
                continue
            try:
                if bacNames[locNames[locus]] not in readToSp10[temp[0]]:
                    not_unique10.add(temp[0])
                    readToSp10.pop(temp[0])
            except:
                readToSp10[temp[0]] = set()
                readToSp10[temp[0]].add(bacNames[locNames[locus]])
            try:
                alignedSetMPQ[bacNames[locNames[locus]]].add(temp[0])
                # aligned[bacNames[locNames[locus]]]+=1
            except:
                # print locNames[locus[1:]]
                alignedSetMPQ[bacNames[locNames[locus]]] = set()
                alignedSetMPQ[bacNames[locNames[locus]]].add(temp[0])
            # try:
            #    alignedSetMPQ_hL[bacNames_hL[locNames[locus]]].add(temp[0])
            # except:
                #print locNames[locus[1:]]
            #    alignedSetMPQ_hL[bacNames_hL[locNames[locus]]]=set()
            #    alignedSetMPQ_hL[bacNames_hL[locNames[locus]]].add(temp[0])
                # aligned[bacNames[locNames[locus]]]=1
        # if count==200000:
            # print alignedSet
            # 0/0
        #    break          
    inFile.close()
    

print("----------")
print(len(not_unique10))
print(len(not_unique20))

    
for bac in alignedSet:
    aligned[bac]=len(alignedSet[bac]-not_unique20)
# print(aligned)
sortAl = sorted(aligned.keys(), key=lambda xT: aligned[xT], reverse=True)
# print np.mean(quallity)
# print np.median(quallity)
# print np.std(quallity)
outFile=open("bowtie_summary_genera_D_noxia_ext_all_mpq20_unique", "w")
for bac in sortAl:
    outFile.write(str(bac)+"\t"+str(aligned[bac])+"\t"+str(bacNamesReverse[bac])+"\n")
outFile.close()


aligned = {}
for bac in alignedSetMPQ:
    aligned[bac] = len(alignedSetMPQ[bac]-not_unique10)
# print aligned
sortAl = sorted(aligned.keys(), key=lambda xT: aligned[xT], reverse=True)

outFile = open("bowtie_summary_genera_D_noxia_ext_all_mpq1_unique", "w")
for bac in sortAl:
    outFile.write(str(bac)+"\t"+str(aligned[bac])+"\t"+str(bacNamesReverse[bac])+"\n")
outFile.close()


# aligned={}
# for bac in alignedSetMPQ_hL:
#    aligned[bac]=len(alignedSetMPQ_hL[bac]-not_unique)
# print aligned
# sortAl=sorted(aligned.keys(),key=lambda xT: aligned[xT],reverse=True)

# outFile=open("bowtie_summary_taxa_ext_all_mpq1_hL_unique","w")
# for bac in sortAl:
#    outFile.write(str(bac)+"\t"+str(aligned[bac])+"\t"+str(bacNamesReverse_hL[bac])+"\n")
# outFile.close()
