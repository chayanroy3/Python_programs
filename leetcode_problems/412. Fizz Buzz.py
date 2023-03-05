class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            a.append(str(i))
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                a[i-1]="FizzBuzz"
            if i%3==0 and i%5!=0:
                a[i-1]="Fizz"
            if i%5==0 and i%3!=0:
                a[i-1]="Buzz"
        return a
