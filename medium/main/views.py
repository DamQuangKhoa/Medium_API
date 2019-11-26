from django.contrib.auth.models import User
from django.http import JsonResponse

from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from taggit.models import Tag
from rest_framework.permissions import IsAdminUser
from . import documents
from elasticsearch_dsl.query import MultiMatch

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from . import utils

# class IsAdmindNotGet(IsAdminUser):
#     """
#     If request == get >  >  > just request = get not authen, other request must admin
#     """

#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return True
#         return super(IsAdmindNotGet, self).has_permission(request, view)


# class PostList(viewsets.GenericViewSet, generics.ListCreateAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#     # permission_classes = (IsAdmindNotGet, )
#     keyword_fields = ['title',
#                       'slug',
#                       'body',
#                       'publish', ]

#     def get_queryset(self):
#         qs = self.request.query_params.get('q', None)
#         if qs is None:
#             return self.queryset

#         words = qs.split(',')
#         search = documents.PostDocument.search()
#         match = MultiMatch(query=' '.join(
#             words), fields=self.keyword_fields, type='best_fields')
#         # q = Q('nested', path='skills', query=Q('match', skills__name=qs)) | Q(match)
#         search = search.query(match)
#         return search.to_queryset()


# class PostDetail(viewsets.GenericViewSet,
#                  generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer


# class CommentList(viewsets.GenericViewSet, generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = (IsAdmindNotGet, )


# class CommentDetail(viewsets.GenericViewSet,
#                     generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = (IsAdmindNotGet, )


# class TagList(viewsets.GenericViewSet,
#               generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


class CategoryList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Products.objects.filter(status=200)
    serializer_class = ProductSerializer


class UserList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class CateProductList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = CateProduct.objects.all()
    serializer_class = CateProductSerializer


class PopularityList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Products.objects.filter(status=200).order_by("-value_count")[:100]
    serializer_class = ProductSerializer


# -------------CATEGORY CLASS-------------------
# All Category 1 IDs and names
class Category_1(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate1_id", "cate1_name").distinct()
    serializer_class = Category_1_Serializer


# All Category 2 IDs and names
class Category_2(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate2_id", "cate2_name").distinct()
    serializer_class = Category_2_Serializer


class Category_3(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate3_id", "cate3_name").distinct()
    serializer_class = Category_3_Serializer


# -------------END OF CATEGORY CLASS----------------

# -----------SUB CATEGORY------------
class Category_1_2(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = (
        Category.objects.filter(cate1_id=1686)
        .values("cate2_id", "cate2_name")
        .distinct()
    )
    serializer_class = Category_2_Serializer


# ----------Top products of cate 1,2,3 id-----------
class Category_prod_1_top(APIView):
    def get(self, request, cate1_id, format=None):
        catObjList = Category.objects.filter(cate1_id=cate1_id).all()
        list_cate3_id_new = list(map(lambda x: x.cate3_id_new, catObjList))
        listProductID = utils.getAllProduct_fromListCate3(list_cate3_id_new)
        listProductInfo = Products.objects.filter(
            pk__in=listProductID, status=200
        ).order_by("-value_count")[:100]

        products = [product.product_id for product in listProductInfo]
        serializer = ProductSerializer(listProductInfo, many=True)

        return Response(serializer.data)


class Category_prod_2_top(APIView):
    def get(self, request, cate2_id, format=None):
        catObjList = Category.objects.filter(cate2_id=cate2_id).all()
        list_cate3_id_new = list(map(lambda x: x.cate3_id_new, catObjList))
        listProductID = utils.getAllProduct_fromListCate3(list_cate3_id_new)
        listProductInfo = Products.objects.filter(
            pk__in=listProductID, status=200
        ).order_by("-value_count")[:100]

        products = [product.product_id for product in listProductInfo]
        serializer = ProductSerializer(listProductInfo, many=True)

        return Response(serializer.data)


class Category_prod_3_top(APIView):
    def get(self, request, cate3_id, format=None):
        catObjList = Category.objects.filter(cate3_id=cate3_id).all()
        list_cate3_id_new = list(map(lambda x: x.cate3_id_new, catObjList))
        listProductID = utils.getAllProduct_fromListCate3(list_cate3_id_new)
        listProductInfo = Products.objects.filter(
            pk__in=listProductID, status=200
        ).order_by("-value_count")[:100]

        products = [product.product_id for product in listProductInfo]
        serializer = ProductSerializer(listProductInfo, many=True)

        return Response(serializer.data)


# -------------End of top product of category---------

# -----------Top Children category of a category-------
class Category_cate_1_top(APIView):
    def get(self, request, cate1_id, format=None):
        cat1Obj = Category.objects.filter(cate1_id=cate1_id).all()
        cat2_id_list = list(set(map(lambda x: x.cate2_id, cat1Obj)))

        totalCountList = []

        for id_2 in cat2_id_list:
            sampleCat3_new = Category.objects.filter(
                cate1_id=cate1_id, cate2_id=id_2
            ).all()
            sampleCat3_list = list(map(lambda x: x.cate3_id_new, sampleCat3_new))
            totalCount = utils.getTotalValueCount_fromListCate3(sampleCat3_list)
            totalCountList.append(totalCount)

        return Response((dict(zip(cat2_id_list, totalCountList))))


class Category_cate_2_top(APIView):
    pass


# -------------------End of top Children category of a category

# -----------Category filter--------------
class CategoryFilter(generics.ListCreateAPIView):
    serializer_class = CategoryFilter_Serializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        print("IM IN THE QUERY SET")
        print(self)
        queryset = Category.objects.all()

        cate1_id = self.request.query_params.get("cate1_id", None)
        cate2_id = self.request.query_params.get("cate2_id", None)

        if cate1_id is not None:
            if cate2_id is not None:
                queryset = queryset.filter(cate1_id=cate1_id, cate2_id=cate2_id)
            else:
                queryset = queryset.filter(cate1_id=cate1_id)
        elif cate2_id is not None:
            queryset = queryset.filter(cate2_id=cate2_id)

        return queryset


# ----------_End of Category filter-------
# class SessionViewSet(viewsets.ModelViewSet):
#     queryset = Session.objects.all()
#     serializer_class = SessionSerializer

#     def get(self, request, format=None):
#         return Response("test")


# class TopCat1(APIView):
#     def get(self, request, format=None):
#         return Response("hello world")


# class Cate1_Product(viewsets.GenericViewSet, generics.ListCreateAPIView):
#     queryset = CateProduct.objects.filter(cate3_new_id.cate1_id=1108)
