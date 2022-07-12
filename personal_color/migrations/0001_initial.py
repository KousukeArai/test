# Generated by Django 3.2.7 on 2022-07-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[(1, '女性'), (2, '男性'), (3, 'その他'), (4, '無回答')], default=1, max_length=100, verbose_name='gender')),
                ('img', models.ImageField(upload_to='media/', verbose_name='img')),
            ],
        ),
    ]
