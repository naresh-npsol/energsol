#!/bin/bash

# Create a temporary directory for downloads
mkdir -p temp_images
cd temp_images

# Download testimonial images
echo "Downloading testimonial images..."
curl -L -o manufacturing-plant.jpg "https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg"
curl -L -o industrial-facility.jpg "https://images.pexels.com/photos/2280549/pexels-photo-2280549.jpeg"
curl -L -o energy-plant.jpg "https://images.pexels.com/photos/2280545/pexels-photo-2280545.jpeg"

# Download metric icons
echo "Downloading metric icons..."
curl -L -o energy-efficiency-icon.png "https://cdn-icons-png.flaticon.com/512/2933/2933116.png"
curl -L -o cost-savings-icon.png "https://cdn-icons-png.flaticon.com/512/2933/2933116.png"
curl -L -o sustainability-icon.png "https://cdn-icons-png.flaticon.com/512/2933/2933116.png"

# Download background image
echo "Downloading background image..."
curl -L -o energy-background.jpg "https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg"

# Move all downloaded images to the images directory
mv *.jpg *.png ../images/

# Clean up
cd ..
rm -rf temp_images

echo "All images have been downloaded and moved to the images directory." 