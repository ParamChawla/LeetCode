class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)
        stack=[]
        for i in range(0,n):#insert the positive in the stack
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:#now check when the negative comes wether the top element is greater than 0 and then check whther it is less tha the negative or not if yes than pop
                while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()
                if len(stack)!=0 and stack[-1]==abs(asteroids[i]):#if value of both top and minus elemnt are same then pop the top element basically remove both
                    stack.pop()
                elif len(stack)==0 or stack[-1]<0:#at last if there is nothing in stack puch the negative elements if there any
                    stack.append(asteroids[i])
        return stack        