"""
功能:从模板中读取气缸和真空的输出变量,自动在后面的表格中输入相关代码
版本:V1.01
作者:xsw
创建时间: 2022年10月11日22:03:03
备注:完成
"""

import xlrd
import xlwt
#import xlutils
import datetime
import time
from xlutils.copy import copy

def my_shwt(list_wr,sh,nrow,ncol,str_old,str_new):
    """
    :param list_wr:	写入的字符串列表
    :param sh:	写入的表格
    :param nrow:	从哪个位置开始写,行数
    :param ncol:	从哪个位置开始写,列数
    :param str_old:	要替换的旧字符串
    :param str_new:	要替换的新字符串

    :return row_col_list:	返回写到了第几行 第几列
    """

    actual_nrow = nrow
    temp_list = []
    temp_str = ""
    for k in range(len(list_wr)):
        actual_nrow += 1
        for l in range(len(list_wr[0])):
            #判断str_old和str_new是字符串还是列表
            if type(str_old) == type(temp_list) and type(str_new) == type(temp_list):
                str_list_wr_new = list_wr[k][l]
                for m in range(len(str_old)):
                    str_list_wr_new = str_list_wr_new.replace(str_old[m],str_new[m])
                sh.write(nrow + k, l, str_list_wr_new)
            elif type(str_old) == type(temp_str) and type(str_new) == type(temp_str):
                str_list_wr_new = list_wr[k][l].replace(str_old, str_new)
                sh.write(nrow+k, l, str_list_wr_new)
    list_row_col = [actual_nrow,0]
    return list_row_col

#打开表格,复制表格
read_book = xlrd.open_workbook('测试表格.xlsx')
wb = copy(read_book)
#读取 第一个表格存放气缸或真空变量
#第一列上下气缸,第二列初始化工作位气缸,第三列真空
sh0 = read_book.sheet_by_index(0)
cyl_list1 = sh0.col_values(0)
cyl_list2 = sh0.col_values(1)
vac_list = sh0.col_values(2)
#变量列表,1上下气缸,2IniWork气缸
#位置变量
cylpos_list1 = [
    ['_Cyl_UpPos','','_Cyl_UpPos : BOOL;'],
    ['_Cyl_DownPos','','_Cyl_DownPos : BOOL;']
]
cylpos_list2 = [
    ['_Cyl_IniPos','','_Cyl_IniPos : BOOL;'],
    ['_Cyl_WorkPos','','_Cyl_WorkPos : BOOL;']
]

#输出变量代码列表
cylout_list1 = [
	['_Cyl_', '', '_Cyl_ : BOOL;', '', '_Cyl_  := FALSE;', '', '_Cyl_FB : CylinderSensor;', '', 'h_Cyl_SafeCondition : BOOL;']
]
cylout_list2 = [
	['_Cyl_', '', '_Cyl_ : BOOL;', '', '_Cyl_  := FALSE;', '', '_Cyl_FB : CylinderSensor;', '', 'h_Cyl_SafeCondition : BOOL;']
]
#报警变量
cylalarm_list1 = [
    ['', ''],
	['', 'a_Cyl_UpPosSensorAlarm: BOOL;'],
	['', 'a_Cyl_DownPosSensorAlarm: BOOL;'],
	['', 'a_Cyl_BothSensorAlarm: BOOL;'],
	['', '_Cyl_SensorAlarm: BOOL;'],
	['', 'am_Cyl_SensorAlarm: BOOL;']
]
cylalarm_list2 = [
    ['', ''],
    ['','a_Cyl_IniPosSensorAlarm : BOOL;'],
    ['','a_Cyl_WorkPosSensorAlarm : BOOL;'],
    ['','a_Cyl_BothSensorAlarm : BOOL;'],
    ['','_Cyl_SensorAlarm : BOOL;'],
    ['','am_Cyl_SensorAlarm : BOOL;']
]
#CT变量
cylct_list1 = [
	['', '_Cyl_CT: REAL;']
]
cylct_list2 = [
	['', '_Cyl_CT: REAL;']
]

