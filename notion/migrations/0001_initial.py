# Generated by Django 3.1.1 on 2021-10-21 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_url', models.URLField()),
                ('internal_integration_token', models.CharField(default='', max_length=300)),
                ('bearer_token', models.CharField(default='', max_length=200)),
                ('version', models.CharField(default='2021-05-13', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('external_id', models.UUIDField()),
                ('notion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='notion.notion')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='notion.page')),
            ],
        ),
    ]
