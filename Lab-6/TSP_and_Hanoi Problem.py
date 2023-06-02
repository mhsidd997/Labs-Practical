#++++++++++++++++++++++++ TSP Problem ++++++++++++++++++++++++

# V = int(input('Enter the number of nodes between 2 - 5: '))  
# tsp_value = []
 
# def tsp(graph, v, currPos, n, count, cost):
#     if (count == n and graph[currPos][0]):
#         tsp_value.append(cost + graph[currPos][0])
#         return
    
#     for i in range(n):
#         if (v[i] == False and graph[currPos][i]):
             
#             v[i] = True
#             tsp(graph, v, i, n, count + 1,
#                 cost + graph[currPos][i])
             
#             v[i] = False
            
# if __name__ == '__main__':
#     graph= [[ 0, 10, 15, 20 , 25 ],
#             [ 10, 0, 35, 25, 20 ],
#             [ 15, 32, 0, 30, 25 ],
#             [ 20, 25, 30, 0, 15 ],
#             [ 23, 41, 56, 12, 20]]
 
#     v = [False for i in range(V)]
     
#     tsp(graph, v, 0, V, 1, 0)
 
#     print(min(tsp_value))

#++++++++++++++++++++++++ Hanoi Problem ++++++++++++++++++++++++

def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move Disk 1 from Rod {} to Rod {}.'.format(source, target))  
        return  

    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move Disk {} from Rod {} to Rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
  
disks = int(input('Enter the number of Disks: '))  

tower_of_hanoi(disks, 'A', 'B', 'C')