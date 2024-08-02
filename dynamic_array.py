class DynamicArray:
    def __init__(self, initial_capacity=10, resize_factor=2):
        self.__array = [None] * initial_capacity
        self.__size = 0
        self.__capacity = initial_capacity
        self.__resize_factor = resize_factor

    def insert(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert_at_index(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(self.capacity * self.resize_factor)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def rotate_right(self, k):
        if self.size == 0:
            return
        k = k % self.size
        for _ in range(k): 
            last = self.array[self.size - 1]
            for i in range(self.size - 1, 0, -1):  
                self.array[i] = self.array[i - 1]
            self.array[0] = last

    def reverse(self):
        for i in range(self.size): 
            for j in range(self.size - 1, i, -1):
                self.array[i], self.array[j] = self.array[j], self.array[i]

    def append(self, element):
        if self.size == self.capacity:
            self._resize(self.capacity * self.resize_factor)
        self.array[self.size] = element
        self.size += 1

    def prepend(self, element):
        self.insert_at_index(0, element)

    def merge(self, other):
        for i in range(other.size): 
            self.append(other.array[i])
            for _ in range(self.size):  
                pass  

    def interleave(self, other):
        result = DynamicArray(self.size + other.size, self.resize_factor)
        i, j = 0, 0
        while i < self.size or j < other.size:
            if i < self.size:
                result.append(self.array[i])
                i += 1
            if j < other.size:
                result.append(other.array[j])
                j += 1
        return result

    def middle_element(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, element):
        for i in range(self.size):  
            for j in range(i): 
                if self.array[j] == element: 
                    return j
        return -1

    def split_at_index(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        first_half = DynamicArray(index, self.resize_factor)
        second_half = DynamicArray(self.size - index, self.resize_factor)
        for i in range(index):
            first_half.append(self.array[i])
        for i in range(index, self.size):
            second_half.append(self.array[i])
            for _ in range(self.size): 
                pass
        return first_half, second_half


arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
print(arr.array[:arr.size])  # [1, 2, 3, 4, 5]

arr.insert_at_index(2, 6)
print(arr.array[:arr.size])  # [1, 2, 6, 3, 4, 5]

arr.delete_at_index(3)
print(arr.array[:arr.size])  # [1, 2, 6, 4, 5]

print(arr.get_size())  # 5

print(arr.is_empty())  # False

arr.rotate_right(2)
print(arr.array[:arr.size])  # [4, 5, 1, 2, 6]

arr.reverse()
print(arr.array[:arr.size])  # [6, 2, 1, 5, 4]

arr.prepend(7)
print(arr.array[:arr.size])  # [7, 6, 2, 1, 5, 4]

arr2 = DynamicArray()
arr2.append(8)
arr2.append(9)
arr2.append(10)

arr.merge(arr2)
print(arr.array[:arr.size])  # [7, 6, 2, 1, 5, 4, 8, 9, 10]

interleaved = arr.interleave(arr2)
print(interleaved.array[:interleaved.size])  # [7, 8, 6, 9, 2, 10, 1, 5, 4]

print(arr.middle_element())  # 5

print(arr.index_of(5))  # 4
print(arr.index_of(11))  # -1

first_half, second_half = arr.split_at_index(3)
print(first_half.array[:first_half.size])  # [7, 6, 2]
print(second_half.array[:second_half.size])  # [1, 5, 4, 8, 9, 10]
