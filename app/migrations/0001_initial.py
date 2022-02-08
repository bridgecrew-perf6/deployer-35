# Generated by Django 4.0.2 on 2022-02-08 09:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_framework_api_key', '0004_prefix_hashed_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('script_path', models.CharField(max_length=256, verbose_name='script path')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAPIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('apikey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_keys', to='rest_framework_api_key.apikey')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_keys', to='app.project')),
            ],
        ),
    ]