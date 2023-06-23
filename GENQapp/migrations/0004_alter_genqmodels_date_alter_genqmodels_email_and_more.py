# Generated by Django 4.2 on 2023-04-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GENQapp', '0003_alter_genqmodels_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genqmodels',
            name='date',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='genqmodels',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AlterField(
            model_name='genqmodels',
            name='phone1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='genqmodels',
            name='phone2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='genqmodels',
            name='zip',
            field=models.IntegerField(default=0),
        ),
    ]
