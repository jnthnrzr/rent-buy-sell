# Generated by Django 2.2 on 2019-04-23 20:17

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Miscellaneous', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('option', models.CharField(choices=[('B', 'Buy It Now'), ('R', 'Rent'), ('A', 'Auction')], default='B', max_length=1)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('takedown_date', models.DateField(default=datetime.date(2019, 4, 30))),
                ('takedown_time', models.TimeField(default=datetime.time(16, 17, 54, 787558))),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_active', models.BooleanField(blank=True, default=True, max_length=100)),
                ('current_bidder', models.PositiveIntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='')),
                ('phone', models.CharField(blank=True, default='2126507000', max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number')),
                ('address', models.CharField(max_length=40, verbose_name='Street Address')),
                ('address2', models.CharField(max_length=40, null=True, verbose_name='Apt / Floor')),
                ('city', models.CharField(default='New York', max_length=25, verbose_name='City')),
                ('state', models.CharField(default='NY', max_length=20, verbose_name='State')),
                ('zipcode', models.CharField(default='10031', max_length=5, verbose_name='ZIP code')),
                ('country', models.CharField(blank=True, default='USA', max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, default='0.00', max_digits=7)),
                ('transactions', models.PositiveIntegerField(blank=True, default='0', verbose_name='Number of transactions')),
                ('suspensions', models.PositiveIntegerField(default='0', verbose_name='Number of suspensions')),
                ('strikes', models.PositiveIntegerField(default=0, verbose_name='Number of strikes')),
                ('credit_card', models.CharField(blank=True, default='1234999912348888', max_length=16)),
                ('verified_by_admin', models.BooleanField(default=False, verbose_name='RBS Verified User')),
                ('rbs_rating', models.DecimalField(blank=True, decimal_places=2, default='5.00', max_digits=3)),
                ('rbs_vip_user', models.BooleanField(default=False, verbose_name='RBS VIP User')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('products', models.ManyToManyField(to='marketplace.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='marketplace.UserProfile')),
            ],
            options={
                'verbose_name': 'Shopping Cart',
                'verbose_name_plural': 'Shopping Carts',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='marketplace.Product')),
                ('rated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rater', to='marketplace.UserProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.UserProfile'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('products', models.ManyToManyField(to='marketplace.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(blank=True, default='No details', max_length=512, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.Product')),
            ],
        ),
    ]
