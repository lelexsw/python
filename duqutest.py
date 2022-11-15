#从123.xlsx表格中读取模板,转换为列表输出到 代码.txt里面
import xlrd

#打开表格,复制表格
read_book = xlrd.open_workbook('123.xlsx')
#读取 10行 10列
sh0 = read_book.sheet_by_index(0)

range_10row_10col = []
for i in range(sh0.nrows):
    range_10row_10col.append(sh0.row_values(i))

str_range_10row_10col = str(range_10row_10col)
print(str_range_10row_10col)
new_str_range_10row_10col = str_range_10row_10col.replace("[[","[\n\t[")
new_str_range_10row_10col = new_str_range_10row_10col.replace("]]","]\n]")
new_str_range_10row_10col = new_str_range_10row_10col.replace("], ","],\n\t")
print(new_str_range_10row_10col)

# 1. 打开文件
f = open('代码.txt', 'w')
# 2.文件写入
f.write(new_str_range_10row_10col)
# 3. 内容刷新
f.flush()
f.close()
