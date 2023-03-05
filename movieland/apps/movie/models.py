from django.db import models
import hashlib

# Create your models here.


class Programme(models.Model):
    movie_id = models.IntegerField(primary_key=True,)
    name = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    publish_year = models.CharField(max_length=30, default='其他', null=True, blank=True)
    detail_url = models.CharField(max_length=255, blank=True, null=True, default='')
    cover_img = models.CharField(max_length=255, blank=True, null=True, default='')
    uniquetag = models.CharField(max_length=255, blank=True, null=True, default='')
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def generate_uniquetag(self):
        key = self.name + self.detail_url
        machine = hashlib.sha256()
        machine.update(key.encode("utf-8"))
        return machine.hexdigest()

    def save(self, *args, **kwargs):
        self.uniquetag = self.generate_uniquetag()
        super(Programme, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return f"<Moive- {self.name} >"


class Channel(models.Model):
    """
        所属类型， 综艺，电影，动漫, 电视剧
    """
    channel_name = models.CharField(max_length=30, blank=True, null=True)
    movies = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='channel')

    def __str__(self) -> str:
        return f"<Channel- {self.channel_name}>"


class Category(models.Model):
    """
    分类
    """
    category_name = models.CharField(max_length=30, blank=True, null=True)
    movies = models.ManyToManyField(Programme)

    def __str__(self) -> str:
        return f"<Category- {self.name}>"
    
class Artist(models.Model):
    """
    演员艺人
    """
    # artist.movie
    artist_id =  models.IntegerField(primary_key=True,)
    movies = models.ManyToManyField(Programme)

    def __str__(self):
        return '<Aritst - %s>' % self.name


class Country(models.Model):
    """
    所属地区， 中国， 日本, 美国...
    """
    country_name = models.CharField(max_length=30, blank=True, null=True)
    movies = models.ManyToManyField(Programme)

    def __str__(self):
        return '<Country - %s>' % self.name

