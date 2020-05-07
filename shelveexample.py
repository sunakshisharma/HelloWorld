import shelve

with shelve.open('shelveexample') as fruit:
    fruit['Apple'] = "is good for health"
    fruit['orange'] = "is good for face"
    fruit['grape'] = "is good for eyes"
    fruit['lemon'] = "is a citrous fruit"
    # print(fruit['Apple'])
    # print(fruit['orange'])

#only key
    for key in fruit.keys():
     print(key)
    print("="  * 40)
#sorted keys
    for key in sorted(fruit.keys()):
        print(key)

# only value
    for value in fruit.values():
        print(value)
    print("="  * 40)
# sorted key with values
    for value in sorted(fruit.items()):
        print(value)
