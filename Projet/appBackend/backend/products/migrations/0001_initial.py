# Generated by Django 4.0.4 on 2022-05-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Laptoop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('marque', models.CharField(max_length=150)),
                ('taille_ecran', models.CharField(max_length=100)),
                ('taille_disque', models.CharField(max_length=100)),
                ('cpu', models.CharField(max_length=100)),
                ('systeme_exploitation', models.CharField(max_length=100)),
                ('caracteristique_speciale', models.CharField(max_length=100)),
                ('coprocesseur_graphique', models.CharField(max_length=100)),
                ('vitesse_CPU', models.CharField(max_length=100)),
                ('description_disque', models.CharField(max_length=100)),
                ('resolution', models.CharField(max_length=100)),
            ],
        ),
    ]
