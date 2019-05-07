# --*-- coding=utf-8 --*--
# @File    : do_excel.py
# @Time    : 2019-05-04 19:07
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


from openpyxl import load_workbook
from API_2.common.project_path import case_path


class DoExcel:

    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def read_data(self):
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]

        test_data = []
        for i in range(2, sheet.max_row+1):
            row_data = {}
            row_data["CaseId"] = sheet.cell(i, 1).value
            row_data["Module"] = sheet.cell(i, 2).value
            row_data["Title"] = sheet.cell(i, 3).value
            row_data["Url"] = sheet.cell(i, 4).value
            row_data["Method"] = sheet.cell(i, 5).value
            row_data["Params"] = sheet.cell(i, 6).value
            row_data["ExpectedResult"] = sheet.cell(i, 7).value
            test_data.append(row_data)
        wb.close()
        return test_data

    def write_back(self, row, col, val):
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]
        sheet.cell(row, col).value = val
        wb.save(self.file_name)
        wb.close()


if __name__ == '__main__':

    result = DoExcel(case_path, "register").read_data()
    print(result)





