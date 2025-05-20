#my_list = ["1", "2", "3", "4"]

my_list = list(range (1,5))
print(my_list)
my_list = list(map(str,range(1,5)))

#versiunea 2
my_list = list(map(lambda x:str(x), range(1,50)))
print(my_list)

#versiunea 3 list comprehension

my_list = [str(i) for i in range(1,50)]
my_list