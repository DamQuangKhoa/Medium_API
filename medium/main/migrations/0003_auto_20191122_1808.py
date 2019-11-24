# Generated by Django 2.1.5 on 2019-11-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191121_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='CateProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cate_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('product_name', models.TextField()),
                ('uri', models.TextField(blank=True, null=True)),
                ('oldprice', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('value_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=50, null=True)),
                ('last_activity', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'managed': False},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
