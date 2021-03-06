# Generated by Django 3.1.1 on 2021-10-25 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notion', '0002_auto_20211025_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('title', 'title'), ('rich_text', 'rich_text')], max_length=20)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('text', 'text'), ('number', 'number')], default='text', max_length=30)),
                ('value', models.CharField(default='', max_length=200)),
                ('color', models.CharField(choices=[('DEFAULT ', 'default'), ('GRAY ', 'gray'), ('BROWN ', 'brown'), ('RED ', 'red'), ('ORANGE ', 'orange'), ('YELLOW ', 'yellow'), ('GREEN ', 'green'), ('BLUE ', 'blue'), ('PURPLE ', 'purple'), ('PINK ', 'pink')], default='default', max_length=10)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='notion.property')),
            ],
        ),
    ]
