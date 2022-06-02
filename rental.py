from datetime import date
from Pyro5.api import expose, behavior, serve, Daemon

@expose #This makes the rental class available remotely.
@behavior(instance_mode="single")#For all the method calls there will be only a single instance.
class rental(object):
    def __init__(self):
      #all these list Variable will store the information dictionary format
      self.user = []#[{'user_name': 'Conor Reilly', 'number': 123456},{'user_name': 'Mohammed Shaad', 'number': 21065793}]
      self.cars = []#[{'manufacturer_name': 'BMW', 'manufacturere_country': 'Germany'}]
      self.addcars= []#[{'manufacturer_name': 'BMW', 'car_model': '3 Series', 'available': True}] 
      self.rented = []#[{'user_name': 'Conor Reilly', 'car_model': '3 Series', 'year': 2019, 'month': 2, 'day': 4, 'available': True}]

    #Task-1.Add a user to the system/registering all the users.
    def add_user(self,user_name,user_number):
      #stroing the values in a dictionary format and then appending it to a list
      self.user.append({"user_name": user_name, "number": user_number})
      print("Stored the user with USER_NAME as",user_name,"and the USER_NUMBER as",user_number)

    #Task-2.Returning all the infromation about registered user.
    def return_users(self):
      return self.user

    #Task-3.Add a car manufacturer to the system
    def add_manufacturer(self, manufacturer_name, manufacturer_country):
      #stroing the values in a dictionary format and then appending it to a list
      self.cars.append({'manufacturer_name':manufacturer_name, 'manufacturer_country':manufacturer_country})
      print("Stored the MANUFACTURER_NAME as {0} and the MANUFACTURER_COUNTRY as {1}.".format(manufacturer_name, manufacturer_country))

    #Task-4.Returning all the infromation about manufacturer.
    def return_manufacturers(self):
      return self.cars

    #Task-5.Add a rental car to the system and stroing in a list of dictionary format. Making the newly added car available.
    def add_rental_car(self, manufacturer_name, car_model):
      #available=True  ==> The car is available. available=False ==> The car has been rented currently and is not availavle.
      self.addcars.append({'manufacturer_name':manufacturer_name,'car_model':car_model, 'available':True})
      print("Stored the MANUFACTURER_NAME as {0}, CAR_MODEL as {1}.".format(manufacturer_name, car_model))

    #Task-6.Return all the information of the car which are currently not rented.
    def return_cars_not_rented(self):
      availablecars=[]
      for i,value in enumerate(self.addcars):
        if value['available']==True:
          availablecars.append(value) 
      return availablecars

    #Task-7.Renting a car of a specific model to a specific user on a specific date.
    def rent_car(self, user_name, car_model, year, month, day):
      #check if the user is registered.
      for i in range(len(self.user)):
        if self.user[i]['user_name']==user_name :
          return 0
      #if the user is registered then only the user will be able to rent the car
      for i in range(len(self.addcars)):
        if self.addcars[i]['car_model'] == car_model and self.addcars[i]['available']==True :
          self.addcars[i]['available'] = False
          self.rented.append({'user_name':user_name,'car_model':car_model,'year':year,'month':month,'day':day,'available':False})
          print("Stored the information of the CAR_MODEL",car_model,"rented by USER_NAME", user_name,"on DATE:-",year,"/",month,"/",day)
          return 1
        return 0

    #Task-8.Return all the information relating to the set of cars currently rented.
    def return_cars_rented(self):    
      return self.rented 

    #Task-9.End the rental of a car 
    def end_rental(self, user_name, car_model, year, month, day):
      for i in range(len(self.rented)):
        #If the user_name and car_model matches and if the car is not available (the car is rented) then store the dates and change the available to True.
        if self.rented[i]['user_name']==user_name and self.rented[i]['car_model']==car_model and self.rented[i]['available']==False :
          self.rented[i]['year']=year
          self.rented[i]['month']=month
          self.rented[i]['day']=day
          self.rented[i]['available']=True
          #Also, change the available to True in the addcars.
          if self.addcars[i]['car_model']==car_model:
            self.addcars[i]['available']=True
         

    #Taske-10. Deleting from the system all the cars which are currently not rented and the rented cars should not be deleted.
    def delete_car(self,car_model):
      for i in range(len(self.addcars)):
        if self.addcars[i]['car_model']==car_model and self.addcars[i]['available']==True:
          del self.addcars[i]
    
    #Task-11. Delete from the system a user who have never rented a car.
    def delete_user(self, user_name):
      #If the user was found in the rented list that means that the user has previously rented the car and hence do nothing and return 0.
      for i in range(len(self.rented)):
        if self.rented[i]['user_name']==user_name :
          return 0 
      #But if we didn't find the user in the rented list then the user has never rented a car and we can now delete it and return 1.
      for i in range (len(self.user)):
        if self.user[i]['user_name']==user_name:
          del self.user[i]
          return 1
      return 0 

    #Task-12. Return all car models a user previously rented where the corresponding rental and return dates both lie between a specified start and end date inclusive.
    def user_rental_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day):
      user_rented=[]
      start_date = date(start_year,start_month,start_day)
      end_date = date(end_year,end_month,end_day)
      for i in range(len(self.rented)):
        if self.rented[i]['user_name']==user_name:
          #storing the dates to match so that it can be compared with the start and the end dates
          userdate=date(self.rented[i]['year'],self.rented[i]['month'],self.rented[i]['day'])
          # if the date is in between the start date and the end date then store it in the temporary
          if start_date<=userdate<=end_date:
            user_rented.append(self.rented[i])
      return user_rented  

daemon = Daemon() 
serve({rental: "example.rental"}, daemon=daemon, use_ns=True)


    
