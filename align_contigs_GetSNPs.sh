#!/usr/bin/bash
filename="$1"
refgenome="$2"

while read -r line
do
    name="$line"
    filename="${name%.*}"
    dirname="${filename}_Aln+SNPs"
    mkdir $dirname
    echo "Proceeding $name" 
    echo "########### Aligning the contigs"
    nucmer  -p $filename  $refgenome  $line
    echo "########## Generate SNP file"   
    show-snps -CHIlrT "${filename}.delta" | awk '$5 > 20' |awk '$6 > 50'  >"${filename}.snp" 
    echo "                  "
    mv "${filename}.delta" $dirname
    mv "${filename}.snp" $dirname
    
    
    


done < "$filename"
