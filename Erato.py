import math

n=1000 #2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n+1)]#처음엔 모든 수가 소수인것으로 초기화(0과 1 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):#2부터 n의 제곱근까지의 모든 수를 확인
    if array[i] == True:#i가 소수
        #i 외 모두 제거
    j=2
    while i*j <=n:
        array[i*j]=False
        j+=1
    for i in range(2,n+1):
        if array[i]:
            print(i, end=' ')