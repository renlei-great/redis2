# Generated by Django 2.2.7 on 2019-11-25 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('book_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=20)),
                ('hero_skill', models.CharField(max_length=128)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest1.Book')),
            ],
        ),
    ]
