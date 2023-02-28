import os

import sys
# print(os.getcwd())
sys.path.append(os.getcwd()) 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieland.settings')
import django # isort:skip
django.setup() # isort:skip
from movieland.apps.movie.models import Programme


def main():
    p = Programme.objects.all()
    print(p)


if __name__ == "__main__":
    print(main())
