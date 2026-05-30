class Node:
    #Узел односвязного списк
    def __init__(this, data):
        this.data_ = data
        this.next_ = None


class LinkedListQueue:    
    def __init__(this):
        this.front_ = None   # указатель на начало очереди (первый элемент)
        this.rear_ = None    # указатель на конец очереди  (последний элемент)
        this.size_ = 0
    
    def is_empty(this):
        return this.size_ == 0
    
    def enqueue(this, data):
        #Добавление элемента в конец очереди
        new_node = Node(data)
        
        if this.is_empty():
            this.front_ = new_node
            this.rear_ = new_node
        else:
            this.rear_.next_ = new_node
            this.rear_ = new_node
        
        this.size_ += 1
    
    def dequeue(this):
        #Удаление элемента из начала очереди
        if this.is_empty():
            raise IndexError("Очередь пуста")
        
        removed_data = this.front_.data_
        this.front_ = this.front_.next_
        
        # Если очередь стала пустой, обнуляем rear
        if this.front_ is None:
            this.rear_ = None
        
        this.size_ -= 1
        return removed_data
    
    def peek(this):
        #"Просмотр первого элемента
        if this.is_empty():
            raise IndexError("Очередь пуста")
        return this.front_.data_
    
    def __len__(this):
        return this.size_
    
    def __str__(this):
        if this.is_empty():
            return "Очередь: []"
        
        elements = []
        current = this.front_
        while current:
            elements.append(str(current.data_))
            current = current.next_
        return "Очередь: [" + " <- ".join(elements) + "]"


class LinkedListStack:
    
    def __init__(this):
        this.top_ = None     # указатель на вершину стека
        this.size_ = 0
    
    def is_empty(this):
        return this.size_ == 0
    
    def push(this, data):
        new_node = Node(data)
        new_node.next_ = this.top_
        this.top_ = new_node
        this.size_ += 1
    
    def pop(this):
        if this.is_empty():
            raise IndexError("Стек пуст")
        
        removed_data = this.top_.data_
        this.top_ = this.top_.next_
        this.size_ -= 1
        return removed_data
    
    def peek(this):
        if this.is_empty():
            raise IndexError("Стек пуст")
        return this.top_.data_
    
    def __len__(this):
        return this.size_
    
    def __str__(this):
        if this.is_empty():
            return "Стек: []"
        
        elements = []
        current = this.top_
        while current:
            elements.append(str(current.data_))
            current = current.next_
        return "Стек: [" + " -> ".join(elements) + "] (вершина слева)"


class DoubleNode:
    """Узел двусвязного списка"""
    def __init__(this, data):
        this.data_ = data
        this.prev_ = None
        this.next_ = None


class DoublyLinkedListDeque:
    """Дек (deque) на основе двусвязного списка
    
    Поддерживает операции добавления и удаления с обоих концов за O(1)
    """
    
    def __init__(this):
        this.head_ = None    # указатель на начало дека
        this.tail_ = None    # указатель на конец дека
        this.size_ = 0
    
    def is_empty(this):
        """Проверка на пустоту"""
        return this.size_ == 0

    def append_left(this, data):
        new_node = DoubleNode(data)
        
        if this.is_empty():
            this.head_ = new_node
            this.tail_ = new_node
        else:
            new_node.next_ = this.head_
            this.head_.prev_ = new_node
            this.head_ = new_node
        
        this.size_ += 1

    def pop_left(this):
        if this.is_empty():
            raise IndexError("Дек пуст")
        
        removed_data = this.head_.data_
        
        if this.size_ == 1:
            this.head_ = None
            this.tail_ = None
        else:
            this.head_ = this.head_.next_
            this.head_.prev_ = None
        
        this.size_ -= 1
        return removed_data
       
    def append_right(this, data):
        new_node = DoubleNode(data)
        
        if this.is_empty():
            this.head_ = new_node
            this.tail_ = new_node
        else:
            new_node.prev_ = this.tail_
            this.tail_.next_ = new_node
            this.tail_ = new_node
        
        this.size_ += 1
    
    def pop_right(this):
        if this.is_empty():
            raise IndexError("Дек пуст")
        
        removed_data = this.tail_.data_
        
        if this.size_ == 1:
            this.head_ = None
            this.tail_ = None
        else:
            this.tail_ = this.tail_.prev_
            this.tail_.next_ = None
        
        this.size_ -= 1
        return removed_data
    
    # ========== Просмотр элементов ==========
    
    def peek_left(this):
        """Просмотр левого элемента без удаления"""
        if this.is_empty():
            raise IndexError("Дек пуст")
        return this.head_.data_
    
    def peek_right(this):
        """Просмотр правого элемента без удаления"""
        if this.is_empty():
            raise IndexError("Дек пуст")
        return this.tail_.data_
    
    # ========== Допы ==========
    
    def clear(this):
        """Очистка дека"""
        this.head_ = None
        this.tail_ = None
        this.size_ = 0
    
    def __len__(this):
        return this.size_
    
    def __str__(this):
        """Строковое представление дека (слева направо)"""
        if this.is_empty():
            return "Дек: []"
        
        elements = []
        current = this.head_
        while current:
            elements.append(str(current.data_))
            current = current.next_
        
        return "Дек: [ " + " <-> ".join(elements) + " ]"
    
    def __repr__(this):
        return f"DoublyLinkedListDeque({this.__str__()})"
    
    # ========== Итераторы ==========
    
    def __iter__(this):
        """Итератор слева направо"""
        current = this.head_
        while current:
            yield current.data_
            current = current.next_
    
    def iter_reverse(this):
        """Итератор справа налево"""
        current = this.tail_
        while current:
            yield current.data_
            current = current.prev_

  
