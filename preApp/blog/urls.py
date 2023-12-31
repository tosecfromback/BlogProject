from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", views.Index.as_view(), name='list'), 
    # 글 상세 조회
    path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    # 글 작성
    path("write/", views.PostCreateView.as_view(), name='write'),
    # 글 수정
    path("delete/<int:pk>/edit/", views.PostUpdateView.as_view(), name='edit'),
    # 글 삭제
    path("delete/<int:pk>/delete/", views.PostDeleteView.as_view(), name='delete'),
    # 글 검색
    path("search/<str:tag>/", views.Index.as_view(), name='list_srch'),
    # 코멘트 작성
    # path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    # 코멘트 삭제
    # path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    # 태그 작성
    # path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    # 태그 삭제
    # path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
]