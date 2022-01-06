from django.contrib import admin
from .models import Post

# 관리자모드에 Post 테이블 등록
admin.site.register(Post)

'''
위에서 등록 이후 꼭 아래의 마이그레이트 작업을 해줘야함.
C:\ProjectRoot> python manage.py makemigrations  ⇒ 데이터베이스에 변경이 필요한 사항을 추출
C:\ProjectRoot> python manage.py migrate ⇒ 데이터베이스에 변경사항을 반영함

'''

# Register your models here.
