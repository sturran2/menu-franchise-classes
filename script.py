#create a menu class

class Menu():

  #5 parameters- self, name, items, start_time, end_time
  def __init__(self, name, items, start_time, end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
    
  #create representation method that says hours and the name of the menu
  def __repr__(self):
    return "This is the " + self.name + " menu. It is available from "+ str(self.start_time)+ " until " +str(self.end_time) + "."

  def calculate_bill(self, purchased_items):
    #method that returns the total price of purchase, consisting of all the items purchased. 
    self.purchased_items=purchased_items
    total=0
    for item in self.purchased_items:
      total+=self.items[item]
    return total
#define brunch item dictionary
brunch_items={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

#create brunch menu:
brunch=Menu("brunch",brunch_items,11,16)

#define items on early bird menu

early_bird_items={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

#create early_bird menu

early_bird=Menu("early bird", early_bird_items,15,18)

# create items for dinner

dinner_items={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

#create dinner menu

dinner=Menu("dinner",dinner_items, 17, 23)

# create items on kids menu

kids_items={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

#create kids_menu

kids=Menu("kids", kids_items, 11, 21)

#the below were used to test calculate_bill
#brunch_order=['pancakes', 'home fries', 'coffee']
#brunch_order2=['pancakes', 'home fries', 'coffee', 'pancakes']
#early_bird_order=['salumeria plate', 'mushroom ravioli (vegan)']
#print(early_bird.calculate_bill(early_bird_order))

#due to success of Basta Fazoolin' we want to create franchises. Create franchise class

class Franchise():
  def __init__(self, address,menus):
    self.address=address
    self.menus=menus
  
  def __repr__(self):
    return "this franchise is at "+self.address + "."

  #create available menus method that takes in time parameter and says what menu times are available.
  def available_menus(self,time):
    self.time=time
    avail_menus=[]
    for menu in self.menus:
      if self.time>=menu.start_time and self.time<=menu.end_time:
        avail_menus.append(menu)
    return avail_menus

      

#define list of all 4 menus
menus=[brunch, early_bird, dinner, kids]

flagship_store=Franchise("1232 West End Road", menus)
new_installment=Franchise("12 East Mulberry Street", menus)

#test franchise repr
#print(flagship_store)

#use these to test available menus method
#print(flagship_store.available_menus(14))
#print(new_installment.available_menus(17))

#define a business class
class Business():
  def __init__(self,name,franchises):
    self.name=name
    self.franchises=franchises
  
#create business
Basta_biz=Business("Basta Fazoolin' with my Heart", [flagship_store,new_installment])

#new business -take a arepa needs a menu
arepas_items={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu=Menu("Take a' Arepa",arepas_items,10,20)

#create a franchise
arepas_place=Franchise("189 Fitzgerald Avenue", [arepas_menu])

Arepa_biz=Business("Take a' Arepa",[arepas_place])