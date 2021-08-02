# Generated by Django 3.2 on 2021-08-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField()),
                ('PublicationDate', models.DateField()),
                ('Rating', models.FloatField()),
                ('CopyRightInfo', models.TextField()),
                ('NumberOfCopy', models.IntegerField()),
                ('Caption', models.CharField(max_length=50)),
                ('Quality_Old', models.CharField(choices=[('good', 'good'), ('damaged', 'damaged')], default='good', max_length=8)),
                ('Quality_New', models.CharField(choices=[('good', 'good'), ('damaged', 'damaged')], default='good', max_length=8)),
                ('Size', models.CharField(choices=[('a5', 'a5'), ('a4', 'a4'), ('a3', 'a3'), ('a2', 'a2'), ('a1', 'a1'), ('b3', 'b3'), ('b5', 'b5')], default='a5', max_length=8)),
                ('Price', models.CharField(max_length=14)),
                ('FrontCover', models.ImageField(upload_to=None)),
                ('BackCover', models.ImageField(upload_to=None)),
                ('FirstPage', models.ImageField(upload_to=None)),
                ('Body2nd', models.ImageField(upload_to=None)),
                ('PageInside', models.ImageField(upload_to=None)),
                ('DamagedPart', models.ImageField(upload_to=None)),
                ('Author', models.ManyToManyField(to='Accounts.Author')),
                ('PublisherInfo', models.ManyToManyField(to='Accounts.Publisher')),
            ],
        ),
    ]
