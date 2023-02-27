from django.db import models
import hashlib

# Create your models here.


class Program(models.Model):
    movie_id = models.IntegerField(primary_key=True,)
    name = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    publish_year = models.CharField(max_length=30, default='其他', null=True, blank=True)
    detail_url = models.CharField(max_length=255, blank=True, null=True, default='')
    cover_img = models.CharField(max_length=255, blank=True, null=True, default='')
    uniquetag = models.CharField(max_length=255, blank=True, null=True, default='')

    def generate_uniquetag(self):
        key = self.name + self.detail_url
        machine = hashlib.sha256()
        machine.update(key.encode("utf-8"))
        return machine.hexdigest()

    def __str__(self) -> str:
        return f"<Moive- {self.name} >"

class Category(models.Model):
    """
    电影分类
    """
    category_name = models.CharField(max_length=30, blank=True, null=True)
    movies = models.ManyToManyField(Movie)

    def __str__(self) -> str:
        return f"<Category- {self.name}>"
    
class Artist(models.Model):
    """
    演员艺人
    """
    # artist.movie
    artist_id =  models.IntegerField(primary_key=True,)
    movies = models.ManyToManyField(Movie)

    def __repr__(self):
        return '<Aritst - %s>' % self.name


class Country(models.Model):
    """
    所属地区， 中国， 日本 ， 美国...
    """
    country_name = models.CharField(max_length=30, blank=True, null=True)
    movies = models.ManyToManyField(Movie)

    def __repr__(self):
        return '<Country - %s>' % self.name

