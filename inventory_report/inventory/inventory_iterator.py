from collections.abc import Iterator


class InventoryIterator(Iterator):
    @classmethod
    def __init__(self, data) -> None:
        self.__data = data
        self.__index = 0

    def __next__(self):
        try:
            while type(self.__data[self.__index]) != str:
                self.__index += 1
            data = self.__data[self.__index]
            self.__index += 1
            return data
        except IndexError:
            raise StopIteration()
