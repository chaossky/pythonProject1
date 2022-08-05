import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.XHwpWindows.Item(0).Visible=True
act=hwp.CreateAction("InsertText")
pset = act.CreateSet()
pset.SetItem("Text","Hello\r\nWogdsgsdsdgrld!!!")
act.Execute(pset)