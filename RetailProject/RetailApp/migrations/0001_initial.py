# Generated by Django 3.1.7 on 2022-01-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('product_prize', models.CharField(max_length=50)),
                ('product_discription', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
