from django.db import models


# class NovelsData(models.Model):
#     id = models.CharField(primary_key=True, max_length=40)
#     type = models.CharField(max_length=20, verbose_name='小说类别')
#     novel_name = models.CharField(max_length=20, verbose_name='小说书名')
#     title = models.CharField(max_length=50, verbose_name='小说标题')
#     desc = models.TextField(verbose_name='概述')
#     author = models.CharField(max_length=20, verbose_name='作者')
#     image = models.ImageField(upload_to='novels', verbose_name='小说图片')
#     add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
#     chapter_name = models.CharField(max_length=20, verbose_name='章节名称')
#     # main_body =
#
#     class Meta:
#         db_table = 'novels_data'
#         verbose_name = '小说数据表'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.novel_name,self.chapter_name


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

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


class IndexBanner(models.Model):
    image = models.CharField(max_length=100)
    index = models.SmallIntegerField()
    novels = models.ForeignKey('Novels', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'index_banner'


class MyCacheTable(models.Model):
    cache_key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'my_cache_table'


class Mybookrack(models.Model):
    chapters_uid = models.IntegerField(blank=True, null=True)
    add_time = models.DateTimeField()
    is_delete = models.SmallIntegerField()
    novels = models.ForeignKey('Novels', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mybookrack'

#小说表
class Novels(models.Model):
    uid = models.CharField(primary_key=True, max_length=40)
    novel_name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    author = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    status = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    add_time = models.DateTimeField()
    update_time = models.DateTimeField()
    type = models.ForeignKey('NovelsType', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'novels'

#章节表
class NovelsChapter(models.Model):
    uid = models.CharField(primary_key=True, max_length=40)
    chaptername = models.CharField(max_length=20)
    add_time = models.DateTimeField()
    novels = models.ForeignKey(Novels, models.DO_NOTHING)
    path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'novels_chapter'


class NovelsCollection(models.Model):
    uid = models.CharField(primary_key=True, max_length=40)
    collec_time = models.DateTimeField(db_column='Collec_time')  # Field name made lowercase.
    novels = models.ForeignKey(Novels, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'novels_collection'


class NovelsData(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    type = models.CharField(max_length=20)
    novel_name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    author = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    add_time = models.DateTimeField()
    update_time = models.DateTimeField()
    chapter_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novels_data'


class NovelsHits(models.Model):
    uid = models.CharField(primary_key=True, max_length=40)
    hits_time = models.DateTimeField()
    novels = models.ForeignKey(Novels, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'novels_hits'


class NovelsType(models.Model):
    typename = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'novels_type'


class NovelsVice(models.Model):
    uid = models.CharField(primary_key=True, max_length=40)
    hits = models.IntegerField()
    collection = models.IntegerField()
    novels = models.ForeignKey(Novels, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'novels_vice'


class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=40)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    phone_num = models.CharField(unique=True, max_length=11)
    head_img = models.CharField(max_length=100)
    last_ip = models.CharField(max_length=32)
    is_author = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class UserGroups(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_permissions'
        unique_together = (('user', 'permission'),)

