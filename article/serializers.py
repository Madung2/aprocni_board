from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Article, Comment
from .service import has_numbers



class ArticleSerializer(serializers.ModelSerializer):

    def validate(self, data):
        password= data['password']
        default_len=6

        if not has_numbers(password): 
            raise serializers.ValidationError(detail={"detail": "비밀번호에 숫자를 포함해주세요"})
        if len(password)<default_len:
            raise serializers.ValidationError(detail={"detail": "비밀번호는 6자리 이상이어야 합니다"})
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        article=Article(**validated_data)
        article.save()
        return validated_data

    class Meta:
        model = Article
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
