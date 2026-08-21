# Python Assignment 1
#1
string1 = "Hello "
name = input("Enter your Name: ")
result = string1 + name
print(result)

string3 = ", Welcome to Python Programming"
result = result + string3
print(result)

#2
print(result[0])

print(result[-1])

print(result[:5])

print(result[-11:])

print(result[::-1])

print(result.split(" ")[4])
#OR
python_word = "Python"
start = result.index(python_word)
print(result[start:start + len(python_word)])

#3
strM = "Python beginner tutorial"
print(strM.upper())

print(strM.lower())

print(strM.capitalize())

print(strM.count("t"))

print(strM.replace("Python", "Machine Learning"))


#4
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t_combine = t1 + t2
print(t_combine)

print(t_combine*3)

print(t_combine[2])

print(t_combine[:3])

print(t_combine[-3:])