#气缸报警功能块程序
cylalarmfb_list1 = [
	['', '', ''],
	['_Cyl_FB(', '', ''],
	['', 'bI_CylinderIniPos:=_Cyl_UpPos ,', ''],
	['', 'bI_CylinderWorkPos:=_Cyl_DownPos ,', ''],
	['', 'bQ_Cylinder:=_Cyl_ ,', ''],
	['', 'tmSensorTimeOut:= t#5s,', ''],
	['', 'bErrIniPos=>a_Cyl_UpPosSensorAlarm ,', ''],
	['', 'bErrWorkPos=>a_Cyl_DownPosSensorAlarm ,', ''],
	['', 'bErrBothPos=>a_Cyl_BothSensorAlarm ,', ''],
	['', 'rExecuteTime=>_Cyl_CT );', ''],
	['', '', ''],
	['', 'IF a_Cyl_UpPosSensorAlarm', ''],
	['', '', 'OR a_Cyl_DownPosSensorAlarm'],
	['', '', 'OR a_Cyl_BothSensorAlarm THEN'],
	['', '', '_Cyl_SensorAlarm := TRUE;'],
	['', 'END_IF', '']
]
cylalarmfb_list2 = [
    ['', '', ''],
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
    ['','END_IF','']
]
#HMI安全条件代码
cylhmi_list1 =[
	['', ''],
	['h_Cyl_SafeCondition:=NOT PowerOn', ''],
	['', 'OR RunButtonDuplex OR ManualAutoSwitchButton;']
]
cylhmi_list2 =[
	['', ''],
	['h_Cyl_SafeCondition:=NOT PowerOn', ''],
	['', 'OR RunButtonDuplex OR ManualAutoSwitchButton;']
]
#人工干涉报警
cylamalarm_list1 = [
	['', '', ''],
	['', 'IF OutputMem[99,99] XOR _Cyl_ THEN', ''],
	['', '', 'am_Cyl_SensorAlarm := TRUE;'],
	['', 'END_IF', '']
]
cylamalarm_list2 = [
	['', '', ''],
	['', 'IF OutputMem[99,99] XOR _Cyl_ THEN', ''],
	['', '', 'am_Cyl_SensorAlarm := TRUE;'],
	['', 'END_IF', '']
]

