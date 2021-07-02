#FCFS Scheduling

def partition(list1,list2,list3, low, high): 
    i = (low-1)
    pivot = list1[high]
    for j in range(low, high):  
        if list1[j] <= pivot: 
            i = i+1
            list1[i], list1[j] = list1[j], list1[i] 
            list2[i], list2[j] = list2[j], list2[i] 
            list3[i], list3[j] = list3[j], list3[i] 
    list1[i+1], list1[high] = list1[high], list1[i+1] 
    list2[i+1], list2[high] = list2[high], list2[i+1] 
    list3[i+1], list3[high] = list3[high], list3[i+1] 
    return (i+1) 

#Sort list1 and make simultaneous changes in list2 and list3
def quickSort(list1,list2,list3,low,high): 
    if low < high: 
        pi = partition(list1,list2,list3, low, high) 
        quickSort(list1,list2,list3, low, pi-1) 
        quickSort(list1,list2,list3, pi+1, high)

#get input from user
def getInput():
	n=int(input('Enter no. of Processes:'))
	print('Processes will be assumed as 1 to',n,'in order')
	arrival_times=[] #store all arrival times
	print('Enter arrival times of processes(',n,'integers,one on each line):')
	it=1
	processes=[] #processes will be auto assigned as 1,2..n
	for _ in range(n):
		processes.append(it)
		it+=1
		arr=int(input())
		arrival_times.append(arr)
	burst_times=[]
	print('Enter burst times of processes(',n,'integers,one on each line):')
	for _ in range(n):
		burst=int(input())
		burst_times.append(burst)

	return processes,arrival_times,burst_times

#calculate turn around time and waiting times
def calculateParameters(processes, arrival_times, burst_times):
	waiting_times=[]
	turn_around_times=[]
	waiting_times.append(0)
	for i in range(1,len(processes)): #simplified formula to calculate waiting time
		waiting_times.append(burst_times[i-1]+waiting_times[i-1]-arrival_times[i]+arrival_times[i-1])
	for i in range(len(processes)): #simplified formula to caluculate turn around time
		turn_around_times.append(burst_times[i]+waiting_times[i])

	return turn_around_times,waiting_times


def fcfs_scheduling(processes, arrival_times, burst_times):
	quickSort(arrival_times,processes,burst_times,0,len(processes)-1) #sort according to arrival time
	turn_around_times , waiting_times = calculateParameters(processes, arrival_times, burst_times)
	print('******FINAL ANSWER (FCFS SCHEDULING)******')

	print('\nProcess Id\tTurnAround     Waiting')
	for i in range(len(processes)):
		print(processes[i],'\t\t',turn_around_times[i],'\t\t',waiting_times[i])

	avg_tat = sum(turn_around_times)/len(turn_around_times)
	avg_wt = sum(waiting_times)/len(waiting_times)
	print('\nAverage Waiting time    :',avg_wt)
	print('Average turn around time:',avg_tat)



processes, arrival_times, burst_times = getInput()
fcfs_scheduling(processes,arrival_times,burst_times)

