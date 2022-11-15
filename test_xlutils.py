import xlrd
import xlwt
#import xlutils
import datetime
import time
from xlutils.copy import copy

#打开表格,复制表格
read_book = xlrd.open_workbook('测试表格.xlsx')
wb = copy(read_book)
#读取
sh0 = read_book.sheet_by_index(0)
cyl_list = sh0.col_values(0)
cyl_list1 = sh0.col_values(0)
cyl_list2 = sh0.col_values(1)

print("上下气缸:",cyl_list)
print("初始位工位位气缸:",cyl_list2)
#变量列表,1上下气缸,2IniWork气缸
#位置变量
cylpos_list1 = [
    ['_Cyl_UpPos'],
    ['_Cyl_DownPos']
]
cylpos_list2 = [
    ['_Cyl_IniPos'],
    ['_Cyl_WorkPos']
]
#CT变量
cylct_list1 = [['_Cyl_CT']]
cylct_list2 = [['_Cyl_CT']]
#报警变量
cylalarm_list1 = [
    ['a_Cyl_UpPosSensorAlarm'],
    ['a_Cyl_DownPosSensorAlarm'],
    ['a_Cyl_BothSensorAlarm'],
    ['_Cyl_SensorAlarm'],
    ['am_Cyl_SensorAlarm']
]
cylalarm_list2 = [
    ['a_Cyl_IniPosSensorAlarm'],
    ['a_Cyl_WorkPosSensorAlarm'],
    ['a_Cyl_BothSensorAlarm'],
    ['_Cyl_SensorAlarm'],
    ['am_Cyl_SensorAlarm']
]
#气缸报警功能块程序
cylalarmfb_list1 = [
    ['_Cyl_FB(','',''],
    ['','bI_CylinderIniPos:=_Cyl_UpPos ,',''],
    ['','bI_CylinderWorkPos:=_Cyl_DownPos ,',''],
    ['','bQ_Cylinder:=_Cyl_ ,',''],
    ['','tmSensorTimeOut:= t#5s,',''],
    ['','bErrIniPos=>a_Cyl_UpPosSensorAlarm ,',''],
    ['','bErrWorkPos=>a_Cyl_DownPosSensorAlarm ,',''],
    ['','bErrBothPos=>a_Cyl_BothSensorAlarm ,',''],
    ['','rExecuteTime=>_Cyl_CT );',''],
    ['','',''],
    ['','IF a_Cyl_UpPosSensorAlarm',''],
    ['','','OR a_Cyl_DownPosSensorAlarm'],
    ['','','OR a_Cyl_BothSensorAlarm THEN'],
    ['','','_Cyl_SensorAlarm := TRUE;'],
    ['','END_IF',''],
    ['', '', '']
]
cylalarmfb_list2 = [
    ['_Cyl_FB(','',''],
    ['','bI_CylinderIniPos:=_Cyl_IniPos ,',''],
    ['','bI_CylinderWorkPos:=_Cyl_WorkPos ,',''],
    ['','bQ_Cylinder:=_Cyl_ ,',''],
    ['','tmSensorTimeOut:= t#5s,',''],
    ['','bErrIniPos=>a_Cyl_IniPosSensorAlarm ,',''],
    ['','bErrWorkPos=>a_Cyl_WorkPosSensorAlarm ,',''],
    ['','bErrBothPos=>a_Cyl_BothSensorAlarm ,',''],
    ['','rExecuteTime=>_Cyl_CT );',''],
    ['','',''],
    ['','IF a_Cyl_IniPosSensorAlarm',''],
    ['','','OR a_Cyl_WorkPosSensorAlarm'],
    ['','','OR a_Cyl_BothSensorAlarm THEN'],
    ['','','_Cyl_SensorAlarm := TRUE;'],
    ['','END_IF',''],
    ['', '', '']
]
sh1_nrows = 0
sh2_nrows = 0
sh3_nrows = 0
sh4_nrows = 0
sh1 = wb.get_sheet(1)
sh2 = wb.get_sheet(2)
sh3 = wb.get_sheet(3)
sh4 = wb.get_sheet(4)
for i in range(1,len(cyl_list1)):
    for k in range(len(cylpos_list1)):
        sh1_nrows += 1
        for l in range(len(cylpos_list1[0])):
            sh1.write(k+len(cylpos_list1)*(i-1), l, cylpos_list1[k][l].replace('_Cyl_',cyl_list1[i]))
            sh1.write(k+len(cylpos_list1)*(i-1), l+2, cylpos_list1[k][l].replace('_Cyl_',cyl_list1[i]) + ' : BOOL;')
