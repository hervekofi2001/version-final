# Generated by Django 2.2.12 on 2021-08-24 23:48

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('motdepass', models.CharField(max_length=8)),
                ('localisation', models.CharField(max_length=50)),
                ('gps', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mesurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumFiber', models.CharField(max_length=5)),
                ('PerteConnecteur', models.CharField(max_length=50)),
                ('CumuleConnecteur', models.CharField(max_length=50)),
                ('PerteDistance', models.CharField(max_length=50)),
                ('CumuleDistance', models.CharField(max_length=50)),
                ('BilanPertes', models.CharField(max_length=50)),
                ('LongueurCable', models.CharField(max_length=50)),
                ('Episure', models.CharField(max_length=50)),
                ('rapport', models.CharField(blank=True, editable=False, max_length=255)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reflecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumFiber', models.CharField(max_length=5)),
                ('PerteConnecteur', models.CharField(max_length=50)),
                ('CumuleConnecteur', models.CharField(max_length=50)),
                ('PerteDistance', models.CharField(max_length=50)),
                ('CumuleDistance', models.CharField(max_length=50)),
                ('BilanPertes', models.CharField(max_length=50)),
                ('LongueurCable', models.CharField(max_length=50)),
                ('Episure', models.CharField(max_length=50)),
                ('photo', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Technicien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('motdepass', models.CharField(max_length=8)),
                ('statut', models.CharField(max_length=50, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_client', models.BooleanField(default=False)),
                ('is_technicien', models.BooleanField(default=False)),
                ('is_partenaire', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descrp', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tchat.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(default=0, max_length=200)),
                ('lng', models.CharField(default=0, max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tchat.Zone')),
            ],
        ),
    ]