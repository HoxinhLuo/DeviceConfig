from ttkbootstrap import Frame, Button, Treeview
from ttkbootstrap import Window
from addDevice import AddDeviceWidget
from config import connect_db


# from ttkbootstrap.dialogs.dialogs import Messagebox


class MainApp(Window):
    def __init__(self, **kw):
        # build ui
        super(MainApp, self).__init__(**kw)

        self.adddevicewidget = None
        self.topFrame = Frame(self)
        self.operateFrame = Frame(self.topFrame)
        self.addDevBtn = Button(self.operateFrame)
        self.addDevBtn.configure(text='添加')
        self.addDevBtn.pack(padx=5, side="left")
        self.addDevBtn.configure(command=self.toAddDevice)

        self.modDevBtn = Button(self.operateFrame)
        self.modDevBtn.configure(text='修改')
        self.modDevBtn.pack(padx=8, side="left")
        self.modDevBtn.configure(command=self.toModifyDevice)

        self.delDevBtn = Button(self.operateFrame)
        self.delDevBtn.configure(text='删除')
        self.delDevBtn.pack(padx=3, side="left")
        self.delDevBtn.configure(command=self.toDeleteDevice)

        self.bakDevBtn = Button(self.operateFrame)
        self.bakDevBtn.configure(text='备份')
        self.bakDevBtn.pack(padx=5, side="left")
        self.bakDevBtn.configure(command=self.toBackupDevice)

        self.operateFrame.pack(pady=12, side="top")
        self.devListTreeview = Treeview(self.topFrame)
        self.devListTreeview.configure(selectmode="extended", show="headings")
        self.devListTreeview_cols = [
            'devNameCol',
            'devTypeCol',
            'devModelCol',
            'devIPCol',
            'devSiteCol']
        self.devListTreeview_dcols = [
            'devNameCol',
            'devTypeCol',
            'devModelCol',
            'devIPCol',
            'devSiteCol']
        self.devListTreeview.configure(
            columns=self.devListTreeview_cols,
            displaycolumns=self.devListTreeview_dcols)
        self.devListTreeview.column(
            "devNameCol",
            anchor="center",
            stretch=True,
            width=150,
            minwidth=20)
        self.devListTreeview.column(
            "devTypeCol",
            anchor="center",
            stretch=True,
            width=200,
            minwidth=20)
        self.devListTreeview.column(
            "devIPCol",
            anchor="center",
            stretch=True,
            width=200,
            minwidth=20)
        self.devListTreeview.column(
            "devModelCol",
            anchor="center",
            stretch=True,
            width=150,
            minwidth=20)
        self.devListTreeview.column(
            "devSiteCol",
            anchor="center",
            stretch=True,
            width=150,
            minwidth=20)
        self.devListTreeview.heading("devNameCol", anchor="center", text='设备名称')
        self.devListTreeview.heading("devTypeCol", anchor="center", text='设备类型')
        self.devListTreeview.heading("devModelCol", anchor="center", text='设备型号')
        self.devListTreeview.heading("devIPCol", anchor="center", text='设备IP地址')
        self.devListTreeview.heading("devSiteCol", anchor="center", text='所属装置')
        self.devListTreeview.pack(expand=True, fill="both", pady=8, side="top")
        self.topFrame.pack(expand=True, fill="both", side="top", padx=5)

        # Main widget
        self.mainwindow = self.topFrame

        # Init device list
        self.init_device()

    def run(self):
        self.mainwindow.mainloop()

    def toAddDevice(self):
        self.adddevicewidget = AddDeviceWidget(self)
        self.mainwindow.wait_window(self.adddevicewidget)

    def toModifyDevice(self):
        pass

    def toDeleteDevice(self):
        item_list = self.devListTreeview.selection()
        # okcancel = Messagebox.show_question("是否删除全部?", "删除全部")
        # print(okcancel)
        self.devListTreeview.delete(*item_list)

    def toBackupDevice(self):
        pass

    def init_device(self):
        conn = connect_db()
        cur = conn.cursor()
        fetch_cmd = '''SELECT * from DEVICEINFO'''
        cur.execute(fetch_cmd)
        fetch_data = cur.fetchall()
        for line in fetch_data:
            self.devListTreeview.insert('', 'end', values=line)
