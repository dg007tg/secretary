# Generated by Django 2.1.7 on 2019-03-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('account', models.IntegerField(verbose_name=0)),
                ('bank', models.TextField()),
                ('balance', models.IntegerField(verbose_name=0)),
                ('fund_change', models.IntegerField(verbose_name=0)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=32)),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField(verbose_name=0)),
            ],
        ),
        migrations.CreateModel(
            name='Salery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('amount', models.FloatField(verbose_name=0)),
                ('date', models.DateTimeField()),
                ('position', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('authority', models.IntegerField(verbose_name=0)),
            ],
        ),
    ]
