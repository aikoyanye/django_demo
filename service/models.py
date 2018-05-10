import mongoengine

class User(mongoengine.Document):
    # 默认id
    # 名字，字符串字段，最大长度36位，默认字符KirisameMarisa，允许为空，不允许重复，
    name = mongoengine.StringField(max_length=36, unique=True)
    # 年龄，整型字段，最大长度5，不允许位空
    age = mongoengine.IntField(max_length=5, null=False)
    # 密码，最长12，不允许为空
    pwd = mongoengine.StringField(max_length=12, null=False)

    # 更多字段请百度