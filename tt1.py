import time, threading
print('本程序将进行比较，单线程和多线程的用时')
balance=0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread1(n):
    for i in range(200000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def run_thread2(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

if __name__ == '__main__':
    balance=0
    start1 = time.time()
    td = threading.Thread(target=run_thread1, args=(5,))
    td.start()
    td.join()
    end1 = time.time()
    timeuse1=end1-start1
    print('\nbalance最终结果:%d        单线程用时:%f 秒'%(balance,timeuse1))

    balance=0
    start2 = time.time()
    t1 = threading.Thread(target=run_thread2, args=(5,))
    t2 = threading.Thread(target=run_thread2, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end2 = time.time()
    timeuse2=end2-start2
    print('\nbalance最终结果:%d        多线程用时:%f 秒'%(balance,timeuse2))