# Generated by Django 5.1.2 on 2024-10-24 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('pro_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
