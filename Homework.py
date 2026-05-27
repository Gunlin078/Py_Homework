class Node:
    #Узел односвязного списк
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:    
    def __init__(self):
        self.front = None   # указатель на начало очереди (первый элемент)
        self.rear = None    # указатель на конец очереди (последний элемент)
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        #Добавление элемента в конец очереди
        new_node = Node(data)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def dequeue(self):
        #Удаление элемента из начала очереди
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        removed_data = self.front.data
        self.front = self.front.next
        
        # Если очередь стала пустой, обнуляем rear
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return removed_data
    
    def peek(self):
        #"Просмотр первого элемента
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.front.data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "Очередь: []"
        
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Очередь: [" + " <- ".join(elements) + "]"


class LinkedListStack:
    
    def __init__(self):
        self.top = None     # указатель на вершину стека
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        
        removed_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return removed_data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.top.data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "Стек: []"
        
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Стек: [" + " -> ".join(elements) + "] (вершина слева)"


# Примеры от дипсика
if __name__ == "__main__":
    print("=" * 40)
    print("РАБОТА С ОЧЕРЕДЬЮ")
    print("=" * 40)
    
    queue = LinkedListQueue()
    
    print("Добавляем элементы: 10, 20, 30")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    print(f"Размер очереди: {len(queue)}")
    print(f"Первый элемент: {queue.peek()}")
    
    print("\nУдаляем элемент:", queue.dequeue())
    print(queue)
    print(f"Удаляем элемент:", queue.dequeue())
    print(queue)
    print(f"Размер после удалений: {len(queue)}")
    
    print("\n" + "=" * 40)


    
    print("РАБОТА СО СТЕКОМ")
    print("=" * 40)
    
    stack = LinkedListStack()
    
    print("Добавляем элементы: 100, 200, 300")
    stack.push(100)
    stack.push(200)
    stack.push(300)
    print(stack)
    print(f"Размер стека: {len(stack)}")
    print(f"Вершина стека: {stack.peek()}")
    
    print("\nУдаляем элемент:", stack.pop())
    print(stack)
    print(f"Удаляем элемент:", stack.pop())
    print(stack)
    print(f"Размер после удалений: {len(stack)}")
    
    # Дополнительная демонстрация
    print("\n" + "=" * 40)
    print("ДОПОЛНИТЕЛЬНЫЕ ПРИМЕРЫ")
    print("=" * 40)
    
    # Очередь - добавление и удаление
    print("\nОчередь (FIFO - First In First Out):")
    q = LinkedListQueue()
    for i in range(5):
        q.enqueue(i)
        print(f"Добавили {i}: {q}")
    
    while not q.is_empty():
        print(f"Извлекли {q.dequeue()}: {q}")
    
    # Стек - добавление и удаление
    print("\nСтек (LIFO - Last In First Out):")
    s = LinkedListStack()
    for i in range(5):
        s.push(i)
        print(f"Добавили {i}: {s}")
    
    while not s.is_empty():
        print(f"Извлекли {s.pop()}: {s}")
