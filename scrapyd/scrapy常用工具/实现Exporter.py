#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
其中的每一个Exporter都是BaseItemExporter的一个子类，BaseItemExporter定义了一些抽象接口待子类实现：
●　export_item(self, item) 负责导出爬取到的每一项数据，参数item为一项爬取到的数据，每个子类必须实现该方法。
●　start_exporting(self) 在导出开始时被调用，可在该方法中执行某些初始化工作。
●　finish_exporting(self) 在导出完成时被调用，可在该方法中执行某些清理工作。

以JsonItemExporter为例，其实现非常简单：
●　为了使最终导出结果是一个json中的列表，在start_exporting和finish_exporting方法中分别向文件写入b"[\n, b"\n]"。
●　在export_item方法中，调用self.encoder.encode方法将一项数据转换成json串（具体细节不再赘述），然后写入文件。

以Excel为例：如下

完成ExcelExporter后,在配置文件settings.py添加如下代码：
FEED_EXPORTERS = {'excel': 'example.my_exporters.ExcelItemExporter'}

"""

from scrapy.exporters import BaseItemExporter
import xlwt

class ExcelItemExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        self._configure(kwargs)
        self.file = file
        self.wbook = xlwt.Workbook()
        self.wsheet = self.wbook.add_sheet('scrapy')
        self.row = 0

    def finish_exporting(self):
        self.wbook.save(self.file)

    def export_item(self, item):
        fields = self._get_serialized_fields(item)
        for col, v in enumerate(x for _, x in fields):
            self.wsheet.write(self.row, col, v)
            self.row += 1