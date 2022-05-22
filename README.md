# psi_to_prof_for_acdc
A script for transfer psi file to prof file for acdc stability prediction.\n
psi file is one of the outputs for hhlits. Just use as python psi_to_prof.py omi.psi omi.prof.\n
hhblits -i wt.fasta -o wt.hhr -d path/uniclust30_2018_08 -cpu 40 -norealign -maxmem 10 -oa3m wt.a3m -opsi wt.psi -B 5000 -Z 5000
