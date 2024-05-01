def p_alignment(seq1, seq2, ):
    seq1, seq2 = list(seq1), list(seq2)
    scoreLocation, optimalAlignment = [], []
    score = 0
    

    # initialize matrix
    matrix = [[0 for i in range(len(seq2)+1)] for j in range(len(seq1)+1)] # +1 because alignment can start at index 0
    
    #calculate a score for each cell in the matrix
    for x in range(len(seq1)):
        for y in range(len(seq2)):
            
            #if match. note: values for match, mismatch, gaps are hardcoded
            if seq1[x] == seq2[y]:
                matrix[x+1][y+1] = max(matrix[x][y] + 5, matrix[x][y] - 1, matrix[x][y+1] - 4, matrix[x+1][y] - 4, 0)
            else:
                matrix[x+1][y+1] = max(matrix[x][y] - 1, matrix[x][y+1] - 4, matrix[x+1][y] - 4, 0)

    #print matrix for debugging
    # for row in range(len(matrix)):
    #     for each in matrix[row]:
    #         print(each, end=' ')
    #     print()

    #set score
    #spaghetti dinner, bon appetite.
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
                score = max(score, matrix[x][y])

    #set score location
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == score:
                scoreLocation.append((x, y))

    #traceback, that returns optimal alignment of both sequences
    while scoreLocation:
        x, y = scoreLocation.pop()
        alignment_x = []
        alignment_y = []
        while matrix[x][y] != 0:
            if seq1[x-1] == seq2[y-1]:
                alignment_x.append(seq1[x-1])
                alignment_y.append(seq2[y-1])
                x -= 1
                y -= 1
            else:
                #check for mismatch 
                if matrix[x][y] == matrix[x-1][y-1] - 1:
                    alignment_x.append(seq1[x-1])
                    alignment_y.append(seq2[y-1])
                    x -= 1
                    y -= 1
                #check for vertical gap in x
                elif matrix[x][y] == matrix[x-1][y] - 4:
                    alignment_x.append(seq1[x-1])
                    alignment_y.append('-')
                    x -= 1
                #check for hoziontal gap in y
                elif matrix[x][y] == matrix[x][y-1] - 4:
                    alignment_x.append('-')
                    alignment_y.append(seq2[y-1])
                    y -= 1
        optimalAlignment.append(alignment_x[::-1])
        optimalAlignment.append(alignment_y[::-1])



    print(f"Score: {score}")
    if len(optimalAlignment) == 0:
        print("No optimal alignment found")
        return
    print(f"Optimal X Alignment: {''.join(optimalAlignment[0]).upper()}")
    print(f"Optimal Y Alignment: {''.join(optimalAlignment[1]).upper()}")
    print()

    #print matrix y sequence
    # for i in range(len(seq2)):
    #     if i == 0:
    #         print('   ', end=' ')
    #     print(seq2[i], end=' ')
    # print()

    #print matrix with x sequence in the first column moved downward by 3
    # for x in range(len(matrix)):
    #     if x == 0:
    #         print(' ', end=' ')
    #     if x > 0:
    #         print(seq1[x-1], end=' ')
    #     for y in range(len(matrix[x])):
    #         print(matrix[x][y], end=' ')
    #     print()
    # print()

print("Optimal PairwiseLocal Alignment Tool\n")
#sequence1 = input("Enter the first sequence: ").upper()
#sequence2 = input("Enter the second sequence: ").upper()

#tests
p_alignment('AAT', 'CAAG')
p_alignment('SALTY', 'PLATE')
p_alignment('ISALIGNED', 'THISLINE')
p_alignment('ARE', 'REST')
p_alignment('A', 'A')
p_alignment('abcfghinopqrstuvwghijklmnopqrstuvwzyklmnopqrstuvwzyz', 'abcdejklmnopqyzabcdefghijklmnopqr')
p_alignment('l;kqwercmvn.a,jemfhoqialksdfnal.skdfjl292830lkajsd.v,zmxlaiula', 'a1234098sldkjnaweroqpiuhas;f;asdr')
p_alignment('a        a', 'a       a')




