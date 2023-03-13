from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile', 'nickname')

    # 유저 password 암호화하여 DB저장
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    # 유저 정보 변경 - UserAPIView patch와 연관
    def update(self, user, validated_data):
        # 수정된 정보일 경우만 저장
        if user.password != self.validated_data['password']:
            user.set_password(validated_data['password'])
        elif user.profile != self.validated_data['profile']:
            user.profile = validated_data.get('profile', user.profile)
        elif user.nickname != self.validated_data['nickname']:
            user.nickname = validated_data.get('nickname', user.nickname)
        user.save()
        return user