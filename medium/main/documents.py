# from django_elasticsearch_dsl import DocType, Index, fields
# from .models import *


# post = Index('posts')
# # See Elasticsearch Indices API reference for available settings
# post.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )


# @post.doc_type
# class PostDocument(DocType):

#     class Meta:
#         model = Post  # The model associated with this DocType

#         # The fields of the model you want to be indexed in Elasticsearch
#         fields = [
#             'title',
#             'slug',
#             'body',
#         ]


# @post.doc_type
# class CommentDocument(DocType):
#     post = fields.ObjectField(properties={
#         'title': fields.TextField(),
#         'slug': fields.TextField(),
#     })

#     class Meta:
#         model = Comment  # The model associated with this DocType

#         # The fields of the model you want to be indexed in Elasticsearch
#         fields = [
#             'name',
#             'email',
#             'body',
#         ]
#     related_models = [post]

#     # def get_queryset(self):
#     #     """Not mandatory but to improve performance we can select related in one sql request"""
#     #     return super(PostDocument, self).get_queryset().select_related(
#     #         'post'
#     #     )

#     # def get_instances_from_related(self, related_instance):
#     #     """If related_models is set, define how to retrieve the Car instance(s) from the related model.
#     #     The related_models option should be used with caution because it can lead in the index
#     #     to the updating of a lot of items.
#     #     """
#     #     if isinstance(related_instance, post):
#     #         return related_instance.car_set.all()

#     # Ignore auto updating of Elasticsearch when a model is saved
#     # or deleted:
#     # ignore_signals = True
#     # Don't perform an index refresh after every update (overrides global setting):
#     # auto_refresh = False
#     # Paginate the django queryset used to populate the index with the specified size
#     # (by default there is no pagination)
#     # queryset_pagination = 5000
