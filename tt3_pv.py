import random
import threading
import time
from queue import Queue


class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self,name=t_name)
        self.queue = queue

    def run(self):
        for i in range(101):    #随机产生10个数字 ，可以修改为任意大小
            randomnum = random.randint(1,100)
            print("%s is producing %d to the queue!" % (self.getName(), randomnum))
            self.queue.put(randomnum)
            time.sleep(random.random())
        print("%s finished!" %(self.getName()))


class Consumer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.queue = queue

    def run(self):
        while 1:
            try:
                val_even = self.queue.get(1,5)  #get(self, block=True, timeout=None) ,1就是阻塞等待,5是超时5秒
                print("%s is consuming. %d in the queue is consumed!" % (self.getName(),val_even))
                time.sleep(2)
            except:
                print("%s finished!" %(self.getName()))
                break


def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer.', queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print('All threads terminate!')

if __name__ == '__main__':
    main()