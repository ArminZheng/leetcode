

import practice.course.basic.LinearDS.queue


def plus(s: str, j: int) -> str:
    return s[:j] + plusOne(s[j]) + s[j+1:]


def minus(s: str, j: int) -> str:
    return s[:j] + minusOne(s[j]) + s[j+1:]


def plusOne(s: str) -> str:
    return '0' if s == '9' else chr(ord(s) + 1)


def minusOne(s: str) -> str:
    return '9' if s == '0' else chr(ord(s) - 1)


def bfs(target):
    q = queue()
