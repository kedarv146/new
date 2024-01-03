print("WELCOM")
print("DR Cafe")


def pizza():
    total1=0
    while True:
        print("\n1:Margherita Pizza                  250 \n2:Double Cheese Margherita Pizza    320 \n3:Veg Extravaganza Pizza            250 \n4:Cheese n Corn Pizza               200 \n5:Veggie Paradise Pizza             300 \n6:Paneer Makhani Pizza              350 \n7:Indi Tandoori Paneer Pizza        350 \n8:Chicken Golden Delight Pizza      420 \n9:Chicken Dominator Pizza           400 \n10:Pepper Barbeque Chicken Pizza    400 \n11:Indi Chicken Tikka Pizza         450 \n12:Chicken Pepperoni Pizza          420")
        p=int(input("select which pizza u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total1+=250*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total1+=320*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total1+=250*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total1+=200*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total1+=300*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total1+=350*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total1+=350*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total1+=420*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==9:
            q=int(input("Quantity: "))
            total1+=400*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==10:
            q=int(input("Quantity: "))
            total1+=400*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==11:
            q=int(input("Quantity: "))
            total1+=450*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        elif p==12:
            q=int(input("Quantity: "))
            total1+=420*q
            c=input("You want more pizza or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for pizza is: ",total1)
    return (total1)
    
    
def burger():
    total2=0
    while True:
        print("\n1:Chilli burger With Pepper Relish             200 \n2:Perfect Lamb Satay Burger                    200 \n3:Lamb and Tomato Stuffed Burger               250 \n4:Crunchy Chicken and Fish Burger              300 \n5:Chicken Feta Cheese Burger With Potato Salad 400 \n6:Lentil and Mushroom Burger                   400 \n7:Stuffed Bean Burger                          250 \n8:Lamb Burger with Radish Slaw                 220 \n9:Potato Corn Burger                           200 \n10:Supreme Veggie Burger                       230 \n11:Butter Chicken Twin Burgers                 400 \n12:Pizza Burger                                350 ")
        p=int(input("select which Burger u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total2+=200*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total2+=200*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total2+=250*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total2+300*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total2+=400*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total2+=400*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total2+=250*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total2+=220*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==9:
            q=int(input("Quantity: "))
            total2+=200*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==10:
            q=int(input("Quantity: "))
            total2+=230*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==11:
            q=int(input("Quantity: "))
            total2+=400*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        elif p==12:
            q=int(input("Quantity: "))
            total2+=350*q
            c=input("You want more burger or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for burger is: ",total2)
    return (total2)


def sandwiches():
    total3=0
    while True:
        print("\n1:Chilli Sandwich          50 \n2:Egg Sandwich             60 \n3:Seafood Sandwich         120 \n4:Roast Allu Sandwich      50 \n5:Grilled Cheese Sandwich  70 \n6:Chicken Sandwich         100 \n7:Nutella Sandwich         90 \n8:Grilled Chicken Sandwich 110")
        p=int(input("select which Burger u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total3+=50*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total3+=60*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total3+=120*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total3+=50*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total3+=70*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total3+=100*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total3+=90*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total3+=110*q
            c=input("You want more sandwiches or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for sandwiches is: ",total3)
    return (total3)
    

def drink():
    total4=0
    while True:
        print("\n1:Red bull              100 \n2:Sting                 100 \n3:Mountain Dew          100 \n4:Monster               100 \n5:Pepsi                 100 \n6:Coke                  100 \n7:Virgin Daiquiri       150 \n8:Virgin Mint Lemonade  190 \n9:Bellini               200 \n10:Pomegranate Spritzer 210 \n11:Apple Fizz           100 \n12:Cindrella            120 ")
        p=int(input("select which Burger u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total4+=100*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total4+=100*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total4+=100*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total4+=100*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total4+=100*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total4+=100*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total4+=150*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total4+=190*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==9:
            q=int(input("Quantity: "))
            total4+=200*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==10:
            q=int(input("Quantity: "))
            total4+=210*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==11:
            q=int(input("Quantity: "))
            total4+=100*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        elif p==12:
            q=int(input("Quantity: "))
            total4+=120*q
            c=input("You want more drink or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for drink is: ",total4)
    return (total4)
 
 
def coffee():
    total5=0
    while True:
        print("\n1:Espresso       150 \n2:Latte Latte    160 \n3:Black Coffee   120 \n4:Mocha          130 \n5:Americano      160 \n6:Cappuccino     200 \n7:Flat White     190 \n8:Long Black     150 \n9:Macchiato      140 \n10:Caramel       110 \n11:Normal Coffee 50")
        p=int(input("select which Burger u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total5+=150*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total5+=160*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total5+=120*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total5+=130*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total5+=160*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total5+=200*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total5+=190*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total5+=150*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==9:
            q=int(input("Quantity: "))
            total5+=140*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==10:
            q=int(input("Quantity: "))
            total5+=110*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        elif p==11:
            q=int(input("Quantity: "))
            total5+=50*q
            c=input("You want more coffee or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for coffee is: ",total5)
    return (total5)

    
def tea():
    total6=0
    while True:
        print("\n1:Normal Tea          20 \n2:Massala Tea         45 \n3:White Tea           60 \n4:Green Tea           50 \n5:Yellow Tea          60 \n6:Oolong Tea          65 \n7:Black Tea           40 \n8:Dark Tea            55 \n9:Herbal Tea          50 \n10:Kashmiri Kahwa Tea 60")
        p=int(input("select which Burger u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total6+=20*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total6+=45*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total6+=60*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total6+=50*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total6+=60*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total6+=65*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total6+=40*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total6+=55*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==9:
            q=int(input("Quantity: "))
            total6+=50*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        elif p==10:
            q=int(input("Quantity: "))
            total6+=60*q
            c=input("You want more tea or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for tea is: ",total6)
    return (total6)
    
    
def soup():
    total7=0
    while True:
        print("\n1:Italian Wedding Soup     200 \n2:Minestrone               190 \n3:Lentil Soup              250 \n4:Tomato Soup              150 \n5:New England Clam Chowder 500 \n6:French Onion Soup        200 \n7:Chicken Tortilla Soup    250 \n8:Butternut Squash Soup    220 \n9:Corn Chowder             200 \n10:Chicken and Rice Soup   300 \n11:Split Pea Soup          200")
        p=int(input("select which Burger u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total7+=200*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total7+=190*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total7+=250*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total7+=150*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total7+=500*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total7+=200*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total7+=250*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total7+=220*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==9:
            q=int(input("Quantity: "))
            total7+=200*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==10:
            q=int(input("Quantity: "))
            total7+=300*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        elif p==11:
            q=int(input("Quantity: "))
            total7+=200*q
            c=input("You want more soup or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for soup is: ",total7)
    return (total7)
    
    
def dessert():
    total8=0
    while True:
        print("\n1:Gulab Jamun              30 \n2:Jalebi                   10 \n3:Rasgulla                 20 \n4:Brownies                 120 \n5:Red Velvet Cake          80 \n6:Cup Cake                 50 \n7:Cheesecakes              80 \n8:Muffins                  100 \n9:Ice Cream(All Flavers)   100 \n10:Massala Sweet Paan      50")
        p=int(input("select which Burger u want: "))
        if p==1:
            q=int(input("Quantity: "))
            total8+=40*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==2:
            q=int(input("Quantity: "))
            total8+=10*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==3:
            q=int(input("Quantity: "))
            total8+=20*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==4:
            q=int(input("Quantity: "))
            total8+=120*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==5:
            q=int(input("Quantity: "))
            total8+=80*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==6:
            q=int(input("Quantity: "))
            total8+=50*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==7:
            q=int(input("Quantity: "))
            total8+=80*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==8:
            q=int(input("Quantity: "))
            total8+=100*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==9:
            q=int(input("Quantity: "))
            total8+=100*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        elif p==10:
            q=int(input("Quantity: "))
            total8+=50*q
            c=input("You want more dessert or continue...(y/n): ")
            if c=='n':
                break
        else:
            print("You select wrong election..... Please select again...")
            continue
    print("total balance for dessert is: ",total8)
    return (total8)



    
import random
ptotal=0
btotal=0
swtotal=0
dtotal=0
ttotal=0
ctotal=0
stotal=0
dtotal=0
while True:
    print("\nMENUE \n1:Pizza \n2:Burgers \n3:Sandwiches \n4:Drinks \n5:Coffee \n6:Tea \n7:Soup \n8:Dessert")
    x=int(input("Select your choise (If you don't want to order more then enter '0'): "))
    if x==1:
        ptotal+=pizza()
    elif x==2:
        btotal+=burger()
    elif x==3:
        swtotal+=sandwiches()
    elif x==4:
        dtotal+=drink()
    elif x==5:
        ctotal+=coffee()
    elif x==6:
        ttotal+=tea()
    elif x==7:
        stotal+=soup()
    elif x==8:
        dtotal+=dessert()
    elif x==0:
        total=ptotal+btotal+swtotal+dtotal+ctotal+ttotal+stotal+dtotal
        gst=(total*10)/100
        total_gst=total+gst
        print('\nPlay a game and win without GST bill.....')
        r=random.randint(0,5)
        g=int(input('Guess a number between 0 to 5 '))
        if r==g:
            print('Hurray!!! Your guess is match... Your Guess number is',g,'and random number is',r,'U win. Now u are paying without GST.:)')
            print("\nyour total balance is: ",total)
        else:
            print('Sorry! Your guess does not match... Your Guess number is',g,'and random number is',r,'Now u have to pay with GST..Better luck next time:)')
            print("\nyour total balance is: ",total_gst)
        f=int(input('\nPlease give us rating as ur experience (1 to 5): '))
        print('Thank you :) for giving us',f,'rating......')
        print('Pleas visit again....Have a good day:)')
        break
    else:
        print("You choose wrong....Please choose again.... ")
        continue