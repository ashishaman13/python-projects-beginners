""" ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False """

ipt = input("Enter two words string :")

def animal_crackers (ipt):
    words = ipt.split()
    return words[0][0].lower == words[1][0].lower

result = animal_crackers("Lama Langer")
print(result)




# def animals_crackers():
#     ipt = input("Enter two words strings:")
#     words = ipt.split()
#     return words[0][0].lower() == words[1][0].lower()
#
# result = animals_crackers()
# print(result)












