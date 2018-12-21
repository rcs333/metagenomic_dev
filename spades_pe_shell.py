import subprocess 
import glob 

for fastq_file in glob.glob('*_out.fastq'):
  print(fastq_file)
  base = fastq_file.split('_unclassified_out')[0]
  r1 = fastq_file
  #r2 = base + '_unclas_R2.fastq'
  
  spades_cmd = '/tools/SPAdes-3.13.0-Linux/bin/spades.py -s ' + r1 + ' -o ' + base + '_direct_from_kraken '
  subprocess.call(spades_cmd, shell=True)
  
  
