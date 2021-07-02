#Program to implement IPC using Shared Memory
#import necessary packages
from multiprocessing import shared_memory,Process
import multiprocessing
import numpy as np

#read process
def read():
	#attach sharedMemoryRead to the existing 'read_write_memory'
	sharedMemoryRead = shared_memory.SharedMemory(name="read_write_memory")
	print(np.asarray(sharedMemoryRead.buf[:5]))#read data from buffer
	sharedMemoryRead.close()#close sharedMemoryRead

#write process
def write():
	#attach sharedMemoryWrite to the existing 'read_write_memory'
	sharedMemoryWrite = shared_memory.SharedMemory(name="read_write_memory")
	sharedMemoryWrite.buf[5:7]=bytearray([6,7])#append 2 more numbers in buffer
	print(np.asarray(sharedMemoryWrite.buf[:7]))#print current state of buffer
	sharedMemoryWrite.close()#close sharedMemoryWrite

#edit process
def edit():
	#attach sharedMemoryEdit to the existing 'read_write_memory'
	sharedMemoryEdit = shared_memory.SharedMemory(name="read_write_memory")
	sharedMemoryEdit.buf[0:2]=bytearray([8,9])#Edit the array positions 0,1
	print(np.asarray(sharedMemoryEdit.buf[:7]))#print current state of buffer
	sharedMemoryEdit.close()#close sharedMemoryEdit

#main function
if __name__ == '__main__':

	#create a shared memory space named 'read_write_memory' of size 10 bytes
	sharedMemory = shared_memory.SharedMemory(name="read_write_memory",create=True,size=10)

	#initialize the shared memory buffer with some list elements (bytearray)
	sharedMemory.buf[:5]=bytearray([1,2,3,4,5])

	print('Starting read process...')
	#create a read process
	readProcess = Process(target=read())
	#start the read process
	readProcess.start()
	#call read.join() to block execution of further statements until this process is completed
	readProcess.join()
	print('Read process completed!')

	print('\nStarting write process...')
	#create a write process
	writeProcess = Process(target=write())
	#start the write process
	writeProcess.start()
	writeProcess.join()
	print('Write process completed!')

	print('\nStarting edit process...')
	#create a edit process
	editProcess = Process(target=edit())
	#start the edit process
	editProcess.start()
	editProcess.join()
	print('Edit process completed!')

	#close the sharedMemory for the main process
	sharedMemory.close()
	#unlink sharedMemory to destroy it completely
	sharedMemory.unlink()


