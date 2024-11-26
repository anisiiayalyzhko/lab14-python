import matplotlib.pyplot as plt
import numpy as np

# Визначаємо значення x
x = np.linspace(1, 10, 500)  # Збільшуємо значення для більш гладкого зображення графіка

# Записуємо функцію Y(x) = 5*sin(x)*cos(x^2 + 1/x)^2
y = 5 * np.sin(x) * np.cos(x**2 + 1/x)**2

# Побудуємо графік
plt.plot(x, y, label=r'$Y(x) = 5 \sin(x) \cos^2(x^2 + 1/x)$', color="purple", linewidth=2)

# Додаємо назви осей і графіка
plt.title('Graph of the function $Y(x)$', fontsize=16)
plt.xlabel('x', fontsize=14, color='green')
plt.ylabel('Y(x)', fontsize=14, color='green')

# Додаємо легенду і сітку
plt.legend()
plt.grid(True)

# Рядок для виведення графіка користувачу
plt.show()
