import sys

from django.core.management.commands.loaddata import Command as LoadDataCommand


class Command(LoadDataCommand):
    """
    A quick hack to support loading data from stdin, using the filename '-'.
    When doing so, json format is assumed.
    """
    def parse_name(self, fixture_name):
        # Hack the compression formats to include a 'stdin' format that
        # will read from sys.stdin
        self.compression_formats['stdin'] = (lambda x,y: sys.stdin, None)
        if fixture_name == '-':
            return '-', 'json', 'stdin'

    def find_fixtures(self, fixture_label):
        if fixture_label == '-':
            return [('-', None, '-')]
        return super(Command, self).find_fixtures(fixture_label)
