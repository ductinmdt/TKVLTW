# Generated by Django 3.1.4 on 2021-12-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211214_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetails',
            name='img',
            field=models.CharField(db_column='IMG', default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(blank=True, db_column='OrderDate', default='2021-12-15'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2021-12-15'),
        ),
    ]
