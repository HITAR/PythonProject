import threading
import time
import random
from multiprocessing import Queue

idle = threading.Semaphore(value=2)
# busy = threading.Semaphore(value=0)
# sem = threading.Semaphore(value=1)


def producer(q):
    idle.acquire()
    #sem.acquire()
    for i in list(range(1,101)):
        q.put(i)
        print("Producer %s: %d" %(threading.current_thread().name,i))
        time.sleep(random.random())
    # sem.release()
    # busy.release()
    idle.release()
    print("Producer finished.")

def consumer(q):
    idle.acquire()
    # busy.acquire()
    # sem.acquire()
    while True:
        try:
            val = q.get(block=True,timeout=2)
            print("Consumer %s: %d" %(threading.current_thread().name,val))
            time.sleep(1)
        except:
            break
    #sem.release()
    idle.release()
    print("consumer finished.")

if __name__ == '__main__':
    q = Queue()
    t1 = threading.Thread(target=producer,name='p',args=(q,))
    t2 = threading.Thread(target=consumer,name='v1',args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
