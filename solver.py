
def solve(s):

    try:
        i = s.index(0)
    except ValueError:
        # No empty cell left: solution found
        return s

    c = [s[j] for j in range(81)
         if not ((i-j)%9 * (i//9^j//9) * (i//27^j//27 | (i%9//3^j%9//3)))]

    for v in range(1, 10):
        if v not in c:
            r = solve(s[:i]+[v]+s[i+1:])
            if r is not None:
                return r



class Sudoku(list):
    '''Sudokus with nicer IO'''

    def __init__(self, content):
        list.__init__(self, [int(i) for i in content.split()]
        if isinstance(content, str) else content)

    def __str__(self):
        return '\n'.join(
            ' '.join([(str(j) if j != 0 else '-')
                      for j in self[i * 9:(i + 1) * 9]]) for i in range(9))


# Usage
problem = Sudoku('''
0 0 3 1 6 0 0 0 0
5 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 4 7
0 0 7 0 1 5 4 0 8
0 0 8 0 7 0 2 0 0
2 0 5 6 4 0 3 0 0
4 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 3
0 0 0 0 8 6 5 0 0
''')


result = Sudoku(solve(problem))
result = str(result)
print(type(result))

print(result)
print('==== Problem ====\n{0}\n\n=== Solution ====\n{1}'.format(
         problem, result))

