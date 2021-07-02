#SJF non-Preemptive Scheduling Algorithm
n=int(input('Enter no. of Processes:'))
process_data=[] #to store all parameters of each process(will be a nested list)
for i in range(n): #get input
	print('Process',i+1,':')
	process_id = int(input('Enter process id:'))
	arrival_time= int(input('Enter arrival time:'))
	burst_time=int(input('Enter burst time:'))
	process_data.append([process_id,arrival_time,burst_time,0]) #last parameter: whether process has been completed(boolean)

time=0 #current time
completed=0 #count of no. of processes completed
completion_time=[] #process id,completion time,TAT and wait time for each process in nested list
process_data.sort(key = (lambda x: x[1])) #sort according to arrival time
queue_data=[] #process data of processes currently in queue
while completed!=n: #loop until all processes are completed
	for i in range(len(process_data)): #push already arrived processes which are not yet completed in queue_data[]
		if process_data[i][1]<=time and process_data[i][3]==0:
			queue_data.append(process_data[i])
	queue_data.sort(key = (lambda x: x[2])) #sort according to burst time
	if(len(queue_data)<1): #if queue is empty
		time+=1
		continue
	curr=queue_data.pop(0) #pop first element from queue
	time+=curr[2] #execute process completely as non-preemptive
	for i in range(len(process_data)): #search for process and upate parameters
		if(process_data[i][0]==curr[0]):
			process_data[i][3]=1
	completion_time.append([curr[0],time])
	completed+=1
	queue_data.clear() #clear the current state of queue

process_data.sort(key=lambda x:x[0]) #sort according to id
completion_time.sort(key=lambda x: x[0]) #sort according to id
for i in range(n):
	completion_time[i].append(completion_time[i][1]-process_data[i][1]) #append turn around time
	completion_time[i].append(completion_time[i][2]-process_data[i][2]) #append waiitng time

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









	

