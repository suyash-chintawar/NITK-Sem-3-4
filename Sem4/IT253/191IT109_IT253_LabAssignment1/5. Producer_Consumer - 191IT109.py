from threading import Thread, Semaphore
import time
import random       

pc_buffer = [] #producer-consumer buffer
MAX_SIZE = 15 #max length of buffer

mutex = Semaphore(1) #mutex semaphore initialized to 1
full = Semaphore(0) #full semaphore initialized to 0
empty= Semaphore(MAX_SIZE) #empty semaphore initialized to MAX_SIZE


class Producer(Thread):
    def run(self):
        items = range(5)
        global pc_buffer
        
        while True:
            item = random.choice(items) #item to be produced
            print('Produced',item)
            empty.acquire() #wait(empty)
            mutex.acquire() #wait(mutex)
            pc_buffer.append(item) #put item in buffer
            print('Appended',item)
            mutex.release() #signal(mutex)
            full.release() #signal(full)
            time.sleep(random.random()) #to decrease program speed

class Consumer(Thread):
    def run(self):
        global pc_buffer
        
        while True:
            full.acquire() #wait(full)
            mutex.acquire() #wait(mutex)
            item=pc_buffer.pop(0)
            mutex.release() #signal(mutex)
            empty.release() #signal(empty)
            print('Consumed',item) #consume an item
            time.sleep(random.random()) #to decrease program speed


Producer().start() #start producer thread
Consumer().start() #start consumer thread
