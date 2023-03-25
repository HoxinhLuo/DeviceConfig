from ui import MainApp


if __name__ == "__main__":
    app = MainApp(title="网络设备管理", size=(880, 480), resizable=(False, False))
    app.place_window_center()
    app.run()
