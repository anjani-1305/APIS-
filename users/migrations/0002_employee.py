# Generated by Django 4.2.3 on 2023-07-06 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField()),
                ('active_employee', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('position', models.CharField(choices=[('IT Developer', 'Developer'), ('IT Engineer', 'Engineer'), ('Manager', 'Manager'), ('HR', 'HR')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company')),
            ],
        ),
    ]