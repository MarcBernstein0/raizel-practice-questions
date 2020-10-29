x = [1, 5, 4, 3, 0, 10, 7, 10, 9, 9, 8, 2, 9, 12, 6]
# basic nested loop example
def isThereARepeat(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return (True, lst[i])
    return (False, None)

# print(isThereARepeat(x))

dct = {
    "Marc": {
        "sex": "male",
        "age": 22,
        "favorite color": "Red"
    },
    "Raizel": {
        "sex": "female",
        "age": 27,
        "favorite color": "Blue"
    }
}

# dct["Marc"] =>  {"sex": "male", "age": 22, "favorite color": "Red"}
# dct["Marc"]["Favorite color"] => {"sex": "male", "age": 22, "favorite color": "Red"}["Favorite Color"] => "Red"


for name in dct:
    print(name, dct[name]["favorite color"])

# for name in dct:
#     print(list(dct[name].values()))


x = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8]
    ]

for i in range(len(x)):
    for j in range(len(x[0])):
        print("Value:", x[i][j], "Position:", i, j)
