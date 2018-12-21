import subprocess
import glob

for input_fastq in glob.glob('*.fastq'):
  base = input_fastq.split('_')[0]
  class_command = '/tools/kraken2-master/kraken2 --db /tools/kraken2-master/nt ' + input_fastq + ' --output ' + base + '_kraken_out --report ' + base + '_kraken_report --classified-out ' + base + '_classified_out --unclassified-out ' + base + '_unclassified_out'
  subprocess.call(class_command, shell=True)