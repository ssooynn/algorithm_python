class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size()

    def push(self, item):
        
        if self.stack1.size() == self.max_size:
            return False
        else:
            self.stack1.push(item)
            return True

    def pop(self):
        try:
            if self.stack1.size() == 0:
                raise emptyException

            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())

            item = self.stack2.pop()

            while self.stack2.size() > 0:
                self.stack1.push(self.stack2.pop())

            return item

        except emptyException:
            return False


class emptyException(Exception):
    pass


n, max_size = map(int, input().strip().split(' '))
q = MyQueue(max_size)
for _ in range(n):
    order = input()

    if order == "POP":
        print(q.pop())
    elif order == "SIZE":
        print(q.qsize())
    else:
        order, integer = order.strip().split(' ')
        print(q.push(int(integer)))
