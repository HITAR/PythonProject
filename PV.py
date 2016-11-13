import threading
import time
import random
import queue
from multiprocessing import Queue

idle = threading.Semaphore(value=2)
busy = threading.Semaphore(value=0)
sem = threading.Semaphore(value=1)


def producer(q):
    idle.acquire()
    #sem.acquire()
    for i in list(range(1,11)):
        q.put(i)
        print("Producer %s: %d" %(threading.current_thread().name,i))
        time.sleep(random.randrange(1,2)*0.5)
    # sem.release()
    # busy.release()
    idle.release()

def consumer(q):
    idle.acquire()
    # busy.acquire()
    # sem.acquire()
    while(True):
        try:
            val = q.get(block=True,timeout=5)
            print("Consumer %s: %d" %(threading.current_thread().name,val))
            time.sleep(random.randrange(1,3))
        except:
            break
    #sem.release()
    idle.release()

if __name__ == '__main__':
    q = Queue(maxsize=10)
    t1 = threading.Thread(target=producer,name='p',args=(q,))
    t2 = threading.Thread(target=consumer,name='v1',args=(q,))
    # t3 = threading.Thread(target=consumer,name='v2',args=(q,))
    # t4 = threading.Thread(target=consumer,name='v3',args=(q,))
    t1.start()
    t2.start()
    # t3.start()
    # t4.start()
    t1.join()
    t2.join()

    # t3.join()
    # t4.join()
