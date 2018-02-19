# python 2.7
# hothman https://github.com/hothman/NGS

import sys

def OpenSNPMummer(mummerSNPFile):
	with open(mummerSNPFile) as f:
		lines = f.readlines()
		lines=lines[1:] 
	return lines

def readLIST(listSNPFiles):
	with open(listSNPFiles) as f:
		lis = f.readlines()
	lis = [fileName[:-1] for fileName in lis]
	return lis

def MaxPos(lines):
	nuc_pos=[]
	
	for line in lines:
		position=int( (line.split('\t') )[0] )	
		nuc_pos.append( position )
	max_pos=max(nuc_pos)
	return list(max_pos*"-")

def concatOneSeq(AnemptyList, lines):
	"""
	This function modify the empty list and returns a dict 
	for the reference positions
	"""
	ref={}
	for line in lines:
		snp=line.split( '\t' )
		AnemptyList[int( snp[0] ) - 1]= snp[2]
		ref.update( { int( snp[0] ):snp[1] } )
	return ref
			
	

def concatSNPs(mummerSNPFile):
	lines=OpenSNPMummer(mummerSNPFile)
	concatenatedSNPs=MaxPos(lines)
	concatOneSeq(concatenatedSNPs, lines)	
	return ''.join(concatenatedSNPs)

def MultipleSNPs(listfile):
	SNPtable=[] ; referenceSNP={}
	for file in readLIST(listfile):
		lines=OpenSNPMummer(file)
		concatenatedSNPs=MaxPos(lines)
		container_dic=concatOneSeq(concatenatedSNPs, lines)
		referenceSNP.update(container_dic)
		SNPtable.append (''.join(concatenatedSNPs) )

	lenSeq=[len(elem) for elem in SNPtable]
	maxLen=max(lenSeq)
	
	for i, seq in enumerate(SNPtable):
		CharToAdd=(maxLen-len(seq))*'-'
		SNPtable[i]=seq+CharToAdd
	i=1
	
	# construct the variants of the reference 
	Seqref = list(maxLen*'-')
	for key, value in referenceSNP.items():
		Seqref[int(key)-1]=referenceSNP[key] 
	Seqref=''.join(Seqref)
	
	# output the cocatenated SNP
	print ">Reference"+"\n"+Seqref+"\n"
	for seq,file in zip(SNPtable, readLIST(listfile) ) :
		print ">sample"+str(i)+"|"+file+"\n"+seq+"\n"
		i+= 1

print "This is the name of the script: ", str(sys.argv)


MultipleSNPs(sys.argv[1])
