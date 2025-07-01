# def user_input():
#     ipt1 = input("Enter ur name:")
#
#     if ipt1.lower() == "shalu":
#         print("You are authorised")
#     else:
#         print("Access Denied!!")
#
# user_input()




def user_input():
    ipt1 = input("Enter ur name:")
    if ipt1.lower() == 'shalu':
        return "You are authorized"
    else:
        return "Access Denied"

result = user_input()
print(result)
