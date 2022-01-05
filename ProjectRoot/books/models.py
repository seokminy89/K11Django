from django.db import models

# 도서 테이블 생성
class Book(models.Model):
    # 제목
    title = models.CharField(max_length=100)
    # 저자명 : Author 테이블의 PK와 N:N의 관계를 설정. 저자는 여러권의 책을 쓸 수 있다.
    authors = models.ManyToManyField('Author')
    # 출판사 : Publisher 테이블의 PK와 N:N의 관계를 설정. 책은 한 출판사에서만 출간된다.
    # on_delete=models.CASCADE 옵션은 오라클과 동일하게 부모레코드가 삭제될 때 자식까지 같이 삭제된다.
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    # 출판일 
    #publication_date = models.DateTimeField('date published') # 일종의 설명문
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    
# 저자 테이블 생성
class Author(models.Model):
    name = models.CharField(max_length=50) # 저자명
    salutation = models.CharField(max_length=100) # 인사말
    email = models.EmailField() # 이메일

    def __str__(self):
        return self.name

# 출판사 테이블 생성
class Publisher(models.Model): 
    name = models.CharField(max_length=50) # 출판사명
    address = models.CharField(max_length=100) # 주소
    website = models.URLField() #웹사이트URL

    def __str__(self):
        return self.name


# Create your models here.
