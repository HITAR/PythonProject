#!/usr/bin/env python3

from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
import os, time, random, threading

#--------------------------------------------------


def childproc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    print("Parent Process %s" %os.getpid())
    p = Process(target=childproc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

#--------------------------------------------------


def long_time_task(name):
    print("Run task %s(%s)" %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def run_pool():
    print("Parent Process %s" % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    p.close()
    p.join()
    print("Success.")


#--------------------------------------------------


def write(q):
    print("Process %s write." %os.getpid())
    for value in ['A', 'B', 'C']:
        print("write %s to q" %value)
        q.put(value)
        #print q
        time.sleep(random.random())


def read(q):
    print("Process %s read." %os.getpid())
    while True:
        value = q.get()
        print(value)
        print("read %s from q" %value)




def run_commu():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


def thread():
    print('%s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('%s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('%s ended.' % threading.current_thread().name)


def run_thread():
    print('%s is running' % threading.current_thread().name)
    t = threading.Thread(target=thread)
    t.start()
    t.join()
    print('%s ended.' % threading.current_thread().name)

if __name__ == "__main__":
    #run_pool()
    #run_commu()
    run_thread()