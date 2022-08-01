import random

category = ['Hygiene', 'Health', 'Staples',  'Sports', 'Fashion']


class Product():

    def __init__(self, c, capacity = 10):
        self.category = category[c]
        self.product = {}
        self.capacity = capacity
       

    def prodName(self):
        while True:
            prname = input('Enter product name:')
            if len(prname) >= 3 and prname.isalpha():
                return prname
            else:
                print('Should contain only characters and atleast be 3 characters')


    def getPrice(self):
        ch = input('1. Price without tax 2. MRP. your choice:')
        if ch == "1":
            bp = int(input('Enter base price:'))
            tax = int(input('Enter tax %:'))
            MRP = bp + (bp*tax/100)
        elif ch == "2":
            MRP = int(input('Enter MRP:'))
            tax = int(input('Enter tax %:'))
            bp = MRP*100/(tax+100)
        return round(bp, 2), round(tax, 2), round(MRP, 2)

    def discount(self, MRP):
        ch = input('Discount as 1. Rate or 2. Amount. Select:')
        if ch == "1":
            dr = int(input('Enter discount rate:'))
            discountPrice = MRP - (MRP*dr/100)
            return str(dr)+'%', round(discountPrice, 2)
        elif ch == "2":
            da = int(input('Enter discount amount:'))
            discountPrice = MRP - da
            return str(da), round(discountPrice, 2)
    
    def code(self, name, c, p):
       
        
    def addProduct(self):
        name = self.prodName()
        bp, tax, mrp = self.getPrice()
        d, dp = self.discount(mrp)
        global p
        product = [name, self.category, bp, tax, mrp, d, dp]
        pcode = self.code(name, self.category, p)
        p.update({pcode : product}) 
        print('Product added\n')
    
    
while True:
    print("1. Add products 2. List products 3. Exit")
    ch = input("Enter you choice:")
    if ch == '1':    
        print("\n1.Hygiene 2.Health 3.Staples 4.Sports 5.Fashion")
        c = int(input('Enter product category:'))-1
        prod = Product(c)
        prod.addProduct()
    
    