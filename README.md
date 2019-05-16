# cluster_GUI
A simple Application to cluster and visualize images using the k-Means-Clustering (Python)

**REQUIREMENTS**
- PyQt5
- Python 2.7.11 / 3.x
- OpenCV for Python
- Execlusively tried on Ubuntu 16.04 (should also work on Windows however)

**BUILD**
- FIRST, CHANGE SAVE LOCATION (LINE 22)
- make sure you have the python.jpg image in the same folder as the cluster.py file
- Simply compile via console (python cluster.py)

**HOW TO USE**
- If running, browse your system via file browser on the right and upload any image you want. Click on the image you want to upload and press the UPLOAD button. Image will appear at the center of the application. **If it is scaled incorrectly,** hit the RESET button once. Now you can play with the params of the algorithm on the left. Hit UPDATE to apply changes.
- Always press RESET after each cluster! (minor important bug, does not effect functionality)
- SAVE button saves the current shown image to your save location. Name includes params of the current state.

**Recent Update**: Fixed bug that you could not cluster images that were put on spot via file browser. Still some bugs but works pretty well now.

**Update 28.03.2019**: You can now upload images via filebrowser using "UPLOAD" button. However, you cannot cluster or save afterwards. Will be fixed in near future.


