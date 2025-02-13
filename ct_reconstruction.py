import numpy as np
from cil.framework import DataContainer
from cil.io import TIFFWriter, TIFFStackReader
from cil.processors import TransmissionAbsorptionConverter
from cil.plugins.astra import FBP

# Load X-ray projections
reader = TIFFStackReader(file_name='raw_x-ray_image_02.tif')
data = reader.read()

# Convert transmission data to absorption data
converter = TransmissionAbsorptionConverter()
absorption_data = converter(data)

# Set up geometry (modify as needed for your specific case)
angles = np.linspace(0, np.pi, data.shape[0])
geometry = parallel_beam_geometry(angles)

# Perform FBP reconstruction
fbp = FBP(absorption_data, geometry)
reconstruction = fbp()

# Save the reconstructed image
writer = TIFFWriter(data=reconstruction, file_name='reconstruction.tiff')
writer.write()
