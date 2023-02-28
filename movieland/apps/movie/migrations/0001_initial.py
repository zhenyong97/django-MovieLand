# Generated by Django 4.1.6 on 2023-02-28 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('publish_year', models.CharField(blank=True, default='其他', max_length=30, null=True)),
                ('detail_url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('cover_img', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('uniquetag', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=30, null=True)),
                ('movies', models.ManyToManyField(to='movie.programme')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(blank=True, max_length=30, null=True)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel', to='movie.programme')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=30, null=True)),
                ('movies', models.ManyToManyField(to='movie.programme')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movies', models.ManyToManyField(to='movie.programme')),
            ],
        ),
    ]