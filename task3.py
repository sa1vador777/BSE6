#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: str, k: int = None) -> list[str]:
    string_without_third_letter = inp[:2] + inp[3:]
    string_without_k_letter = inp[:k-1] + inp[k:]
    return [string_without_third_letter, string_without_k_letter]


if __name__ == "__main__":
    print(main("123456", 5))
