# Slicing the tuple
elements= ("Mango",100,True,10.175,False,"Lotus","Sunflower","Orange","Sparrow")
print(elements)
# slicing of Elements
print(elements[4])  # False
print(elements[1:5])  # (100, True, 10.175, False)
print(elements[:5])  # ('Mango', 100, True, 10.175, False)
print(elements[3:])  # (10.175, False, 'Lotus', 'Sunflower', 'Orange', 'Sparrow')
print(elements[-7:-3]) # (True, 10.175, False, 'Lotus')
print(elements[-6:])  # (10.175, False, 'Lotus', 'Sunflower', 'Orange', 'Sparrow')
print(elements[:-4]) # ('Mango', 100, True, 10.175, False)
print(elements[::-1])  # ('Sparrow', 'Orange', 'Sunflower', 'Lotus', False, 10.175, True, 100, 'Mango')