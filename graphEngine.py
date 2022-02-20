from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtCore as qtc
import PyQt5.QtWebEngineWidgets as qwe
from io import StringIO


class WebEngineView(qwe.QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.page().profile().downloadRequested.connect(self.onDownloadRequested)
        self.windows = []

    @qtc.pyqtSlot(qwe.QWebEngineDownloadItem)
    def onDownloadRequested(self, download):
        if (
            download.state()
            == qwe.QWebEngineDownloadItem.DownloadRequested
        ):
            path, _ = qwe.QFileDialog.getSaveFileName(
                self, self.tr("Save as"), download.path()
            )
            if path:
                download.setPath(path)
                download.accept()

    def createWindow(self, type_):
        if type_ == qwe.QWebEnginePage.WebBrowserTab:
            window = QMainWindow(self)
            view = qwe.QWebEngineView(window)
            window.resize(640, 480)
            window.setCentralWidget(view)
            window.show()
            return view

    def updateChart(self, chart, **kwargs):
        output = StringIO()
        chart.save(output, "html", **kwargs)
        self.setHtml(output.getvalue())
