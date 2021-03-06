# Generated by Django 2.1.1 on 2018-10-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, verbose_name='User')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('lat', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Lat')),
                ('long', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Long')),
            ],
        ),
    ]
