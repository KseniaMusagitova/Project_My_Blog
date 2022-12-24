# Generated by Django 3.2.8 on 2022-03-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220116_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField()),
                ('mac', models.IntegerField()),
                ('iphone', models.IntegerField()),
                ('android', models.IntegerField()),
                ('other', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
