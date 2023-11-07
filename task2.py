#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: str) -> bool | int:
    if "a" in inp.lower():
        return inp.lower().index("a")
    return False


if __name__ == "__main__":
    print(main("this is source string"))
    print(main("this is source string with letter A"))
