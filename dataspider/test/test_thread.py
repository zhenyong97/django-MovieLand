import threading
import queue
import time

class ProducerThread(threading.Thread):
    def __init__(self, queue):
        super(ProducerThread, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            data = self.produce_data()
            self.queue.put(data)
            print('生产者生产了数据：{}'.format(data))
            time.sleep(1)

    def produce_data(self):
        return time.time()  # 这里以时间戳作为示例数据

class ConsumerThread(threading.Thread):
    def __init__(self, queue):
        super(ConsumerThread, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            data = self.queue.get()
            self.consume_data(data)

    def consume_data(self, data):
        print('消费者消费了数据：{}'.format(data))
        # 在这里可以添加你需要处理消费结果的代码

if __name__ == '__main__':
    queue = queue.Queue()
    producer = ProducerThread(queue)
    consumer = ConsumerThread(queue)

    # 启动生产者和消费者线程
    producer.start()
    consumer.start()

    # 等待生产者和消费者线程结束
    producer.join()
    consumer.join()
