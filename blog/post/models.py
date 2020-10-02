from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Category(models.Model):
    cname = models.CharField(max_length=20, unique=True, verbose_name="类别名称")

    def __str__(self):
        return "Category:%s" % (self.cname)

    class Meta:
        verbose_name_plural = "类别"
        db_table = "cate"


class Tag(models.Model):
    tname = models.CharField(max_length=20, unique=True, verbose_name="标签名称")

    def __str__(self):
        return "Tag:%s" % (self.tname)

    class Meta:
        verbose_name_plural = "标签"
        db_table = "tag"


class Post(models.Model):
    title = models.CharField(max_length=40, unique=True, verbose_name="标题")
    desc = models.TextField(verbose_name="信息描述")
    content = RichTextUploadingField(
        null=True, verbose_name="帖子内容", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="类别")
    tag = models.ManyToManyField(Tag, verbose_name="标签")

    def __str__(self):
        return "Tag:%s" % (self.title)

    class Meta:
        verbose_name_plural = "帖子"
        db_table = "post"
