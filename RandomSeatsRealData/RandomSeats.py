"""
Gao Yang
2021.11.14
随机安排座位。
使用方法见readme.txt。
"""
import xlrd
from xlrd import sheet
import xlwt
import random
import os
import copy
import datetime


def read_names(student_file):
    work_book = xlrd.open_workbook(student_file)
    sheet_1 = work_book.sheets()[0]
    row_num = int(sheet_1.nrows)
    name_list_original = []
    for i in range(row_num):
        name = sheet_1.cell_value(i, 0)
        name_list_original.append(name)
    print(name_list_original)
    name_list_new = copy.deepcopy(name_list_original)
    random.shuffle(name_list_new)
    print("重排后：\n", name_list_new)
    return name_list_new


def read_len(len_file):
    work_book = xlrd.open_workbook(len_file)
    sheet_1 = work_book.sheets()[0]
    row_num = int(sheet_1.nrows)
    col_len = {}
    for i in range(1, row_num):
        col_index = sheet_1.cell_value(i, 0)
        col_n = sheet_1.cell_value(i, 1)
        col_len[col_index] = col_n
    print("每列人数：\n", col_len)
    return col_len


def sum_seats(col_len):
    s = 0
    for _, value in col_len.items():
        s += value
    return s


def write_file(name_list, col_len, file):
    f = xlwt.Workbook()
    sheet_2 = f.add_sheet("Seats", cell_overwrite_ok=True)
    if sum_seats(col_len) < len(name_list):
        print('座位不够，请调整"col_len.xls"')
        return -1
    names = iter(name_list)
    while True:
        try:
            for key, value in col_len.items():
                sheet_2.write(0, int(key), int(key))
                for i in range(int(value)):
                    sheet_2.write(i + 1, int(key), next(names))

        except StopIteration:
            break
    f.save(file)
    print("成功生成座位表文件。程序结束。")


file_path = os.path.abspath(os.curdir)
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

if __name__ == "__main__":
    name_list_new = read_names(
        file_path + "/student.xls"
    )  # 这里是Mac系统的用法。如果在Win下使用，要调整路径的格式。下同。
    col_len = read_len(file_path + "/col_len.xls")
    output_file_name = file_path + "/seats-{}.xls".format(time_stamp)
    write_file(name_list_new, col_len, output_file_name)
