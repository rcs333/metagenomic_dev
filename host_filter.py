import subprocess





DB_LOCATION = 'rabbit_genome/rabbit'
input_fastq = 'R-testR-interleaved.fastq'
output_base = 'R-testR'


align_cmd = 'bowtie2 --very-sensitive-local --threads 8 -x ' + DB_LOCATION + ' -q --interleaved ' + input_fastq + ' -S ' + output_base + '_mappedSam 2>&1 | tee -a ' + output_base + '.log'
subprocess.call(align_cmd, shell=True)

sort_cmd = 'samtools view -Sb ' + output_base + '_mappedSam > ' + output_base + '_mappedBam' 
subprocess.call(sort_cmd, shell=True)

sort_cmd2 = 'samtools sort -O bam -T temp -o ' + output_base + '_sortedBam ' + output_base + '_mappedBam'
subprocess.call(sort_cmd2, shell=True)

index_cmd = 'samtools index -b ' + output_base + '_sortedBam'
subprocess.call(index_cmd, shell=True)

r1_cmd = 'samtools view -F 0x40 ' + output_base + '_mappedBam | awk \'{if($3 == \"*\") print \"@\" $1 \"\\n\" $10 \"\\n\" \"+\" $1 \"\\n\" $11}\' > ' + output_base + '_host_filtered_R1.fastq'
r2_cmd = 'samtools view -f 0x40 ' + output_base + '_mappedBam | awk \'{if($3 == \"*\") print \"@\" $1 \"\\n\" $10 \"\\n\" \"+\" $1 \"\\n\" $11}\' > ' + output_base + '_host_filtered_R2.fastq'
subprocess.call(r1_cmd, shell=True)
subprocess.call(r2_cmd, shell=True)

# to output coverage stats
 #for f in *.log;  do echo $f >> final.txt; cat $f >> final.txt; done