#真空
#IO输入
vacok_list = [
	['_Vac_OK', '', '_Vac_OK : BOOL;']
]
#IO输出,以及其他变量
vacout_list =[
    ['', '', '', '', '', '', ''],
	['_Vac_', '', '_Vac_ : BOOL;', '', '', '', '_Vac_FB :VacSensor_1;'],
	['', '', '', '', '', '', ''],
	['', '', '_Vac_AlarmClose : BOOL;', '', '', '', ''],
	['', '', '_Vac_OKFlag : BOOL;', '', '', '', ''],
	['', '', '', '', '', '', ''],
	['', '', '_Vac_OKTemp : BOOL;', '', '', '', ''],
	['', '', '_Vac_OKDelayTime : REAL := 0.1;', '', '', '', ''],
	['', '', '_Vac_ReleaseVacDelayTime : REAL := 0.1;', '', '', '', ''],
	['', '', '_Vac_OKAlarmTime : REAL := 3;', '', '', '', ''],
	['', '', '_Vac_OKErrTime : REAL := 0.3;', '', '', '', '']
]
#报警变量
vacalarm_list = [
    ['', ''],
	['', 'a_Vac_SensorAlarm : BOOL;'],
	['', 'a_Vac_SensorErrAlarm : BOOL;'],
	['', 'am_Vac_SensorAlarm : BOOL;'],
	['', '_Vac_SensorAlarm : BOOL;']
]
#CT变量
vacct_list = [
	['', '_Vac_CT: REAL;']
]
#报警功能块
vacalarmfb_list = [
	['', '', '', ''],
	['_Vac_FB(', '', '', ''],
	['', 'bI_VacOK:= _Vac_OK OR _Vac_AlarmClose,', '', ''],
	['', 'bQ_VacOpen:=  _Vac_,', '', ''],
	['', 'bEmptyRun:= EmptyRunButton,', '', ''],
	['', 'bHMIVacBlow:= ,', '', ''],
	['', 'rVacAlarmTimeOut:= _Vac_OKAlarmTime,', '', ''],
	['', 'rReleaseAlarmTimeOut:= _Vac_OKErrTime,', '', ''],
	['', 'rVacOKDellayTime:= _Vac_OKDelayTime,', '', ''],
	['', 'rVacBlowDelayTime:= _Vac_ReleaseVacDelayTime,', '', ''],
	['', 'bQ_Blow=>_2Vac_Blow ,', '', ''],
	['', 'bVacNotOKAlarm=> a_Vac_SensorAlarm,', '', ''],
	['', 'bVacReleaseAlarm=> a_Vac_SensorErrAlarm,', '', ''],
	['', 'bErrVacInterruptAlarm=> ,', '', ''],
	['', 'bVacOKFlag=> _Vac_OKFlag,', '', ''],
	['', 'rExecuteTime=> _Vac_CT);', '', ''],
	['', '', '', ''],
	['', 'IF  _Vac_ AND _Vac_OK', '', ''],
	['', '', 'AND AutorunFlag THEN', ''],
	['', '', '_Vac_OKTemp := TRUE;', ''],
	['', 'ELSIF  NOT _Vac_ AND AutorunFlag THEN', '', ''],
	['', '', '_Vac_OKTemp := FALSE;', ''],
	['', 'END_IF', '', ''],
	['', '', '', ''],
	['', 'IF a_Vac_SensorAlarm', '', ''],
	['', '', 'OR a_Vac_SensorErrAlarm', ''],
	['', '', 'OR (_Vac_OKTemp AND _Vac_FB.bErrVacInterruptAlarm', ''],
	['', '', '', 'AND NOT aTP4LeftCellPosChangeAlarm) THEN'],
	['', '', '_Vac_SensorAlarm := TRUE;', ''],
	['', 'END_IF', '', ''],
	['', '', '', ''],
	['', '', '', ''],
	['', '(*真空不OK输出*)', '', ''],
	['', 'IF _Vac_OKTemp AND _Vac_FB.bErrVacInterruptAlarm THEN', '', ''],
	['', '', 'VacNotOKAlarm := TRUE;', ''],
	['', 'END_IF', '', ''],
	['', '', '', ''],
	['', '(*', '有电池检测输出', '*)'],
	['', 'IF _Vac_OK', '', ''],
	['', '', 'OR (TP4LeftCellCheckSensor AND NOT EmptyRunButton) THEN', ''],
	['', '', 'MachineHaveCellFlag := TRUE;', ''],
	['', 'END_IF', '', ''],
	['', '', '', ''],
	['', '(*', '有真空打开', '*)'],
	['', 'IF  _Vac_ THEN', '', ''],
	['', '', 'MachineVacOpenFlag := TRUE;', ''],
	['', 'END_IF', '', ''],
	['', '', '', ''],
	['', '(*', '有真空状态记忆', '*)'],
	['', 'IF _Vac_OKTemp THEN', '', ''],
	['', '', 'MachineVacOKTempFlag := TRUE;', ''],
	['', 'END_IF', '', ''],
	['', '', '', ''],
	['', '(*', '电池实时检测', '*)'],
	['', 'IF ((_Vac_OKTemp AND _Vac_FB.bErrVacInterruptAlarm)', '', ''],
	['', '', '', 'OR aTP4LeftCellLostAlarm)'],
	['', '', 'AND TP4CellPosCheck THEN', ''],
	['', '', 'TP4LeftCellPosChange := TRUE;', ''],
	['', 'END_IF', '', '']
]
#人工干涉
vacamalarm_list = [
	['', 'IF OutputMem[99,99] XOR _Vac_ THEN', ''],
	['', '', 'am_Vac_SensorAlarm := TRUE;'],
	['', 'END_IF', '']
]

# 1,IO输入 2,IO输出 3,报警变量 4,CT变量 5,报警功能块 6,HMI安全条件 7,人工干涉报警
sh1 = wb.get_sheet(1)
sh2 = wb.get_sheet(2)
sh3 = wb.get_sheet(3)
sh4 = wb.get_sheet(4)
sh5 = wb.get_sheet(5)
sh6 = wb.get_sheet(6)
sh7 = wb.get_sheet(7)
nrc_count_sh1 = [0,0]
nrc_count_sh2 = [0,0]
nrc_count_sh3 = [0,0]
nrc_count_sh4 = [0,0]
nrc_count_sh5 = [0,0]
nrc_count_sh6 = [0,0]
nrc_count_sh7 = [0,0]
# 1,IO输入 2,IO输出 3,报警变量 4,CT变量 5,报警功能块 6,HMI安全条件 7,人工干涉报警
for i in range(1,len(cyl_list1)):
    if cyl_list1[i] == '':
        continue
    nrc_count_sh1 = my_shwt(cylpos_list1, sh1, nrc_count_sh1[0], nrc_count_sh1[1], '_Cyl_', cyl_list1[i])
    nrc_count_sh2 = my_shwt(cylout_list1, sh2, nrc_count_sh2[0], nrc_count_sh2[1], '_Cyl_', cyl_list1[i])
    nrc_count_sh3 = my_shwt(cylalarm_list1, sh3, nrc_count_sh3[0], nrc_count_sh3[1], '_Cyl_', cyl_list1[i])
    nrc_count_sh4 = my_shwt(cylct_list1, sh4, nrc_count_sh4[0], nrc_count_sh4[1], '_Cyl_', cyl_list1[i])
    nrc_count_sh5 = my_shwt(cylalarmfb_list1, sh5, nrc_count_sh5[0], nrc_count_sh5[1], '_Cyl_', cyl_list1[i])
    nrc_count_sh6 = my_shwt(cylhmi_list1, sh6, nrc_count_sh6[0], nrc_count_sh6[1], '_Cyl_', cyl_list1[i])
    nrc_count_sh7 = my_shwt(cylamalarm_list1, sh7, nrc_count_sh7[0], nrc_count_sh7[1], '_Cyl_', cyl_list1[i])

