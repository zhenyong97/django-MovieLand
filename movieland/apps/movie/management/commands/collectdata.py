from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'start to collect programme data'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        super(Command, self).add_arguments(parser)


    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS('hello world'))