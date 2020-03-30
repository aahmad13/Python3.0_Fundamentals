#Getting Ready for Physics Class Project

#Given Variables:
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
  
  #Fundamentals of Temperature
def f_to_c(f_temp):
  c_temp=(f_temp-32)*(5/9)
  return c_temp
f100_in_celsius=f_to_c(100)
print("Turn up the Temperature from 100F to C = " + str(round(f100_in_celsius,2))+"°")
def c_to_f(c_temp):
  f_temp=c_temp*(9/5)+32
  return f_temp
c0_in_fahrenheit= c_to_f(0)
print("Turn up the Temperature from 0C to F = " + str(round(f100_in_celsius,2))+"°")
  
  #Fundamentals of Force
def get_force(mass,acceleration):
  return mass*acceleration
round(get_force(train_mass,train_acceleration))
print("The GE train supplies "+str(get_force(train_mass,train_acceleration))+" Newtons of force.")
c=3*10**8
def get_energy(mass,c):
  return mass*c**2
bomb_energy=get_energy(bomb_mass,c)
print('A 1kg bomb supplies '+str(bomb_energy)+' Joules.')

  #Do the Work
def get_work(mass,acceleration,distance):
  force= get_force(mass,acceleration)
  return force*distance
train_work=get_work(train_mass,train_acceleration, train_distance)
print("The GE train does "+ str(train_work)+ " Joules of work over "+ str(train_distance) + " meters")
  
  