# -*-coding:UTF-8-*-

import wx

def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()


if __name__ == '__main__':
    app = wx.App()
    win = wx.Frame(None, title='test', size=(410, 335))

    bkg = wx.Panel(win)

    loadButton = wx.Button(bkg, label='��')
    loadButton.Bind(wx.EVT_BUTTON, load)

    saveButton = wx.Button(bkg, label='����')
    saveButton.Bind(wx.EVT_BUTTON, save)

    filename = wx.TextCtrl(bkg)
    contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

    hbox = wx.BoxSizer()
    hbox.Add(filename, proportion=1, flag=wx.EXPAND)
    hbox.Add(loadButton, proportion=1, flag=wx.LEFT, border=5)
    hbox.Add(saveButton, proportion=1, flag=wx.LEFT, border=5)

    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
    vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)

    bkg.SetSizer(vbox)
    win.Show()

    app.MainLoop()
