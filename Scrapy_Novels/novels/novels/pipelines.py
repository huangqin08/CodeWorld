# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from novels.items import NovelsItem, NovelsItem, NovelsChapterItem
from savenovelsdate.models import Novels, NovelsChapter, NovelsType,User


class NovelsPipeline:
    def process_item(self, item, spider):

        # if isinstance(dict(item), NovelsItem):
        #     pass
        #
        # if isinstance(dict(item), NovelsChapterItem):
        #     pass
        #
        # if isinstance(dict(item), NovelsItem):
        #     pass
        #
        # item.save()
        # return item

        def _check_type(typename):
            try:
                ins = NovelsType.objects.get(typename=typename)
                return ins
            except:
                return None

        def _check_novel(uid):
            try:
                ins = Novels.objects.get(uid=uid)
                return ins
            except:
                return None

        # if isinstance(item, dict):
        #
        #     # 提取 两个 ITEM
        #     typeitem = item['typeitem']
        #     novelsitem = item['novelsitem']
        #     novelschapteritem = item['novelschapteritem']
        #     typename = typeitem['typename']
        #     n_uid = novelsitem['uid']
        #     novelschapteritems_ = 0
        #
        #     if _check_type(typename):
        #         typeitem = _check_type(typename)
        #
        #     type = NovelsType.objects.filter(typename=typename).first()
        #     id = type.id
        #     type1 = NovelsType.objects.get(id=id)
        #     novelsitem['type'] = type1
        #
        #     user=User.objects.get(uid='f8e26ca9f2984595b9886eb81f7375de')
        #     novelsitem['user'] = user
        #
        #     # 判断该小说是否存在
        #     if _check_novel(n_uid):
        #         novelsitem = _check_novel(n_uid)
        #         chapters_ = len(novelsitem.recruit_set.filter(uid=novelschapteritem['novels']))
        #
        #     # 保存数据
        #     novelsitem.save()
        #
        #     # 判断章节是否有重复
        #     if novelschapteritems_ == 0:
        #         novelschapteritem['novels'] = Novels.objects.get(uid=n_uid)
        #         novelschapteritem.save()
        #
        #     return item
        if isinstance(item, dict):
            # 提取 两个 ITEM
            typeitem = item['typeitem']
            novelsitem = item['novelsitem']
            typename = typeitem['typename']
            n_uid = novelsitem['uid']

            # 判断该小说是否存在
            if not _check_novel(n_uid):
                if _check_type(typename):
                    type = NovelsType.objects.filter(typename=typename).first()
                    id = type.id
                    type1 = NovelsType.objects.get(id=id)
                    novelsitem['type'] = type1
                user = User.objects.get(uid='f8e26ca9f2984595b9886eb81f7375de')
                novelsitem['user'] = user
                # 保存数据
                novelsitem.save()
            novelschapteritem = item['novelschapteritem']
            novelschapteritem['novels'] = Novels.objects.get(uid=n_uid)
            # print("----------------------->123123")
            novelschapteritem.save()
            # print("----------------------->345345")
            return item
