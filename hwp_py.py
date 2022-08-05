
#_*_coding:utf-8_*_

import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

hwp.Open("F:\\python_ex\\1111.hwp","HWP","forceopen:true")

hwp.HAction.GetDefault("AllReplace",hwp.HParameterSet.HFindReplace.HSet)

option=hwp.HParameterSet.HFindReplace
option.FindString="손흥민"
option.ReplaceString="손오공"

option.IgnoreMessage=1

hwp.HAction.Execute("AllReplace", hwp.HParameterSet.HFindReplace.HSet)
hwp.Clear(3)
hwp.Quit()

 