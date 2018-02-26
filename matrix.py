import math


a = [[1,2],
     [3,4]]
b = [[5,6,10],
     [7,8,11]]
'''
c = [[19,22],
     [43,50]]
'''

def print_matrix( matrix ):
	p = "\n"
   	for rows in matrix:
   		for cols in rows:
   			p+=str(cols)
   			p+=" "
   		p+="\n"
   	print p

def ident( matrix ):
    
  index = 0
  index2 = 0

  targX = 0
  targY = 0

  for each in matrix:
    for bit in each:
      if (index==targX and index2 == targY):
        matrix[index][index2] = 1
      else:
        matrix[index][index2] = 0
      index2+=1
    targX +=1
    targY +=1
    index+=1
    index2=0


#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
  row_m1 = len(m1)
  col_m1 = len(m1[0])
  row_m2 = len(m2)
  col_m2 = len(m2[0])

  retMatrix = new_matrix(col_m2,row_m1)

  print_matrix(retMatrix)

  for a in range(row_m1):
    for b in range(col_m2):
      for c in range(row_m2):
        retMatrix[a][b] += (m1[a][c] * m2[c][b])
  return retMatrix




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m


#print_matrix(matrix_mult(a,b))

#indent
'''
print_matrix(a)
ident(a)
print_matrix(a)
'''