"""字符串相关工具
"""


def reverse(s: str):
    """字符串反转

    Args:
        s (str): 将被反转的字符串

    Returns:
        str: 反转后的字符串
    """
    return s[::-1]  # 切片, 开始:结束:从后往前


def substr(s: str, x, y):
    """给定下标完成字符串的切片

    Args:
        s (str): 即将被切片的字符串
        x (int): 切片开始的下标
        y (int): 切片结束的下标
    """
    return s[x:y]


if __name__ == "__main__":
    print(reverse("hello world"))
    print(substr("hello world", 1, 3))
