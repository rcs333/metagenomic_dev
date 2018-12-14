import subprocess

BLAST_DB = '/Users/uwvirongs/Downloads/centrifuge/nt.blast'
input_fasta = 'R-kid3/scaffolds.fasta'
output_base = 'R-kid3'

blast_cmd = 'blastn -task megablast -db ' + BLAST_DB + ' -query ' + input_fasta + ' -num_alignments 1 -num_descriptions 7 -outfmt "7 staxids sscinames" -out ' + output_formatting_test.blast_results + ' -num_threads 6'
subprocess.call(blast_cmd, shell=True)





