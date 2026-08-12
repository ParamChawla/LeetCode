class Solution:
    def Solve(self,col,board,ans,leftrow,lowerDigonal,upperDigonal,n):
        if col==n:
            ans.append(board[:])
            return
        for row in range(n):
            if(
                leftrow[row]==0
                and lowerDigonal[row+col]==0
                and upperDigonal[n-1+col-row]==0
            ):
             board[row]=board[row][:col]+"Q"+board[row][col+1:]
             leftrow[row]=1
             lowerDigonal[row+col]=1
             upperDigonal[n-1+col-row]=1
             self.Solve(col+1,board,ans,leftrow,lowerDigonal,upperDigonal,n)
             board[row]=board[row][:col]+"."+board[row][col+1:]
             leftrow[row]=0
             lowerDigonal[row+col]=0
             upperDigonal[n-1+col-row]=0


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=["."*n for _ in range(n)]
        leftrow=[0]*n
        lowerDigonal=[0]*(2*n-1)
        upperDigonal=[0]*(2*n-1)
        self.Solve(0,board,ans,leftrow,lowerDigonal,upperDigonal,n)
        return ans
        