# Generated by Django 2.0 on 2018-02-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('api', '0003_auto_20180114_1426')]

    operations = [
        migrations.CreateModel(
            name='Consultaion',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                )
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(
                blank=True, default='default.jpg', null=True, upload_to=''
            ),
        ),
    ]
