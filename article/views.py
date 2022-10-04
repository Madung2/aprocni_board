from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from article.serializers import ArticleSerializer, CommentSerializer
from ipware import get_client_ip 
from .models import Article, Comment, Like
from .service import has_negative_words

# Create your views here.
class ArticleAView(APIView):

    def get(self, request):
        article=Article.objects.filter(board='A').order_by('-created_at')
        serializer=ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
    
        ip, is_routable = get_client_ip(request)
        
        data = request.data
        data['ip_address']=ip
        data['board']='A'

        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id):
        article = Article.objects.get(uid=article_id)
        serializer = ArticleSerializer(article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id):
        article = Article.objects.get(uid=article_id)
        if article.ip_address == get_client_ip(request):
            article.delete()
            return Response({"message": "해당 게시글이 삭제 되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "게시글 작성 ip가 아닙니다"}, status=status.HTTP_400_BAD_REQUEST)


class ArticleBView(APIView):

    def get(self, request):
        article=Article.objects.filter(board='B').order_by('-created_at')
        serializer=ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ip, is_routable = get_client_ip(request)
        
        data = request.data
        data['ip_address']=ip
        data['board']='B'
        
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id):
        article = Article.objects.get(uid=article_id)
        serializer = ArticleSerializer(article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id):

        article = Article.objects.get(uid=article_id)
        if article.ip_address == get_client_ip(request):
            article.delete()
            return Response({"message": "해당 게시글이 삭제 되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "게시글 작성 ip가 아닙니다"}, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, article_id):
        if has_negative_words(request):
            return Response({"message": "모욕적인 단어가 포함되어 있습니다"}, status=status.HTTP_400_BAD_REQUEST)
        ip, is_routable = get_client_ip(request)
        request.data["ip_address"] = ip
        request.data['article']=article_id

        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id):
        comment = Comment.objects.get(id=article_id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id):
        comment = Comment.objects.get(id=article_id)
        
        if comment.ip_address == get_client_ip(request):
            comment.delete()
            return Response({"message": "댓글이 삭제되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "댓글 작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)

class LikeView(APIView):
    
    def post(self, request, article_id):
        ip, is_routable = get_client_ip(request)
        new_like, created = Like.objects.get_or_create(article=article_id, ip_address=ip)
        if created:
            new_like.save()
            return Response({"message": "좋아요 하셨습니다"}, status=status.HTTP_200_OK)
        new_like.delete()
        return Response({"message":"좋아요 취소 하셨습니다"}, status=status.HTTP_200_OK)
