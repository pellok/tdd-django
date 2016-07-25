# tdd-django
練習 測試驅動開發使用Python

#寫第一個Function Test
#創建Django專案
django-admin.py startproject superlists
cd superlists
#啟動Django
python manage.py runserver

git init
vim .git/config
[alias]
  st=status

echo "*.pyc" >>.gitignore
echo db.sqlite >>.gitignore