# Примеры от дипсика ====================================================
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




    print("=" * 60)
    print("ДЕК (DEQUE) НА ДВУСВЯЗНОМ СПИСКЕ")
    print("=" * 60)
    
    deque = DoublyLinkedListDeque()
    
    # Пример 1: Добавление с разных концов
    print("\n1. Базовые операции:")
    print("Добавляем 10 справа:", end=" ")
    deque.append_right(10)
    print(deque)
    
    print("Добавляем 20 справа:", end=" ")
    deque.append_right(20)
    print(deque)
    
    print("Добавляем 5 слева:", end=" ")
    deque.append_left(5)
    print(deque)
    
    print("Добавляем 1 слева:", end=" ")
    deque.append_left(1)
    print(deque)
    
    print(f"\nРазмер дека: {len(deque)}")
    print(f"Левый элемент: {deque.peek_left()}")
    print(f"Правый элемент: {deque.peek_right()}")
    
    # Пример 2: Удаление с разных концов
    print("\n2. Удаление элементов:")
    print(f"Удаляем слева: {deque.pop_left()}")
    print(deque)
    
    print(f"Удаляем справа: {deque.pop_right()}")
    print(deque)
    
    print(f"Удаляем справа: {deque.pop_right()}")
    print(deque)
    
    print(f"Удаляем слева: {deque.pop_left()}")
    print(deque)
    
    # Пример 3: Использование как очереди (FIFO)
    print("\n3. Использование как очереди (FIFO):")
    queue_deque = DoublyLinkedListDeque()
    
    for i in range(5):
        queue_deque.append_right(i)
    print(f"После добавления 0-4: {queue_deque}")
    
    while not queue_deque.is_empty():
        print(f"Извлекаем: {queue_deque.pop_left()} -> {queue_deque}")
    
    # Пример 4: Использование как стека (LIFO)
    print("\n4. Использование как стека (LIFO):")
    stack_deque = DoublyLinkedListDeque()
    
    for i in range(5):
        stack_deque.append_right(i)
    print(f"После добавления 0-4: {stack_deque}")
    
    while not stack_deque.is_empty():
        print(f"Извлекаем: {stack_deque.pop_right()} -> {stack_deque}")
    
    # Пример 5: Палиндром (проверка симметрии)
    print("\n5. Проверка палиндрома с помощью дека:")
    
    def is_palindrome(text):
        """Проверка, является ли строка палиндромом"""
        dq = DoublyLinkedListDeque()
        
        # Заполняем дек символами строки
        for char in text.lower():
            if char.isalnum():  # игнорируем не буквенно-цифровые символы
                dq.append_right(char)
        
        # Сравниваем символы с обоих концов
        while len(dq) > 1:
            if dq.pop_left() != dq.pop_right():
                return False
        return True
    
    test_strings = ["А роза упала на лапу Азора", "racecar", "hello", "12321", "Python"]
    for s in test_strings:
        result = "Да" if is_palindrome(s) else "Нет"
        print(f'"{s}" -> {result}')
    
    # Пример 6: Итерация по декy
    print("\n6. Итерация по деку:")
    dq = DoublyLinkedListDeque()
    for i in [10, 20, 30, 40, 50]:
        dq.append_right(i)
    
    print(f"Дек: {dq}")
    print("Прямой итератор:", list(dq))
    print("Обратный итератор:", list(dq.iter_reverse()))
    
    # Пример 7: Очистка дека
    print("\n7. Очистка дека:")
    print(f"До очистки: {dq}, размер = {len(dq)}")
    dq.clear()
    print(f"После очистки: {dq}, размер = {len(dq)}")
    
    # Пример 8: Обработка ошибок
    print("\n8. Обработка ошибок:")
    empty_deque = DoublyLinkedListDeque()
    try:
        empty_deque.pop_left()
    except IndexError as e:
        print(f"Ошибка при pop_left(): {e}")
    
    try:
        empty_deque.pop_right()
    except IndexError as e:
        print(f"Ошибка при pop_right(): {e}")
