from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="059"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc072_a".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  n=int(input())
  a=list(map(int,input().split()))
  ans1,ans2=0,0
  tmp1,tmp2=0,0
  for i in range(n):
    tmp1+=a[i]
    tmp2+=a[i]
    if i%2==0:
      if tmp1<=0: ans1+=1-tmp1; tmp1=1
      if tmp2>=0: ans2+=tmp2+1; tmp2=-1
    else:
      if tmp1>=0: ans1+=tmp1+1; tmp1=-1
      if tmp2<=0: ans2+=1-tmp2; tmp2=1
  print(min(ans1,ans2))
  """ここから上にコードを記述"""

  print(test_case[__+1])