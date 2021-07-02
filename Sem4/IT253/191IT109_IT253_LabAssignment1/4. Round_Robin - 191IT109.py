#Round Robin Scheduling Algorithm
import copy

n=int(input('Enter no. of Processes:'))
process_data=[] #to store all parameters of each process(will be a nested list)
for i in range(n): #get input
	print('Process',i+1,':')
	process_id = int(input('Enter process id:'))
	arrival_time= int(input('Enter arrival time:'))
	burst_time=int(input('Enter burst time:'))
	process_data.append([process_id,arrival_time,burst_time,0,0])
	#second last parameter: whether process is pushed in queue(boolean)
	#last parameter: whether process has been completed(boolean)

quantum=int(input('Enter time quantum:'))#user input time quantum

process_data_copy=copy.deepcopy(process_data)#copy values of process data in a new list

#find least arrival time
time=100000
for i in range(n):
	temp = process_data_copy[i][1]
	if temp<time:
		time=temp

completed=0 #count of no. of processes completed
completion_time=[] #process id,completion time,TAT and wait time for each process in nested list
process_data_copy.sort(key = (lambda x: x[1])) #sort according to arrival time

queue_data=[] #process data of processes currently in queue

#push processes in queue at initial time
for i in range(n):
	if process_data_copy[i][1]<=time and process_data_copy[i][3]==0:
		queue_data.append(process_data_copy[i])
		process_data_copy[i][3]=1

while completed!=n: #loop until all processes are completed
	curr=queue_data.pop(0) #pop first element from queue
	if curr[2]<=quantum: #if remaining time of process to be executed is less than time quantum
		time+=curr[2] #i.e. process will get completed
		for i in range(n): #search for the process and store completion time and update parameters
			if(process_data_copy[i][0]==curr[0]):
				process_data_copy[i][4]=1
				completion_time.append([curr[0],time])
				completed+=1
		for i in range(n): #append newly arrived processes not in queue at current system time
			if process_data_copy[i][1]<=time and process_data_copy[i][3]==0:
				queue_data.append(process_data_copy[i])
				process_data_copy[i][3]=1
	else: #process gets partially completed
		time+=quantum
		for i in range(n): #subtract time quantum from remaining burst time
			if(process_data_copy[i][0]==curr[0]):
				process_data_copy[i][2]-=quantum
				to_push=process_data_copy[i]
		for i in range(n): #append newly arrived processes not in queue at current system time
			if process_data_copy[i][1]<=time and process_data_copy[i][3]==0:
				queue_data.append(process_data_copy[i])
				process_data_copy[i][3]=1
		queue_data.append(to_push) #append this process at the end of queue

process_data.sort(key=lambda x:x[0]) #sort original contents of processes according to id
completion_time.sort(key=lambda x: x[0]) #sort according to id
for i in range(n):
	completion_time[i].append(completion_time[i][1]-process_data[i][1]) #append turn around time
	completion_time[i].append(completion_time[i][2]-process_data[i][2]) #append waiting time

#calculate avg turn around time and avg waiting time
avg_tat=0
avg_wt=0
for i in range(n):
	avg_tat+=completion_time[i][2]
	avg_wt+= completion_time[i][3]
avg_tat/=n
avg_wt/=n

#Print data to console
print('\nProcess Id\tArrival\t     Burst\tCompletion\tTurnAround\t   Waiting')
for i in range(n):
	print(process_data[i][0],'\t\t',process_data[i][1],'\t\t',process_data[i][2],'\t\t'
		,completion_time[i][1],'\t\t',completion_time[i][2],'\t\t',completion_time[i][3],'\t')

print('\nAverage Turn Around time:',avg_tat)
print('Average waiting time:',avg_wt)



	
