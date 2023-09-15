import matplotlib.pyplot as plt
        
years = [1950, 1960,1970,1980,1990,2000,2010]
co2 = [250,265,272,260,300,320,389]
temp = [14.1,15.5,16.3,18.1,17.3,19.1,20.2]

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
