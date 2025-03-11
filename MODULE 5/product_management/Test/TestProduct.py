import random

products=[]
n=1000
for i in range (1,n+1):
    cateid=random.randrange(1,13)
    price=random.randrange(100,500)
    quantity=random.randrange(1,20)
    products.append(product(f'p{i}',f'Product {i}',price,quantity))
print('List of Products:')
for p in products:
    print(p)

filename=
jff=JsonFileFactory()
jff.write_data(product,filname)
