#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: str):
    for letter in inp:
        print(letter)


if __name__ == "__main__":
    inp = input("Введите название футбольного клуба: ")
    main(inp)
