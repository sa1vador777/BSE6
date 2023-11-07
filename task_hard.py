#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: str) -> int:
    spaces_count: int = 0
    for element in range(len(inp)):
        if inp[element] == ' ' and inp[element+1] == ' ':
            spaces_count += 1
    
    return spaces_count + 1


if __name__ == "__main__":
    print(main("Alo alo    alo"))
