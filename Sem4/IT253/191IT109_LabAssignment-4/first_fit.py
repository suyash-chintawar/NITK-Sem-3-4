#First-Fit memory allocation algorithm using fixed partitioning
num_blocks=int(input('Enter no. of blocks in memory:'))#number of blocks
block_sizes=[]#sizes of each block
print('Enter size of each block:')
for i in range(1,num_blocks+1):
	block_sizes.append(int(input(' Block '+str(i)+': ')))

occupied=[0]*num_blocks#boolean to check whether block is occupied or not

num_processes=int(input('Enter no. of processes:'))#number of processes
process_sizes=[]#sizes of each process
print('Enter size of each process:')
for i in range(1,num_processes+1):
	process_sizes.append(int(input(' Process '+str(i)+': ')))

allocated=[-1]*num_processes#keep track of blocks allocated to each process, -1 if not allotted

#for each process find first free block which has size greater than size of process
for i in range(num_processes):
	idx=-1
	for j in range(num_blocks):
		if occupied[j]==0 and block_sizes[j]>=process_sizes[i]:
			idx=j
			break
	if idx!=-1:
		allocated[i]=idx
		occupied[idx]=1

#Print output to console
print('Process\tProcessSize\tBLock\tBlockSize')
for i in range(num_processes):
	print(i+1,'\t',process_sizes[i],end='\t\t')
	if allocated[i]!=-1:
		print(allocated[i]+1,'\t',block_sizes[allocated[i]])
	else:
		print('N/A\t  N/A')
