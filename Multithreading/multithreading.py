"""
Threads are subsets of process in the computer in execution,
Multithreading is the way of multitasking.

"""
import threading

# A simple function 
def print_power(base, index):
    return base**index

if __name__ == "__main__":

    thread1 = threading.Thread(target = print_power,args = (2,4))

    thread2 = threading.Thread(target = print_power,args = (3,2))
    
    # threads started
    thread1.start()
    thread2.start()

    # current program execution paused
    thread1.join()
    thread2.join()

    print("All threads executed")

