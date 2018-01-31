## NGS 

This script allow to use mummer contigs alignment with different samples aligned to a reference genome. 

##### Usage

```bash
$ ./align_contigs_GetSNPs.sh.sh filelist ref_geneome
```

`filelist` contains a list of the paths to the sample genome filename in FASTA format. 
Exemple:

```
sample1.fa
sample2.fa
sample3.fa
```
refgenome must be in fasta format. 

**Output**: A series of directories, each contains a delta file and the SNP table relative to each sample.
example: 

```bash 
sample1_Aln+SNPs/
sample2_Aln+SNPs/
```
Source code for mummer and instructions to install the software can be found [here](https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz) and
 [here](https://github.com/mummer4/mummer/blob/master/INSTALL.md). 