for i in range(1,len(cyl_list2)):
    if cyl_list2[i] == '':
        continue
    nrc_count_sh1 = my_shwt(cylpos_list2, sh1, nrc_count_sh1[0], nrc_count_sh1[1], '_Cyl_', cyl_list2[i])
    nrc_count_sh2 = my_shwt(cylout_list2, sh2, nrc_count_sh2[0], nrc_count_sh2[1], '_Cyl_', cyl_list2[i])
    nrc_count_sh3 = my_shwt(cylalarm_list2, sh3, nrc_count_sh3[0], nrc_count_sh3[1], '_Cyl_', cyl_list2[i])
    nrc_count_sh4 = my_shwt(cylct_list2, sh4, nrc_count_sh4[0], nrc_count_sh4[1], '_Cyl_', cyl_list2[i])
    nrc_count_sh5 = my_shwt(cylalarmfb_list2, sh5, nrc_count_sh5[0], nrc_count_sh5[1], '_Cyl_', cyl_list2[i])
    nrc_count_sh6 = my_shwt(cylhmi_list2, sh6, nrc_count_sh6[0], nrc_count_sh6[1], '_Cyl_', cyl_list2[i])
    nrc_count_sh7 = my_shwt(cylamalarm_list2, sh7, nrc_count_sh7[0], nrc_count_sh7[1], '_Cyl_', cyl_list2[i])

# 1,IO输入 2,IO输出 3,报警变量 4,CT变量 5,报警功能块 6,HMI安全条件 7,人工干涉报警
for i in range(1,len(vac_list)):
    if vac_list[i] == '':
        continue
    nrc_count_sh1 = my_shwt(vacok_list, sh1, nrc_count_sh1[0], nrc_count_sh1[1],
                            ['_Vac_','_2Vac_'], [vac_list[i],vac_list[i][:-3]])
    nrc_count_sh2 = my_shwt(vacout_list, sh2, nrc_count_sh2[0], nrc_count_sh2[1],
                            ['_Vac_','_2Vac_'], [vac_list[i],vac_list[i][:-3]])
    nrc_count_sh3 = my_shwt(vacalarm_list , sh3, nrc_count_sh3[0], nrc_count_sh3[1],
                            ['_Vac_', '_2Vac_'], [vac_list[i], vac_list[i][:-3]])
    nrc_count_sh4 = my_shwt(vacct_list, sh4, nrc_count_sh4[0], nrc_count_sh4[1],
                            ['_Vac_', '_2Vac_'], [vac_list[i], vac_list[i][:-3]])
    nrc_count_sh5 = my_shwt(vacalarmfb_list, sh5, nrc_count_sh5[0], nrc_count_sh5[1],
                            ['_Vac_','_2Vac_'], [vac_list[i],vac_list[i][:-3]])
    nrc_count_sh7 = my_shwt(vacamalarm_list , sh7, nrc_count_sh7[0], nrc_count_sh7[1],
                            ['_Vac_', '_2Vac_'], [vac_list[i], vac_list[i][:-3]])

#保存表格后加时间
curr_time = datetime.datetime.now()
str_curr_time = (str(curr_time)).replace(':','-')[:19]
xlsx_name = f'测试表格{str_curr_time}.xlsx'
wb.save(xlsx_name)
