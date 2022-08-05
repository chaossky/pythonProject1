#_*_coding:cp949_*_
#
import win32com.client as win32
import pandas as pd
#hwp=win32.Dispatch("HWPFrame.HWPObject") 

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
#hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample") 


excel=pd.read_excel('F:\\python_ex\\award_list.xlsx')

#print(excel)

hwp.Open('F:\\python_ex\\award1.hwp')
