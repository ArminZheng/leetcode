"""文件相关工具
"""


def printFileInfo(file_path: str):
    """输出文件内容

    Args:
        file_path (str): 文件路径
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            content = f.read()
            print("文件内容如下:", content, sep="\n")
    except Exception as e:
        print(f"程序出现异常: {e}")


def appendToFile(file_path: str, data: str):
    """将data附加到指定文件

    Args:
        file_path (str): 文件路径
        data (str): 指定内容
    """
    with open(file_path, "a", encoding="UTF-8") as f:
        f.write(data)
        f.write("\n")


if __name__ == "__main__":
    printFileInfo("README.md")
    print("hello")
    # print(append_to_file("README.md", "hahaha"))
