# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllImg(models.Model):
    img_url = models.CharField(max_length=255, blank=True, null=True)
    img_id = models.IntegerField(blank=True, null=True)
    img_des = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_img'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Culture(models.Model):
    icon_path = models.CharField(max_length=255, blank=True, null=True)
    icon_des = models.CharField(max_length=255, blank=True, null=True)
    icon_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'culture'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipment(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    equip_des = models.TextField(blank=True, null=True)
    equip_imgs = models.CharField(max_length=255, blank=True, null=True)
    update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment'


class GroupDict(models.Model):
    group_type = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_dict'


class ImgType(models.Model):
    img_type = models.CharField(max_length=255, blank=True, null=True)
    img_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'img_type'


class IncIntroduce(models.Model):
    content = models.TextField(blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inc_introduce'


class News(models.Model):
    new_title = models.CharField(max_length=255, blank=True, null=True)
    new_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class TeamRanking(models.Model):
    rank_id = models.IntegerField()
    team_name = models.CharField(max_length=255, blank=True, null=True)
    group_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_ranking'

GENDER_CHOICES = (
    (0, '男'),
    (1, '女'),
)
class User(models.Model):
    """用户信息模型类"""
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=256, verbose_name=u'用户名', null=True)
    password = models.CharField(max_length=256, verbose_name=u'密码', null=True)
    sex = models.CharField(max_length=256, choices=GENDER_CHOICES, verbose_name=u'性别', null=True)
    e_mail = models.CharField(max_length=256, verbose_name=u'邮箱', null=True)
    address = models.CharField(max_length=256, verbose_name=u'地址', null=True)
    sign = models.CharField(max_length=256, verbose_name=u'签名', null=True)
    icon = models.ImageField(upload_to='static/user', verbose_name='头像', null=True)


    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
