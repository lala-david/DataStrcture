class PrintManager:
    def __init__(self):
        # 배열 생성 
        self.queue = []

    def queue_print_job(self, document):
        # 큐 추가 
        self.queue.append(document)

    def run(self):
        # 큐 삭제 pop 
        while self.queue:
            self.print(self.queue.pop(0))

    def print(self, document):
        print(document)

print_manager = PrintManager()
print_manager.queue_print_job("First Document")
print_manager.queue_print_job("Second Document")
print_manager.queue_print_job("Third Document")
print_manager.run()