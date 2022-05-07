#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: transfer_require.py
@time: 2022/2/7 2:40
"""


def main():
    arr=""
    with open("requirements.txt", "r" ) as f:
        for line in f.readlines():
            print(line.split("==")[0])
            arr =arr+(line.split("==")[0])+ " "
    print(arr)
def update_depend():
    pass
if __name__ == "__main__":
    main()
