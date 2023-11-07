#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(s1: str) -> str:
    s2: str = ""
    s2_list: list = [s1[letter] for letter in range(len(s1)) if letter % 2 != 0]
    return s2.join(s2_list)


if __name__ == "__main__":
    print(main("Исходная строка"))
