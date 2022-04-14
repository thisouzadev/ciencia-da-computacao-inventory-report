from collections.abc import Iterator


class InventoryIterator(Iterator):
    @classmethod
    def __init__(self, data) -> None:
        self.__data = data
        self.__index = 0

    def __next__(self):
        if not self.__data[self.__index]:
            raise StopIteration()
        else:
            data = self.__data[self.__index]
            self.__index += 1
            return data
