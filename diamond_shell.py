import glob
import subprocess

for fasta in glob.glob('*.fasta'):
	base = fasta.split('_')[0]
	diamond_cmd = '/tools/diamond blastx -d /db/nr_fa/nr -q ' + fasta + ' -o ' + base + '.m8 --sensitive -p 20'
	subprocess.call(diamond_cmd, shell=True)