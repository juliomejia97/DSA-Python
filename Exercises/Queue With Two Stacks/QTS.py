class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def sizeQueue(self):
        return len(self.s1)+len(self.s2)

    def isEmpty(self):
        return len(self.s1) == 0 and len(self.s2) == 0

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if(len(self.s2) == 0):
            while(len(self.s1) > 0):
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def front(self):
        if(len(self.s2) == 0):
            while(len(self.s1) > 0):
                self.s2.append(self.s1.pop())
        return self.s2[-1]


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    queries = int(first_multiple_input[0])

    q = Queue()
    while(queries > 0):
        second_multiple_input = input().rstrip().split()
        option = int(second_multiple_input[0])
        if option == 1:
            value = int(second_multiple_input[1])
            q.enqueue(value)
        if option == 2:
            q.dequeue()
        if option == 3:
            print(q.front())
        queries -= 1
