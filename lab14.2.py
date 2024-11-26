import numpy as np
import matplotlib.pyplot as plt

# Дані
x = np.array([2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
y = np.array([74.9, 75.3, 75.6, 75.9, 76.2, 76.5, 76.7, 77.0])  # Китай
z = np.array([68.3, 69.2, 70.3, 70.8, 70.9, 71.2, 71.2, 71.2])  # Україна

# Вибір країни користувачем
country = input("Введіть назву країни (China або Ukraine): ")

# Побудова стовпчастої діаграми
if country.lower() == 'china':
    plt.bar(x, y, color='yellow', label='China')
    plt.title('Life expectancy in China', fontsize=18)
elif country.lower() == 'ukraine':
    plt.bar(x, z, color='blue', label='Ukraine')
    plt.title('Life expectancy in Ukraine', fontsize=18)
else:
    print("Неправильна назва країни! Спробуйте ще раз.")
    exit()

plt.xlabel('Year', fontsize=14, color='purple')
plt.ylabel('Indicator', fontsize=14, color='purple')
plt.legend()
plt.grid(axis='y')
plt.show()

# Побудова лінійних графіків для обох країн
plt.plot(x, y, label='China', color='yellow', marker='o')
plt.plot(x, z, label='Ukraine', color='blue', marker='o')
plt.title('Life expectancy at birth, total', fontsize=18)
plt.xlabel('Year', fontsize=14, color='purple')
plt.ylabel('Indicator', fontsize=14, color='purple')
plt.legend()
plt.grid(True)
plt.show()
