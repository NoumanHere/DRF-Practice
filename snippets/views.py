from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnlyPermission



# Class Based Views with mixins

# class SnippetDetailView(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#         permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        
#         queryset = Snippet.objects.all()
#         serializer_class = SnippetSerializer

#         def get(self, request, *args, **kwargs):
#             return self.list(request, *args, **kwargs)
        
#         def post(self, request, *args, **kwargs):
#             return self.create(request, *args, **kwargs)

class SnippetListView(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnlyPermission]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnlyPermission]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Class Based Views

# class SnippetListView(APIView):
#     """
#     List all snippets or create a new snippet.
#     """
#     def get(self, request, format = None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data)
    
#     def post(self,request, format = None):
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetailView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk = pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format = None):
#         snippet = self.get_object(pk = pk)
#         serializer = SnippetSerializer(snippet, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request, pk, format = None):
#         snippet = self.get_object(pk = pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Function Based Views

# @api_view(['GET','POST'])
# def snippet_list(request, format = None):
#     """
#     List all snippets or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = request.data
#         serializer = SnippetSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = statsu.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk, format = None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk = pk)
#     except Snippet.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         data = request.data
#         serializer = SnippetSerializer(snippet, data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)