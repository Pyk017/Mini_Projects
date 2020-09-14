import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))

# solve2("FPFT + OMLBF = JGTKML")
# solve2("CNNTF + NFCI = HICNF")
# solve2("HOW + MUCH = POWER")
# solve2('MAC + MAAR = JOCKO')
# solve2('SEND + MORE = MONEY')
# solve2("FHMTT + HMIVT = VIJKLH")
solve2(input())




#     def isCryptSolution(crypt, solution):
#         newsol = list(zip(*reversed(solution)))
#         newstring1 = ''
#         total = 0
#         for word in range(len(crypt)-1):
#             subtotal, sol_total = 0, 0
#             newstring = ''
#             for char in crypt[word]:
#                 idx = newsol[0].index(char)
#                 newstring = newstring + newsol[1][idx]
#                 subtotal = int(newstring)
#                 # if newstring[0] == '0':
#                 #     return False
#             total = total + subtotal
#         for char1 in crypt[-1]:
#             nidx = newsol[0].index(char1)
#             newstring1 = newstring1 + newsol[1][nidx]
#             sol_total = int(newstring1)
#         if total == sol_total and newstring[0] != '0':
#             return True
#         elif total == 0 and newstring[0] == '0' and len(newstring) == 1:
#             return True
#         else:
#             return False

# crypt = ["SEND", "MORE", "MONEY"]
# solution = [['O', '0'],
#             ['M', '1'],
#             ['Y', '2'],
#             ['E', '5'],
#             ['N', '6'],
#             ['D', '7'],
#             ['R', '8'],
#             ['S', '9']]

# isCryptSolution(crypt, solution)