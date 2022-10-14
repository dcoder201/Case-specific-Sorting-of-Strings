#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
       ll=list(s)
       ll.sort()
       l1=[]
       l2=[]
       for i in ll:
           if(i>='A' and i<='Z'):
               l1.append(i)
           else:
               l2.append(i)
       x=0
       y=0
       ss=""
       for i in range(0,len(s)):
           if(s[i]>='A' and s[i]<='Z'):
             ss+=l1[x]
             x=x+1
           else:
             ss+=l2[y]
             y=y+1
       return ss


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends
