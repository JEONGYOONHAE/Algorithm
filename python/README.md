## Python

목록

- Dictionary



#### Dictionary

1. 딕셔너리 추가

   ```python
   >>> a = {1: 'a'}
   >>> a[2] = 'b'
   >>> a
   {1: 'a', 2: 'b'}
   ```

2.   딕셔너리 삭제

   ```python
   >>> del a[1]
   >>> a
   {2: 'b', 'name': 'pey', 3: [1, 2, 3]}
   ```

3.  key 이용해서 value 구하기

   ```python
   # 1. 
   >>> grade = {'pey': 10, 'julliet': 99}
   >>> grade['pey']
   10
   >>> grade['julliet']
   99
   
   # 2. get 사용
   >>> a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
   >>> a.get('name')
   'pey'
   >>> a.get('phone')
   '010-9999-1234'
   ```

4.  key, value 쌍 구하기 : items 사용

   ```python
   >>> a.items()
   dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])
   ```

5. 해당 key가 딕셔너리 안에 있는지 구하기

   ```python
   >>> a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
   >>> 'name' in a
   True
   >>> 'email' in a
   False
   ```











