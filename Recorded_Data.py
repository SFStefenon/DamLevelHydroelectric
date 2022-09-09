import numpy as np
import matplotlib.pyplot as plt

# Original Data
Y0 = [20.46, 20.61, 20.75, 20.9, 21.02, 21.14, 21.29, 21.43, 21.58, 21.73, 21.88, 21.97, 22.12, 22.27, 22.36, 22.45, 22.54, 22.63, 22.75, 22.87, 22.96, 23.04, 23.13, 23.22, 23.34, 23.43, 23.52, 23.61, 23.7, 23.8, 23.89, 23.98, 24.07, 24.16, 24.22, 24.28, 24.34, 24.4, 24.46, 24.52, 24.61, 24.7, 24.82, 24.91, 24.97, 25.03, 25.09, 25.15, 25.21, 25.27, 25.33, 25.4, 25.46, 25.52, 25.58, 25.64, 25.7, 25.76, 25.82, 25.85, 25.85, 25.88, 25.94, 26.00, 26.06, 26.12, 26.19, 26.25, 26.28, 26.31, 26.34, 26.37, 26.4, 26.46, 26.49, 26.52, 26.58, 26.61, 26.64, 26.67, 26.7, 26.73, 26.76, 26.8, 26.83, 26.86, 26.89, 26.92, 26.95, 26.98, 27.01, 27.04, 27.1, 27.16, 27.19, 27.22, 27.25, 27.32, 27.35, 27.38, 27.41, 27.44, 27.47, 27.5, 27.53, 27.56, 27.59, 27.62, 27.68, 27.71, 27.74, 27.74, 27.78, 27.81, 27.84, 27.87, 27.9, 27.93, 27.96, 27.99, 28.02, 28.05, 28.08, 28.11, 28.11, 28.14, 28.21, 28.3, 28.42, 28.61, 28.76, 28.91, 29.07, 29.19, 29.32, 29.47, 29.59, 29.72, 29.84, 29.97, 30.09, 30.22, 30.34, 30.46, 30.59, 30.71, 30.84, 30.96, 31.09, 31.21, 31.31, 31.4, 31.49, 31.62, 31.81, 31.99, 32.31, 32.65, 33.06, 33.47, 33.85, 34.23, 34.71, 35.22, 35.63, 36.18, 36.66, 37.14, 37.69, 38.24, 38.82, 39.4, 40.05, 40.8, 41.56, 42.41, 43.14, 43.93, 44.87, 45.63, 46.27, 46.97, 47.65, 48.36, 49.00, 49.58, 50.16, 50.74, 51.32, 51.9, 52.49, 53.01, 53.53, 53.98, 54.46, 54.91, 55.3, 55.72, 56.03, 56.45, 56.77, 57.12, 57.36, 57.64, 57.89, 58.17, 58.42, 58.6, 58.81, 59.05, 59.23, 59.44, 59.59, 59.8, 59.98, 60.15, 60.3, 60.51, 60.72, 60.9, 61.08, 61.22, 61.37, 61.51, 61.62, 61.69, 61.8, 61.9, 62.01, 62.08, 62.15, 62.22, 62.33, 62.44, 62.55, 62.66, 62.73, 62.8, 62.83, 62.87, 62.94, 63.09, 63.19, 63.3, 63.48, 63.59, 63.7, 63.81, 63.91, 64.02, 64.13, 64.28, 64.42, 64.49, 64.57, 64.64, 64.71, 64.75, 64.82, 64.93, 65.04, 65.18, 65.33, 65.43, 65.54, 65.69, 65.8, 65.91, 66.05, 66.2, 66.34, 66.49, 66.63, 66.78, 66.93, 67.11, 67.29, 67.47, 67.73, 68.02, 68.46, 68.87, 69.27, 69.6, 69.97, 70.34, 70.71, 71.08, 71.38, 71.68, 71.97, 72.23, 72.49, 72.76, 73.02, 73.28, 73.43, 73.61, 73.84, 74.03, 74.25, 74.48, 74.7, 74.89, 75.08, 75.27, 75.45, 75.57, 75.68, 75.79, 75.91, 75.98, 76.09, 76.25, 76.4, 76.55, 76.66, 76.77, 76.85, 76.93, 77.00, 77.08, 77.15, 77.23, 77.3, 77.38, 77.46, 77.53, 77.61, 77.68, 77.76, 77.84, 77.91, 78.06, 78.14, 78.22, 78.25, 78.29, 78.33, 78.37, 78.37, 78.41, 78.41, 78.44, 78.48, 78.52, 78.56, 78.6, 78.6, 78.63, 78.63, 78.67, 78.67, 78.67, 78.71, 78.75, 78.75, 78.79, 78.82, 78.86, 78.9, 78.94, 78.94, 78.94, 78.94, 78.94, 78.94, 78.94, 78.94, 78.94, 78.98, 78.98, 78.98, 78.98, 78.98, 78.98, 78.98, 78.98, 78.98, 78.98, 79.01, 79.05, 79.09, 79.13, 79.17, 79.21, 79.28, 79.32, 79.4, 79.47, 79.63, 79.74, 79.85, 79.97, 80.08, 80.2, 80.28, 80.35, 80.47, 80.58, 80.7, 80.77, 80.89, 81.00, 81.12, 81.2, 81.27, 81.35, 81.43, 81.5, 81.62, 81.77, 81.93, 82.08, 82.23, 82.35, 82.43, 82.47, 82.54, 82.58, 82.66, 82.7, 82.77, 82.81, 82.85, 82.93, 82.97, 83.01, 83.08, 83.12, 83.16, 83.2, 83.28, 83.35, 83.47, 83.63, 83.7, 83.78, 83.82, 83.86, 83.94, 84.01, 84.09, 84.17, 84.28, 84.36, 84.48, 84.6, 84.71, 84.83, 84.87, 84.91, 84.98, 85.06, 85.14, 85.22, 85.3, 85.37, 85.45, 85.53, 85.61, 85.68, 85.76, 85.84, 85.92, 85.96, 86.00, 86.07, 86.11, 86.15, 86.19, 86.23, 86.27, 86.27, 86.27, 86.27, 86.27, 86.27, 86.27, 86.27, 86.27, 86.27, 86.23, 86.23, 86.23, 86.23, 86.23, 86.23, 86.23, 86.19, 86.15, 86.11, 86.07, 86.04, 86.00, 85.96, 85.92, 85.92, 85.92, 85.92, 85.92, 85.92, 85.88, 85.88, 85.88, 85.84, 85.84, 85.84, 85.84, 85.8, 85.8, 85.8, 85.76, 85.72, 85.68, 85.65, 85.61, 85.57, 85.53, 85.49, 85.45, 85.41, 85.37, 85.33, 85.3, 85.3, 85.3, 85.26, 85.26, 85.22, 85.22, 85.18, 85.18, 85.14, 85.14, 85.1, 85.1, 85.06, 85.06, 85.02, 85.02, 84.98, 84.98, 84.94, 84.94, 84.94, 84.91, 84.91, 84.87, 84.87, 84.83, 84.79, 84.75, 84.71, 84.67, 84.63, 84.6, 84.56, 84.52, 84.48, 84.44, 84.4, 84.36, 84.32, 84.28, 84.25, 84.25, 84.25, 84.21, 84.21, 84.21, 84.17, 84.17, 84.13, 84.13, 84.09, 84.05, 84.05, 84.01, 83.97, 83.94, 83.9, 83.86, 83.82, 83.74, 83.7, 83.66, 83.59, 83.51, 83.43, 83.39, 83.35, 83.32, 83.28, 83.24, 83.24, 83.2, 83.2, 83.2, 83.2, 83.16, 83.16, 83.16, 83.12, 83.12, 83.12, 83.08, 83.08, 83.12, 83.12, 83.12, 83.16, 83.16, 83.2, 83.2, 83.2, 83.2, 83.16, 83.12, 83.08, 83.05, 82.97, 82.93, 82.89, 82.85, 82.81, 82.77, 82.74, 82.7, 82.66, 82.62, 82.58, 82.54, 82.5, 82.47, 82.43, 82.39, 82.35, 82.31, 82.27, 82.23, 82.2, 82.16, 82.12, 82.08, 82.04, 82.00, 81.97, 81.93, 81.89, 81.85, 81.81, 81.77, 81.73, 81.7, 81.66, 81.58, 81.54, 81.5, 81.46, 81.43, 81.39, 81.39, 81.35, 81.35, 81.35, 81.31, 81.31, 81.27, 81.27, 81.23, 81.2, 81.16, 81.16, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.12, 81.08, 81.08, 81.08, 81.04, 81.00, 81.00, 81.00, 80.97, 80.97, 80.97, 80.93, 80.93, 80.93, 80.89, 80.89, 80.89, 80.85, 80.85, 80.81, 80.81, 80.77, 80.77, 80.74, 80.74, 80.74, 80.7, 80.7, 80.7, 80.66, 80.66, 80.62, 80.62, 80.58, 80.58, 80.54, 80.51, 80.51, 80.47, 80.43, 80.39, 80.35, 80.31, 80.28, 80.24, 80.2]  
length = len(Y0)

# Include Noice
noice = 4
t = np.linspace(0, 50*np.pi, length)
x_1 = Y0 - 0.0005*(t**2) + np.random.normal(0, noice, length)
x_2 = Y0 + 0.05*t + np.random.normal(0, noice, length)

# Plot Figure
plt.figure(figsize=(8, 4))
plt.plot(range(len(x_1)), Y0, 'k', label='Original')
plt.plot(range(len(x_1)), x_1, 'r', label='$x_1$')
plt.plot(range(len(x_2)), x_2, 'b', label='$x_2$')
plt.legend(loc='upper center', bbox_to_anchor=(0.9, 0.27), fancybox=True, shadow=False, ncol=1)
plt.axis([0, len(x_1), 0, 105])
plt.xlabel('Time (h)')
plt.ylabel('Reservoir Level (%)')
plt.grid()
# plt.savefig('1.pdf')
plt.show()