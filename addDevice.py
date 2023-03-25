from ttkbootstrap import Toplevel, Frame, Label, Entry, StringVar, Button, Combobox, Labelframe, Notebook, Radiobutton
from ttkbootstrap.dialogs.dialogs import Messagebox
from config import insert_db, connect_db, close_db
from utils import check_ip


class AddDeviceWidget(Toplevel):
    def __init__(self, parent=None):
        super(AddDeviceWidget, self).__init__(parent)
        self.parent = parent
        self.dev_info = None

        self.addDeviceNotebook = Notebook(self)
        self.autoImportFrame = Frame(self.addDeviceNotebook)
        self.autoImportFrame.configure(height=200, width=200)
        self.fileTypeLabelFrame = Labelframe(self.autoImportFrame)
        self.fileTypeLabelFrame.configure(text='文件类型')
        self.fileTypexlsxRd = Radiobutton(self.fileTypeLabelFrame)
        self.fileTypeRd = StringVar(value='xlsx')
        self.fileTypexlsxRd.configure(
            text='XLSX', value="xlsx", variable=self.fileTypeRd)
        self.fileTypexlsxRd.pack(padx=5, side="left")
        self.fileTypeCSVRd = Radiobutton(self.fileTypeLabelFrame)
        self.fileTypeCSVRd.configure(
            text='CSV', value="csv", variable=self.fileTypeRd)
        self.fileTypeCSVRd.pack(padx=5, side="left")
        self.fileTypeJsonRd = Radiobutton(self.fileTypeLabelFrame)
        self.fileTypeJsonRd.configure(
            text='JSON', value="json", variable=self.fileTypeRd)
        self.fileTypeJsonRd.pack(padx=5, side="left")
        self.fileTypeLabelFrame.pack(fill="x", ipady=3, padx=5, side="top")
        self.fileOperateFrame = Frame(self.autoImportFrame)
        self.fileSelectBtn = Button(self.fileOperateFrame)
        self.fileSelectBtn.configure(text='选择文件')
        self.fileSelectBtn.pack(anchor="center", fill="x", side="top")
        self.fileSelectBtn.configure(command=self.fileSelect)
        self.fileOperateFrame.pack(fill="x", padx=5, pady=10, side="top")
        self.fileNameFrame = Frame(self.autoImportFrame)
        self.importFileNameLabel = Label(self.fileNameFrame)
        self.importFrlenameVar = StringVar()
        self.importFileNameLabel.configure(
            text='C:\\Network_List.csv',
            textvariable=self.importFrlenameVar)
        self.importFileNameLabel.pack(
            anchor="center", fill="x", padx=5, side="top")
        self.fileNameFrame.pack(anchor="center", padx=5, pady=5, side="top")
        self.dataValidateFrame = Frame(self.autoImportFrame)
        self.validateDataBtn = Button(self.dataValidateFrame)
        self.validateDataBtn.configure(text='检查数据有效性', state="disable")
        self.validateDataBtn.pack(anchor="w", fill="x", side="top")
        self.validateDataBtn.configure(command=self.validateData)
        self.dataValidateFrame.pack(fill="x", padx=5, side="top")
        self.importDataFrame = Frame(self.autoImportFrame)
        self.dataImportBtn = Button(self.importDataFrame)
        self.dataImportBtn.configure(text='导入数据')
        self.dataImportBtn.pack(fill="x", pady=5, side="top")
        self.dataImportBtn.configure(command=self.dataImport, state="disable")
        self.importDataFrame.pack(
            anchor="center",
            fill="x",
            padx=5,
            pady=5,
            side="top")
        self.autoImportFrame.pack(side="top")
        self.addDeviceNotebook.add(self.autoImportFrame, text='文件导入')

        # 手动输入
        self.inputFrame = Frame(self.addDeviceNotebook)
        self.addDeviceFrame = Frame(self.inputFrame)
        self.AddDeviceFrame = Frame(self.inputFrame)
        self.devNameLb = Label(self.AddDeviceFrame)
        self.devNameLb.configure(justify="left", text='设备名称:')
        self.devNameLb.grid(column=0, padx=5, pady=5, row=0)
        self.devNameEntry = Entry(self.AddDeviceFrame)
        self.devNameVar = StringVar()
        self.devNameEntry.configure(
            justify="left",
            textvariable=self.devNameVar,
            width=30)
        self.devNameEntry.grid(column=1, padx=5, pady=5, row=0)
        self.devTypeLb = Label(self.AddDeviceFrame)
        self.devTypeLb.configure(text='设备类型:')
        self.devTypeLb.grid(column=0, padx=5, pady=5, row=1)

        self.devTypeCb = Combobox(self.AddDeviceFrame)
        self.devTypeCb.configure(values=["交换机", "防火墙", "其他"], width=28)
        self.devTypeCb.current(0)

        self.devTypeCb.grid(column=1, padx=5, pady=5, row=1)
        self.devModelLb = Label(self.AddDeviceFrame)
        self.devModelLb.configure(text='设备型号:')
        self.devModelLb.grid(column=0, padx=5, pady=5, row=2)

        self.devModelCb = Combobox(self.AddDeviceFrame)
        self.devModelCb.configure(values=["思科", "H3C", "安点", "其他"], width=28)
        self.devModelCb.current(0)
        self.devModelCb.grid(column=1, padx=5, pady=5, row=2)

        self.devIPLb = Label(self.AddDeviceFrame)
        self.devIPLb.configure(justify="left", text='设备    IP:')
        self.devIPLb.grid(column=0, padx=5, pady=5, row=3)
        self.devIPEntry = Entry(self.AddDeviceFrame)
        self.devIPVar = StringVar()
        self.devIPEntry.configure(
            justify="left",
            textvariable=self.devIPVar,
            width=30)
        self.devIPEntry.grid(column=1, padx=5, pady=5, row=3)
        self.devSiteLb = Label(self.AddDeviceFrame)
        self.devSiteLb.configure(justify="left", text='所属装置:')
        self.devSiteLb.grid(column=0, padx=5, pady=5, row=4)
        self.devSiteEntry = Entry(self.AddDeviceFrame)
        self.devSiteVar = StringVar()
        self.devSiteEntry.configure(
            justify="left",
            textvariable=self.devSiteVar,
            width=30)
        self.devSiteEntry.grid(column=1, padx=5, pady=5, row=4)
        self.AddDeviceFrame.pack(anchor="center", side="top", fill='x')
        self.addDeviceEnsureFrame = Frame(self.inputFrame)
        self.addDevEnsureBtn = Button(self.addDeviceEnsureFrame)
        self.addDevEnsureBtn.configure(text='确定')
        self.addDevEnsureBtn.pack(padx=5, pady=5, side="right")
        self.addDevEnsureBtn.configure(command=self.addDevEnsure)

        self.addDeviceEnsureFrame.pack(expand=True, fill="both", side="top")

        self.inputFrame.pack(expand=True, fill="both", side="top")
        self.addDeviceNotebook.add(self.inputFrame, text='手动添加')
        self.addDeviceNotebook.pack(expand=True, fill="both", side="top")
        self.configure(height=200, padx=5, pady=5)
        self.resizable(False, False)
        self.title("添加设备")
        self.place_window_center()

    def fileSelect(self):
        pass

    def validateData(self):
        pass

    def dataImport(self):
        pass

    def addDevEnsure(self):

        dev_fields = self.read_fields()
        self.dev_info = dev_fields
        if not check_ip(dev_fields[3]):
            Messagebox.show_error(
                message="IP地址错误，请检查！",
                title="IP地址错误"
            )
            return

        fetch_cmd = '''
                SELECT * FROM DEVICEINFO where DEVIP="{}" OR DEVNAME="{}"
        '''.format(self.dev_info[3], self.dev_info[0])
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(fetch_cmd)
        fetch_data = cursor.fetchall()
        if fetch_data:
            Messagebox.show_warning('数据已存在, 请输入新的数据!', '数据已存在')
        else:
            self.parent.devListTreeview.insert('', 'end', values=self.dev_info)
            insert_db(self.dev_info)
            self.dev_info.clear()
            self.destroy()
        close_db(cursor, conn)

    def read_fields(self):
        dev_name = self.devNameVar.get()
        dev_type = self.devTypeCb.get()
        dev_model = self.devModelCb.get()
        dev_ip = self.devIPVar.get()
        dev_site = self.devSiteVar.get()
        return [dev_name, dev_type, dev_model, dev_ip, dev_site]
