from .base import FormatColumn


class BoolColumn(FormatColumn):
    ch_type = 'Bool'
    py_types = (bool, )
    format = '?'

    def write_items(self, items, buf):
        super(BoolColumn, self).write_items(items, buf)