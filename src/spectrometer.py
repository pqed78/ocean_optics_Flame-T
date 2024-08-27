import matplotlib.pyplot as plt
import time

# # explicitly request cseabreeze (default)
#  import seabreeze
#  seabreeze.use('cseabreeze')
#  from seabreeze.spectrometers import list_devices, Spectrometer

# explicitly request pyseabreeze
import seabreeze
seabreeze.use('pyseabreeze')
from seabreeze.spectrometers import list_devices, Spectrometer


# open a spectrometer
# ===================

# # option 1
# from seabreeze.spectrometers import Spectrometer
# spec = Spectrometer.from_first_available()
# print(spec)
# <Spectrometer USB2000PLUS:USB2+F01234>

# option 2
# from seabreeze.spectrometers import Spectrometer, list_devices
# devices = list_devices()
# print(devices)
# # # [<SeaBreezeDevice USB2000PLUS:USB2+F01234>, <SeaBreezeDevice SPARK:00001>]
# spec = Spectrometer(devices[0])
# print(spec)
# # <Spectrometer SPARK:00001>

# # option 3
# from seabreeze.spectrometers import Spectrometer
# spec = Spectrometer.from_serial_number("F01234")
# spec
# # <Spectrometer USB2000PLUS:USB2+F01234>

spec = Spectrometer.from_serial_number("FLMT02893")
spec.integration_time_micros(100000)
wavelengths=spec.wavelengths()
intensities=spec.intensities()

# enable interactive mode
plt.ion()

figure, ax = plt.subplots(figsize=(10,8))
line,=ax.plot(wavelengths, intensities, color='red', alpha=0.8, linewidth=2)
plt.title("Spectrum of light source")
plt.xlabel("Wavelength")
plt.ylabel("Intensity (arb. unit)")



while True:
    # creating new intensity values
    intensities=spec.intensities()
    # updating data values
    line.set_ydata(intensities)

    # drawing updated values
    figure.canvas.draw()

    # This will run the GUI event
    # loop until all UI events
    # currently waiting have been processed
    figure.canvas.flush_events()
    time.sleep(0.1)