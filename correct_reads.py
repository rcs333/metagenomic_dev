import subprocess
input_fastq_1 = 'CG_S578_L001_R1_001.preprocessed.fastq'
input_fastq_2 = 'CG_S578_L001_R2_001.preprocessed.fastq'
 
base = 'CG'



repair_cmd = '/tools/bbmap/repair.sh in=' + input_fastq_1 + ' in2=' + input_fastq_2 + ' out=' + base + '_1_corrected.fastq out2=' + base + '_2_corrected.fastq outs=' + base + '_single.fastq'

subprocess.call(repair_cmd, shell=True)
