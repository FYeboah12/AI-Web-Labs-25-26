# # def generate_children(state):
# #    '''your code goes here'''
# #    skip = False
# #    children = []
# #    blank = state.index("_")
# #    for ind in [blank + 1, blank - 1, blank + 3, blank - 3]:
# #         if ind >= 0 and ind < 9:
# #             if (blank == 2 and ind == 3) or (blank == 5 and ind == 6) or (blank == 3 and ind == 2) or (blank == 6 and ind == 5):
# #                 #print(blank == 2 and ind == 3,blank == 5 and ind == 6,blank == 3 and ind == 2,blank == 6 or ind == 5)
# #                 skip = True
# #             else:
# #                 children.append(swap(state,blank,ind))
# #    return children
# def generate_children(state):
#    children = []
#    blank = state.index("_")
#    row = blank // 3
#    col = blank % 3
#    for [r,c] in [[row, col + 1],[row, col - 1],[row + 1, col],[row - 1, col]]:
#       if 0 <= r < 3 and 0 <= c < 3:
#          ind = r * 3 + c
#          children.append(swap(state,blank,ind))
#    return children

# def swap(state,i,j):
#     sl = list(state)
#     a = sl[i]
#     sl[i] = sl[j]
#     sl[j] = a
#     return "".join(sl)

# print(swap("_42135678",1,0)) #4_2135678



# print("C" < "3")







# # print(0 <= 5 < 10)
# # print("Blank index 0:",generate_children("_42135678"))
# # print("Blank index 1:",generate_children("4_2135678"))
# # print("Blank index 2:",generate_children("42_135678"))
# # print("Blank index 3:",generate_children("421_35678"))
# # print("Blank index 4:",generate_children("4213_5678"))
# # print("Blank index 5:",generate_children("42135_678"))
# # print("Blank index 6:",generate_children("421356_78"))
# # print("Blank index 7:",generate_children("4213567_8"))
# # print("Blank index 8:",generate_children("42135678_"))
neighbors = {}
edges = [["3200014","3200044"],["3200013","3200014"],["3200014","3200050"]]   
for x in range(len(edges)):   
   edge_list = edges[x]
   #edgeCost[(edge_list[0], edge_list[1])] = calc_edge_cost(nodeLoc[edge_list[0]][0],nodeLoc[edge_list[0]][1],nodeLoc[edge_list[1]][0],nodeLoc[edge_list[1]][1])
   #edgeCost[(edge_list[1], edge_list[0])] = calc_edge_cost(nodeLoc[edge_list[1]][0],nodeLoc[edge_list[1]][1],nodeLoc[edge_list[0]][0],nodeLoc[edge_list[0]][1])
   if edge_list[0] not in neighbors:
      neighbors[edge_list[0]] = {edge_list[1]}
   if edge_list[1] not in neighbors:
      neighbors[edge_list[1]] = {edge_list[0]}
   else:
      neighbors[edge_list[0]].add(edge_list[1])
      neighbors[edge_list[1]].add(edge_list[0])
print(neighbors)