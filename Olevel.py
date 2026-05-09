
# grid = [[0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 'X', 0],
#         [0, 0, 0, 0, 0]]


# moves = 10
# x = 0
# y = 0

# # print(grid[x][y])

# while moves > 0:
#     move = input("Left, right, up or down: ")
    
#     if move.lower() == 'left':
#         if y == 0:
#             print("Not possible to move left")
#         else:
#             y -= 1
#             moves -= 1
#     elif move.lower() == 'right':
#         if y == 4:
#             print("Not possible to move right")
#         else:
#             y += 1
#             moves -= 1
#     elif move.lower() == 'up':
#         if x == 0:
#             print("Not possible to move up")
#         else:
#             x -= 1
#             moves -= 1
#     elif move.lower() == 'down':
#         if x == 4:
#             print("Not possible to move down")
#         else:
#             x += 1
#             moves -= 1
#     else:
#         print("Please input a valid move")
        
#     if grid[x][y] == 'X':
#         print("You Won.")
#         break
    
#     print(f"Moves remaining: {moves}")
    
# if moves == 0:
#     print("You lost")
        


#  2025 

compete = 5
CompetitorName = []
CompetitorScore = []
for i in range(compete):
    name = input("Enter a name: ")
    CompetitorName.append(name)
    
for i in range(compete):
    score = []
    for j in range(5):
        x = int(input(f"Enter {j+1}th score for Competitor {i+1}"))
        score.append(x)
    CompetitorScore.append(score)
    
# print(CompetitorName)
# print(CompetitorScore)

Points = []

for i in range(compete):
    total = sum(CompetitorScore[i])
    Points.append(total)
    

medal_1 = []
highest = 0
for i in range(5):
    for j in range(compete):
        if CompetitorScore[j][i] > highest:
            highest = CompetitorScore[j][i]
            high_name = CompetitorName[j]
    print(f"Highest scorer in event {i} is {high_name}")


highest = 0
for i in range(compete):
    if Points[i] > highest:
        highest  = Points[i]
        high_name = CompetitorName[i]
        
print(f"Highest overall scorer is {high_name}")
