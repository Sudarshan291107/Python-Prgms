# form_name={
#     "applicant_name":"Sudarshan",
#     "phone":9673907908,
#     "email":"4al21cs160@gmail.com",
#     "is_accepted":True
# }
# print(form_name)
# print(form_name["email"])
# print(form_name.get("email"))
# print(form_name.get("dateofbirth")) #since there is no element present for dateofbirth it returns object as none
# print(form_name.get("dateofbirth","Key does not exist")) #it returns default value that u give if element not there
#
# form_name["age"]=54 #to add another parameter
# print(form_name)
# form_name["email"]="samishere2907@gmail.com"#to update emailid
# print(form_name)

kan_dict={
    "there":"alli",
    "here":"illi",
    "one":1
}
# print(kan_dict)
# user_input=input("Enter English word to find kannada version: ")
# print(kan_dict.get(user_input))

user_input=input("Enter English word to find kannada version: ")
words=user_input.split("_")
print(words)
for everyword in words:
    print(kan_dict.get(everyword))