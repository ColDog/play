# Generated by Django 2.0.3 on 2018-09-19 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0001_initial'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='HeatGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('heat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Heat')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SnakeHeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Heat')),
            ],
        ),
        migrations.CreateModel(
            name='SnakeTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snake.Snake', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='snaketournament',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament'),
        ),
        migrations.AddField(
            model_name='snakeheat',
            name='snake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.SnakeTournament'),
        ),
        migrations.AddField(
            model_name='round',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament'),
        ),
        migrations.AddField(
            model_name='heat',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Round'),
        ),
        migrations.AlterUniqueTogether(
            name='snaketournament',
            unique_together={('snake', 'tournament')},
        ),
        migrations.AlterUniqueTogether(
            name='snakeheat',
            unique_together={('heat', 'snake')},
        ),
        migrations.AlterUniqueTogether(
            name='round',
            unique_together={('number', 'tournament')},
        ),
    ]