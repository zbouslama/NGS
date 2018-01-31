## NGS 

This script allow to use mummer contigs alignment with different samples aligned to a reference genome. 

##### Usage

`bash
$ ./multiMummer.sh filelist ref_geneome
`

`filelist` contains a list of the paths to the sample genome filename in FASTA format. 
Exemple:

`
sample1.fa
sample2.fa
sample3.fa
`
refgenome must be in fasta format. 

**Output**: A series of directories, each contains a delta file and the SNP table relative to each sample.
example: 

```bash 
sample1_Aln+SNPs/
sample2_Aln+SNPs/
```





