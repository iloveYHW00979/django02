# Generated by Django 2.2.6 on 2021-04-15 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jthjapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_path', models.CharField(blank=True, max_length=255, null=True)),
                ('icon_des', models.CharField(blank=True, max_length=255, null=True)),
                ('icon_title', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'culture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('equip_des', models.TextField(blank=True, null=True)),
                ('equip_imgs', models.CharField(blank=True, max_length=255, null=True)),
                ('update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'equipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_type', models.CharField(blank=True, max_length=255, null=True)),
                ('group_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'group_dict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImgType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_type', models.CharField(blank=True, max_length=255, null=True)),
                ('img_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'img_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IncIntroduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('img_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'inc_introduce',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeamRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_id', models.IntegerField()),
                ('team_name', models.CharField(blank=True, max_length=255, null=True)),
                ('group_type_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'team_ranking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=256, null=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, null=True, verbose_name='密码')),
                ('sex', models.CharField(choices=[(0, '男'), (1, '女')], max_length=256, null=True, verbose_name='性别')),
                ('e_mail', models.CharField(max_length=256, null=True, verbose_name='邮箱')),
                ('address', models.CharField(max_length=256, null=True, verbose_name='地址')),
                ('sign', models.CharField(max_length=256, null=True, verbose_name='签名')),
                ('icon', models.ImageField(null=True, upload_to='static/user', verbose_name='头像')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'user',
            },
        ),
    ]