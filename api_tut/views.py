from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.



class ArticleView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        schema = ArticleSerializer(articles, many=True)
        return Response(schema.data)

    def post(self, request):
        schema = ArticleSerializer(request.data)

        if schema.is_valid():
            schema.save()
            return Response(schema.data, status=status.HTTP_201_CREATED)
        return Response(schema.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ArticleDetailView(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Exception as e:
            print(e)
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        article = self.get_objects(id)
        schema = ArticleSerializer(article)
        return Response(schema.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        article = self.get_object(id)
        schema = ArticleSerializer(article,data=request.data)
        if schema.is_valid():
            schema.save()
            return Response(schema.data)
        return Response(schema.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
