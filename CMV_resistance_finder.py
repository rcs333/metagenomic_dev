import argparse
from Bio import SeqIO
from Bio.Seq import Seq
import subprocess 
import sys

def read_fasta(fasta_file_loc):
    strain_list = []
    genome_list = []
    dna_string = ''

    for line in open(fasta_file_loc):
        if line[0] == '>':
            strain_list.append(line[1:].split()[0])
        else:
            dna_string += line.strip()

    genome_list.append(dna_string)
    return strain_list, genome_list


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Script which will eventually form the backend for the CMV resitence marker detection')
	parser.add_argument('filepath', help='raw ab1 file for analysis')
	parser.add_argument('-gene', help='Specify the gene that is being analyzed - this can be passed somehow during the fileupload because each gene has a different box')

	try:
		args = parser.parse_args()
	except:
		parser.print_help()
		sys.exit(0)

	# we will garuntee that this will just be a string like UL56 
	gene = args.gene 

	# TODO: check file extension and handle 
	filepath = args.filepath
	base_name = filepath.split('.')[0]
	
	record = SeqIO.read(filepath, "abi")
	SeqIO.write(record, base_name + ".fasta", "fasta")
	subprocess.call('cat ' + gene + ' ' + base_name + ".fasta  > " + base_name + '.align.fasta', shell=True)
	subprocess.call('mafft --adjustdirection ' + base_name + ".align.fasta > " + base_name + ".ali.out.fasta", shell=True )

	records = list(SeqIO.parse(base_name + '.ali.out.fasta', 'fasta'))
	# grab the last one because we always order these in the same way
	SeqIO.write(records[1], 'query.fasta', 'fasta')
	name, sequence = read_fasta('query.fasta')
	sequence = sequence[0].replace('-','n')
	my_seq = Seq(sequence)
	function_output = str(my_seq.translate())


	# This string is exactly what the front end javascript takes
	print(function_output)








