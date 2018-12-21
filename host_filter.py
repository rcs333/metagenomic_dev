import subprocess





DB_LOCATION = '/db/rabbit/rabbit_wg'
input_fastq_1 = 'Nic-Lysis_S14_L001_R1_001.preprocessed.fastq'
#input_fastq_2 = '/home/ryan/t_pal_test/RW_2_corrected.fastq'
output_base = 'Nic-Lysis'


align_cmd = 'bowtie2 --very-sensitive-local --threads 42 -x ' + DB_LOCATION + ' -q -U ' + input_fastq_1 + ' -S ' + output_base + '_mappedSam 2>&1 | tee -a ' + output_base + '.log'
subprocess.call(align_cmd, shell=True)

sort_cmd = 'samtools view -Sb ' + output_base + '_mappedSam > ' + output_base + '_mappedBam' 
subprocess.call(sort_cmd, shell=True)

sort_cmd2 = 'samtools sort ' + output_base + '_mappedBam ' + output_base +  '_sorted'
subprocess.call(sort_cmd2, shell=True)

index_cmd = 'samtools index ' + output_base + '_sorted.bam'
subprocess.call(index_cmd, shell=True)

r1_cmd = 'samtools view -F 0x40 ' + output_base + '_mappedBam | awk \'{if($3 == \"*\") print \"@\" $1 \"\\n\" $10 \"\\n\" \"+\" $1 \"\\n\" $11}\' > ' + output_base + '_host_filtered_R1.fastq'
#r2_cmd = 'samtools view -f 0x40 ' + output_base + '_mappedBam | awk \'{if($3 == \"*\") print \"@\" $1 \"\\n\" $10 \"\\n\" \"+\" $1 \"\\n\" $11}\' > ' + output_base + '_host_filtered_R2.fastq'
subprocess.call(r1_cmd, shell=True)
#subprocess.call(r2_cmd, shell=True)

# to output coverage stats
 #for f in *.log;  do echo $f >> final.txt; cat $f >> final.txt; done

 # for human host filtering
 #  bowtie2 --very-sensitive-local --threads 8 -x /Users/uwvirongs/Documents/metagenomic_pipeline_dev/human/hg18/hg18 -q 4991_S101_L001_R1_001.preprocessed.fastq -S SC4991_mappedSam 


#time /tools/kraken2-master/kraken2 --db /tools/kraken2-master/nt t_pal_test/RW_host_filtered_R1.fastq --output RW_kraken_out --report RW_kraken_report --classified-out RW_classified_out --unclassified-out RW_unclassified_out