from abc import ABC, abstractmethod


class AbstractArray(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def create(self, n):
        pass

    def __del__(self):
        print('Deleted!')


class Array(AbstractArray):
    def __init__(self, array):
        super().__init__()
        self.array = array

    def print(self):
        print("Array: ", self.array)

    def create(self, n):
        data = input("Data: ")
        if Type(data) == str:
            self.array.append(data)
            createString(self.array, n)
        elif Type(data) == int:
            self.array.append(int(data))
            createInt(self.array, n)
        elif Type(data) == float:
            self.array.append(float(data))
            createFloat(self.array, n)


def createInt(array, n):
    for i in range(n - 1):
        data = int(input("Data: "))
        array.append(int(data)/(i+2))


def createFloat(array, n):
    for i in range(n - 1):
        data = float(input("Data: "))
        array.append(data/(i + 2))


def createString(array, n):
    for i in range(n - 1):
        data = input("Data: ")
        array.append(data)


def Type(data):
    try:
        data = int(data)
        return type(data)
    except ValueError:
        try:
            data = float(data)
            return type(data)
        except ValueError:
            return type(data)
