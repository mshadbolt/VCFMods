import vcf, os, csv, glob, sys
os.chdir("/Users/marionshadbolt/Dropbox/000_Masters/BINF90002-Research-Project/Analysis/PythonDev/")
filename = glob.glob('*.csv')

#read in csv with info on + or - strand information, two columns tag_id, strand
csvfile = open(filename[0], "rb")
csvreader = csv.reader(csvfile)
StrandDict = dict()
for row in csvreader:
        StrandDict[str(row[0])] = row[1]

#read in your vcf file
vcfname = raw_input("Enter the full name of the vcf to be modified:\n")
print "Thank you, now modifying your vcf and saving to " + vcfname.split(".")[0] + "-mod.vcf ..."
vcf_reader = vcf.Reader(open(vcfname,'r'))
PosDict = dict()
for record in vcf_reader:
    SNPID = str(record.ID) + '_' + str(record.POS)
    PosDict[SNPID] = record.POS

PosDictMod = PosDict.copy()

for key in PosDictMod:
    tag_id = key.split("_")[0]
    if StrandDict[tag_id] == '+':
        PosDictMod[key] += 1
    else:
        PosDictMod[key] -= 1

vcf_reader2= vcf.Reader(open(vcfname,'r'))
modVcfname = vcfname.split(".")[0] + "-mod.vcf"
vcf_writer = vcf.Writer(open(modVcfname, 'w'), vcf_reader2)
for record in vcf_reader2:
    tag_id = str(record.ID) + '_' + str(record.POS)
    record.POS = PosDictMod[tag_id]
    vcf_writer.write_record(record)
    
print "done!"


    
