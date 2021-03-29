# Generated by Django 3.1.4 on 2021-03-28 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('Name', models.CharField(max_length=30)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('NumberBuy', models.IntegerField(blank=True, null=True)),
                ('Made_in', models.CharField(max_length=40)),
                ('Sales', models.BooleanField(blank=True, null=True)),
                ('New_Price', models.IntegerField(blank=True, null=True)),
                ('Image', models.ImageField(upload_to='')),
                ('Description', models.TextField(blank=True, null=True)),
                ('CategoryID', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Height', models.IntegerField(blank=True, null=True)),
                ('Weight', models.IntegerField(blank=True, null=True)),
                ('DOB', models.DateTimeField()),
                ('Gender', models.CharField(max_length=40)),
                ('UserID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('UserID', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('VestsID', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.vests')),
            ],
        ),
        migrations.CreateModel(
            name='BillUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Image', models.ImageField(upload_to='')),
                ('Ship', models.BooleanField(blank=True, null=True)),
                ('UserID', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