for i in range(1,len(cyl_list1)):
    for k in range(len(cylalarm_list1)):
        sh2_nrows += 1
        for l in range(len(cylalarm_list1[0])):
            sh2.write(k+len(cylalarm_list1)*(i-1), l, cylalarm_list1[k][l].replace('_Cyl_',cyl_list1[i]))
            sh2.write(k+len(cylalarm_list1)*(i-1), l+2, cylalarm_list1[k][l].replace('_Cyl_',cyl_list1[i]) + ' : BOOL;')
for i in range(1,len(cyl_list1)):
    for k in range(len(cylct_list1)):
        sh3_nrows += 1
        for l in range(len(cylct_list1[0])):
            sh3.write(k+len(cylct_list1)*(i-1), l, cylct_list1[k][l].replace('_Cyl_',cyl_list1[i]))
            sh3.write(k+len(cylct_list1)*(i-1), l+2, cylct_list1[k][l].replace('_Cyl_',cyl_list1[i]) + ' : REAL;')
for i in range(1,len(cyl_list1)):
    for k in range(len(cylalarmfb_list1)):
        sh4_nrows += 1
        for l in range(len(cylalarmfb_list1[0])):
            sh4.write(k+len(cylalarmfb_list1)*(i-1), l, cylalarmfb_list1[k][l].replace('_Cyl_',cyl_list1[i]))

print("sheet1已写行数:",sh1_nrows)
print("sheet2已写行数:",sh2_nrows)
print("sheet3已写行数:",sh3_nrows)
print("sheet4已写行数:",sh4_nrows)
sh1_nrows_temp = sh1_nrows
sh2_nrows_temp = sh2_nrows
sh3_nrows_temp = sh3_nrows
sh4_nrows_temp = sh4_nrows
#列表2
for i in range(1,len(cyl_list2)):
    for k in range(len(cylpos_list2)):
        for l in range(len(cylpos_list2[0])):
            sh1.write(sh1_nrows_temp+k+len(cylpos_list2)*(i-1), l, cylpos_list2[k][l].replace('_Cyl_',cyl_list2[i]))
            sh1.write(sh1_nrows_temp+k+len(cylpos_list2)*(i-1), l+2, cylpos_list2[k][l].replace('_Cyl_',cyl_list2[i]) + ' : BOOL;')
            sh1_nrows +=1

for i in range(1,len(cyl_list2)):
    for k in range(len(cylalarm_list2)):
        for l in range(len(cylalarm_list2[0])):
            sh2.write(sh2_nrows_temp+k+len(cylalarm_list2)*(i-1), l, cylalarm_list2[k][l].replace('_Cyl_',cyl_list2[i]))
            sh2.write(sh2_nrows_temp+k+len(cylalarm_list2)*(i-1), l+2, cylalarm_list2[k][l].replace('_Cyl_',cyl_list2[i]) + ' : BOOL;')
            sh2_nrows +=1

for i in range(1,len(cyl_list2)):
    for k in range(len(cylct_list2)):
        for l in range(len(cylct_list2[0])):
            sh3.write(sh3_nrows_temp+k+len(cylct_list2)*(i-1), l, cylct_list2[k][l].replace('_Cyl_',cyl_list2[i]))
            sh3.write(sh3_nrows_temp+k+len(cylct_list2)*(i-1), l+2, cylct_list2[k][l].replace('_Cyl_',cyl_list2[i]) + ' : REAL;')
            sh3_nrows +=1

for i in range(1,len(cyl_list2)):
    for k in range(len(cylalarmfb_list2)):
        sh4_nrows += 1
        for l in range(len(cylalarmfb_list2[0])):
            sh4.write(sh4_nrows_temp+k+len(cylalarmfb_list2)*(i-1), l, cylalarmfb_list2[k][l].replace('_Cyl_',cyl_list2[i]))


print("sheet1已写行数:",sh1_nrows)
print("sheet2已写行数:",sh2_nrows)
print("sheet3已写行数:",sh3_nrows)
print("sheet4已写行数:",sh4_nrows)
sh1_nrows_temp = sh1_nrows
sh2_nrows_temp = sh2_nrows
sh3_nrows_temp = sh3_nrows
sh4_nrows_temp = sh4_nrows

#保存表格后加时间
curr_time = datetime.datetime.now()
str_curr_time = (str(curr_time)).replace(':','-')[:19]
xlsx_name = f'测试表格{str_curr_time}.xlsx'
wb.save(xlsx_name)
