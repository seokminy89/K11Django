from django.contrib import admin
from books.models import Book, Author, Publisher

#admin 페이지(관리자모드)에 테이블이 보이도록 등록
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

# Register your models here.
'''
윗부분 작성한 뒤에는 
실제 DB에 반영되도록 마이그레이트


C:\ProjectRoot> python manage.py makemigrations  ⇒ 데이터베이스에 변경이 필요한 사항을 추출
C:\ProjectRoot> python manage.py migrate ⇒ 데이터베이스에 변경사항을 반영함


'''