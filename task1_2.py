#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: str) -> str:
    return inp[::-1]


if __name__ == "__main__":
    inp = input("Введите любую строку: ")
    print(main(inp))
