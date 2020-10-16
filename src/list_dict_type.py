x = ["hello", 4, 3, 5, 6, 8]
# print(x, type(x[:]))
y = x[-1::-1]
# print(y)


def foo(lst):
    x = 0
    for num in lst:
        # type(x) ==> type
        # if type(num) == str:
        #     continue
        if type(num) == int or type(num) == float:
            x += num
    return x

# print(foo([0,1,2,3,4,5]))
# print(foo(x))


dct = {
    "Raizel": {
        "address":{
            "house num": 214,
            "street": "Elmwood Ave",
            "city": "Glen Rock",
            "state": "NJ",
            "country": "USA"
        },
        "age": 27,
        "hobbies": [
            "losing in mario kart", 
            "reading", 
            "coding", 
            "being a boss ass bitch"
            ]
    },
    "Marc": {
        "address":{
            "house num": 214,
            "street": "Elmwood Ave",
            "city": "Glen Rock",
            "state": "NJ",
            "country": "USA"
        },
        "age": 22,
        "hobbies": [
            "beating sisters in mario kart", 
            "coding", 
            "being a handsome devil"
            ]
    }
}

# people ==> dictionary
# people["Raizel"] ==> dictionary
# people["Raizel"]["age"] ==> int




def getAges(people):
    # type(people) ==> dictionary
    result = {}
    for person in people:
        print(person + ":")
        print(" ",people[person]["age"])
        result[person] = people[person]["age"]
    
    return result


print(getAges(dct))









# families = {
#     "Fitter": df_fitter,
#     "Bernstein": df_bernstein
# }

# families["Benstein"][families["Bernstein"]["names"]]
