# -*- coding: utf-8 -*-
"""AttentionIsAllYouNeed_PositionalEncoding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ox--QvgInxKPc1909OOjJ_VS6A9s9GLy
"""

I import numpy as np
import matplotlib.pyplot as plt

# Function for positional encoding
def get_positional_encoding(pos, d_model):
    PE = np.zeros((pos, d_model))
    for p in range(pos):
        for i in range(0, d_model, 2):  # Small dimensions (2-4)
            PE[p, i] = np.sin(p / (10000 ** (2 * i / d_model)))
            if i + 1 < d_model:
                PE[p, i + 1] = np.cos(p / (10000 ** (2 * i / d_model)))
    return PE

# Test with small values of i (small dimensions)
pos = 20  # Position count, you can change this
d_model = 4  # Try small dimension sizes, e.g., 2, 4, etc.
PE = get_positional_encoding(pos, d_model)

# Plot the positional encodings
plt.figure(figsize=(10, 6))
plt.plot(np.arange(pos), PE[:, 0], label="Dimension 0 (sin)")
plt.plot(np.arange(pos), PE[:, 1], label="Dimension 1 (cos)")
plt.plot(np.arange(pos), PE[:, 2], label="Dimension 2 (sin)")
plt.plot(np.arange(pos), PE[:, 3], label="Dimension 3 (cos)")
plt.legend()
plt.xlabel("Position")
plt.ylabel("Positional Encoding Value")
plt.title(f"Positional Encoding for d_model = {d_model}")
plt.show()