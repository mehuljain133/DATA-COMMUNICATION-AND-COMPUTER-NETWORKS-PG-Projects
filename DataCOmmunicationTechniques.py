# Unit-I Data Communication Techniques: Theoretical basis of data communication, analog and
# digital signals, time domain and frequency domain analysis, frequency spectrum and bandwidth,
# asynchronous and synchronous transmission, data encoding and modulation techniques, baseband and
# broadband transmission, pulse code modulation, baud rate and bitrate of a channel, multiplexingFDM & TDM, transmission medium, transmission errors – error detection techniques.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Constants
sampling_rate = 1000  # Sampling rate in Hz
duration = 1  # Signal duration in seconds
frequency = 50  # Frequency of the analog signal in Hz

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# 1. Analog Signal - Sine Wave
analog_signal = np.sin(2 * np.pi * frequency * t)

# 2. Digital Signal - Square Wave
digital_signal = signal.square(2 * np.pi * frequency * t)

# 3. Pulse Code Modulation (PCM) - Sampling the Analog Signal
pcm_signal = np.round(analog_signal)

# 4. Asynchronous Transmission Simulation (Start and Stop bits)
start_bit = np.zeros(int(sampling_rate * 0.1))  # 0.1 seconds Start bit
stop_bit = np.ones(int(sampling_rate * 0.1))  # 0.1 seconds Stop bit
data_bits = np.random.choice([0, 1], size=int(sampling_rate * duration))  # Data bits (0 or 1)
asynchronous_signal = np.concatenate([start_bit, data_bits, stop_bit])

# 5. Error Detection (Simple Parity Check)
def parity_check(data_bits):
    parity = np.sum(data_bits) % 2  # Even parity check
    return parity

# Simulate an error (flip a random bit)
error_position = np.random.randint(0, len(data_bits))
data_bits_with_error = data_bits.copy()
data_bits_with_error[error_position] = 1 - data_bits_with_error[error_position]  # Flip a bit

# Checking parity before and after error
original_parity = parity_check(data_bits)
error_parity = parity_check(data_bits_with_error)

# Plot the signals
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Plot Analog Signal (Sine Wave)
axs[0].plot(t, analog_signal)
axs[0].set_title("Analog Signal (Sine Wave)")
axs[0].set_xlabel("Time [s]")
axs[0].set_ylabel("Amplitude")

# Plot Digital Signal (Square Wave)
axs[1].plot(t, digital_signal)
axs[1].set_title("Digital Signal (Square Wave)")
axs[1].set_xlabel("Time [s]")
axs[1].set_ylabel("Amplitude")

# Plot PCM Signal (Digitized Analog Signal)
axs[2].stem(t, pcm_signal, use_line_collection=True)
axs[2].set_title("Pulse Code Modulation (PCM) Signal")
axs[2].set_xlabel("Time [s]")
axs[2].set_ylabel("Amplitude")

plt.tight_layout()
plt.show()

# Output parity check results
print(f"Original Data Parity: {original_parity}")
print(f"Error Data Parity: {error_parity}")

if original_parity != error_parity:
    print("Error detected in the transmission!")
else:
    print("No error detected in the transmission.")


