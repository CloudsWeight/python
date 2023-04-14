'''
Testing Python
'''
#!/usr/bin/env python
import wx



class MainWindow(wx.Frame):

    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu= wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", " Info about this you")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", "Exit")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") # addig filemenu to menubar
        self.SetMenuBar(menuBar)
        self.Show(True)





def main():
    app = wx.App(False)
    frame = MainWindow(None, "editor")
    app.MainLoop()


if __name__ == "__main__":
    main()


