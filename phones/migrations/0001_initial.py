# Generated by Django 3.2.9 on 2021-11-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('phone_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y%m%d')),
                ('release_date', models.DateField(blank=True)),
                ('lte_exists', models.BooleanField(default=False)),
            ],
        ),
    ]