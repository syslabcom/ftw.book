from ftw.builder import builder_registry
from ftw.builder.archetypes import ArchetypesBuilder


class BookBuilder(ArchetypesBuilder):

    portal_type = 'Book'

builder_registry.register('book', BookBuilder)


class ChapterBuilder(ArchetypesBuilder):

    portal_type = 'Chapter'

builder_registry.register('chapter', ChapterBuilder)


class TableBuilder(ArchetypesBuilder):

    portal_type = 'Table'

    def __init__(self, *args, **kwargs):
        super(TableBuilder, self).__init__(*args, **kwargs)
        self.table = None


    def with_table(self, table):
        """Fills the table with data represented as list of lists.
        """
        self.table = table
        return self

    def after_create(self, obj):
        self._update_table_data(obj, self.table)
        super(TableBuilder, self).after_create(obj)

    def _update_table_data(self, obj, table):
        if not table:
            return

        column_properties = obj.getColumnProperties()
        for column_index in range(len(table[0])):
            column_properties[column_index]['active'] = True

        data = map(lambda row: dict([('column_%i' % num, value)
                                     for num, value in enumerate(row)]),
                   table)
        obj.setData(data)

builder_registry.register('table', TableBuilder)