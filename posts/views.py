from posts.models import Post, Category
from posts.serializers import PostSerializer, CatSerializer, CatDetailSerializer, PostViewSerializer
from rest_framework import generics  
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView  


class CatList(generics.ListCreateAPIView):  
    queryset = Category.objects.all()  
    serializer_class = CatSerializer

class CatDetail(generics.RetrieveAPIView):  
    queryset = Category.objects.all()  
    serializer_class = CatDetailSerializer

class PostView(APIView):
    permission_classess = [permissions.AllowAny, ]
    def get(self, request, pk=None):
        if pk:
            posts = get_object_or_404(Post.objects.all(), pk=pk)
            serializer = PostSerializer(posts)
            print(PostSerializer(serializer))
            return Response(serializer.data)
        else:
            posts = Post.objects.all()
            serializer = PostViewSerializer(posts, many=True)
            print(serializer)
            return Response(serializer.data)

    def post(self, request):
        post = request.data
        print(post)
        serializer = PostSerializer(data=post)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({'Success': "Post {} created successfully".format(post_saved.title)})

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({'Success': "Post {} updated successfully".format(post_saved.title)})
    
    def delete(self, request, pk):
        post = get_object_or_404(Post.objects.all(), pk=pk)
        title = post.title
        post.delete()
        return Response({'Success': "Post {} delete".format(title)}, status=204)

# class PostList(generics.ListCreateAPIView):  
#     queryset = Post.objects.all()  
#     serializer_class = PostSerializer
#     
# class PostDetail(generics.RetrieveAPIView):  
#     queryset = Post.objects.all()  
#     serializer_class = PostSerializer