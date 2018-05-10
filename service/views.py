from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# 规定该方法只能通过post、get和delete请求
@api_view(['POST', 'GET', 'DELETE'])

# request就是你的请求
def user_api(request):

    # 如果请求是get
    if request.method == 'GET':

        # 获取user表全部的用户
        users = User.objects.all()

        # 将获取结果序列化，当many=True的时候才允许返回多条数据，不然报错
        serializer = UserSerializer(users, many=True)

        # serializer.data是一个字典，status是状态码，2XX是成功返回
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 如果请求是post
    elif request.method == 'POST':

        # request.data也是一个字典，有兴趣可以 print(request.data)
        serializer = UserSerializer(data=request.data)

        # 如果数据符合规定，字符长度之类的
        if serializer.is_valid():

            # 保存
            serializer.save()

            # 同上
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # 如果不符合规定
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # 如果是delete请求
    elif request.method == 'DELETE':

        # 删除全部用户
        User.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 同上
@api_view(['GET', 'PUT', 'DELETE'])

# name是参数，这不是我常用的方法，仅仅是和大家说有这样的用法
def another_user_api(request, username):

    # 同上
    if request.method == 'GET':

        # 获取单个用户，其中name是字段名，username是参数
        # user = User.objects.get(name=username)

        # 由于我在models中没写不允许字段重复，所有get方法当有字段重复时会报错
        # filter就是根据条件查找，first很容易理解，就是第一条数据
        user = User.objects.filter(name=username).first()

        # 将结果序列化，不需要many=True
        serializer = UserSerializer(user)

        # 同上
        return Response(serializer.data, status=status.HTTP_200_OK)

    # put一般是修改
    elif request.method == 'PUT':

        # 同上
        user = User.objects.filter(name=username).first()

        # 同上，request.data是传入的要修改的新数据
        # 先把要修改的那条数据从数据库中获取，然后修改数据，保存
        serializer = UserSerializer(user, data=request.data)

        # 同样要检查数据合法性
        if serializer.is_valid():

            # 合法
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        # 不合法
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        # 同上
        user = User.objects.filter(name=username).first()

        # 删除
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 这样做的话我每次都是POST请求，但是返回却是自定义
@api_view(['POST'])
def android_user_api(request):
    if request.method == 'POST':
        _data = dict(request.data)
        # 之前说过request.data是一个字典，可以利用这个
        if _data['method'][0] == '_GET':
            user = User.objects.get(name=_data['name'][0], pwd=_data['pwd'][0])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif _data['method'][0] == '_POST':
            # request.data 中多余的数据不会保存到数据库中
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif _data['method'][0] == '_PUT':
            user = User.objects.get(name=_data['name'][0])
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif _data['method'][0] == '_DELETE':
            User.objects.get(name=_data['name'][0]).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)