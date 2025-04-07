#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Vans", size = 11):
        self.brand = brand
        self.size = size

    @property
    def brand(self):
        """The brand property"""
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        """The size property"""
        return self._size
        
    @size.setter
    def size(self, size):
        """size must be an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")