# ocean_optics_Flame-T

This code is to extract the spectrum of light source from Flame-T (ocean-optics).


# Install UDEV Rules for Flame-T
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="2457", MODE="0666"' | sudo tee /etc/udev/rules.d/ocean_optics_flame_T.rules
sudo udevadm control --reload-rules && sudo udevadm trigger

## Install Libraries

pip install seabreeze[pyseabreeze]

-Reference: https://github.com/ap--/python-seabreeze
