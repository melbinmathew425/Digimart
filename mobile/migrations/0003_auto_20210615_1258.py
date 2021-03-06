# Generated by Django 3.2.3 on 2021-06-15 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('orderplaced', 'orderplaced'), ('ordernotplace', 'ordernotplaced')], default='orderplaced', max_length=120),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('packed', 'packed'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='ordered', max_length=120)),
                ('date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.product')),
            ],
        ),
    ]
