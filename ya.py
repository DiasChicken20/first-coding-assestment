print("*************** Assestment number 1 ***************")
# odd number checking
def Ganjil(n):
    ganjil = []
    for i in range(n + 1):
        if i % 2 == 1:
            ganjil.append(i)
    print("Bilangan ganjil")
    return ganjil

# even number checking
def Genap(n):
    genap = []
    for i in range(n + 1):
        if i % 2 == 0:
            genap.append(i)
    print("Bilangan genap")
    return genap
print("==========================")

n = 100
print(Ganjil(n))
print(Genap(n)) 

print("************* Assestment number 2 ***************")

def search_number(list, number):
    total_find_number = 0
    index_find_number = []
    for index, value in enumerate(list):
        if value == number:
            total_find_number += 1
            index_find_number.append(index)
    return print(f"angka {number}  ditemukan sebanyak {total_find_number} yang indexnya berada di{index_find_number}")

list = [18, 15, 57, 54, 62, 16, 95, 28, 76, 83, 71, 84, 38, 57, 78, 96, 34, 
        66, 39, 50, 32, 25, 80, 29, 54, 28, 65, 15, 26, 8, 61, 66, 25, 38, 
        78, 99, 14, 49, 43, 2, 80, 65, 18, 30, 25, 65, 30, 66, 64, 81, 66, 
        5, 16, 44, 12, 24, 78, 89, 5, 96, 61, 7, 97, 59, 22, 8, 3, 19, 
        72, 33, 72, 22, 56, 53, 36, 83, 69, 22, 70, 6, 26, 40, 89, 97, 44, 
        40, 83, 18, 80, 89, 61, 91, 19, 61, 56, 16, 29, 11, 26, 92
        ]

result = search_number(list, 61)

print(result)

