## NGS 

This script allow to use mummer contigs alignment with different samples aligned to a reference genome. 
The first code `align_contigs_GetSNPs.sh.sh`, allows to assemble contigs using `nucmer` and generates a variant tab delimited file (headers + SNV), with options `-CHIlrT`. 

##### Usage

```bash
$ ./align_contigs_GetSNPs.sh.sh filelist ref_geneome
```
zied was here

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


The other script `ConcatSNPsMummer.py` concatenates the SNPs from each mummer snp table into a FASTA like file and outputs the results to STDOUT.

usage :

``` bash
$ python ConcatSNPsMummer.py LIST
```
`LIST` is a list contains the path to the SNP table for each line.
exemple:

```
/somedir1/somedir2/sample1.snp
../somedir3/sample2.snp
./somedir4/sample3.snp

```
The contigs must be assembled from the same reference genome. Otherwise you will get wrong results. 
