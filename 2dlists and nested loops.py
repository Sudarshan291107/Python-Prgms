# matrix=[
#     [1,2,3], #0th row 0,1,2
#     [4,5,6], #1th row 0,1,2
#     [7,8,9]  #2th row 0,1,2
# ]
# print(matrix[0][2])
# print(matrix[2][0])

team_list=[
    ["Virat","Dhoni","Rohit"],
    ["Sachin","Ganguly","Srinath"],
    ["Kapil","Sunil","Amarnath"]
]
# print(team_list[0][2])
# team_list[0][2]="Sameer"
# print(team_list)

for players in team_list: #to access entire list at a time
    print(players)
    for main in players:#to access one player at a time
        print(main)