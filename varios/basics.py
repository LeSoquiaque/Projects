
numbers = [1, 2, 3]
numbers2 = [4, 5, 6]

matrizA = [[1, 2], [3, 4]]
matrizB = [[1, 0], [0, 1]]

result = zip(numbers2, numbers)

print(tuple(result))


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(b, a)

#use the tuple() function to display a readable version of the result:

print(tuple(x))


result = [[matrizA[i][j] + matrizB[i][j] for j in range(2)] for i in range(2)]

print(result)

