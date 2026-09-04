#Slicing of list
list=["Mango",100,True,10.175,False,"Lotus","Sunflower","Orange","Sparrow"]
print(list)
print(list[1])  # 100
print(list[6])  # Sunflower
print(list[2:5])  # [True, 10.175, False]
print(list[:5])  # ['Mango', 100, True, 10.175, False]
print(list[3:])  # [10.175, False, 'Lotus', 'Sunflower', 'Orange', 'Sparrow']
print(list[-3:-1])  # ['Sunflower', 'Orange']
print(list[-3:]) # ['Sunflower', 'Orange', 'Sparrow']
print(list[::-1]) # ['Sparrow', 'Orange', 'Sunflower', 'Lotus', False, 10.175, True, 100, 'Mango']
print(list[::-2]) # ['Sparrow', 'Sunflower', False, True, 'Mango']
