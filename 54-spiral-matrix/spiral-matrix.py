class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        total=n*m
        ans=[]
        c=0
        colstart=0
        rowstart=0
        colend=m-1
        rowend=n-1
        while c<total:
            #row start, colstart->colend
            for i in range(colstart,colend+1):
                ans.append(matrix[rowstart][i])
                c=c+1
            rowstart=rowstart+1 
            if c==total:
                break  
            # colend, rowstart->colstart     
            for i in range(rowstart,rowend+1):
                ans.append(matrix[i][colend])
                c=c+1
            colend=colend-1 
            if c==total:
                break   
            #rowend , colend->colstart 
            for i in range(colend,colstart-1,-1):
                ans.append(matrix[rowend][i])
                c=c+1
            rowend=rowend-1 


            for i in range(rowend,rowstart-1,-1):
                ans.append(matrix[i][colstart])
                c=c+1
            colstart=colstart+1
             

        return ans



       