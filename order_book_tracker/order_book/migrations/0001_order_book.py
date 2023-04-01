# Generated by Django 4.0.10 on 2023-03-30 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_code', models.CharField(max_length=10)),
                ('bid', models.FloatField()),
                ('ask', models.FloatField()),
                ('last_price', models.FloatField()),
                ('last_size', models.FloatField()),
                ('volume_24h', models.FloatField()),
                ('change_24h', models.FloatField()),
                ('low_24h', models.FloatField()),
                ('high_24h', models.FloatField()),
                ('avg_24h', models.FloatField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
