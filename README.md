# Face_ID
A simple implementation of OpenCV for face recognition


The main library used in this project is the OpenCV library.
The system has been made as simple as possible to be used.
No special GUI is used only a simple CLI.

In order for the face_identification.py to be used the sampler and.py
and trainer.py must be used in order to create the trainer.yml file
that will be used to identify the people's faces.

Please note that special directories must be used in order to use face_identification.py
these are the dataset and trainer directories. Which can also be created by using the
package_creator.py. Due to the nature of the system all the information is saved persistently
and is not hardcoded in the Python Scripts, except from the names created in order to make
face_identification.py work. haarscade_frontalface_default.xml is used in order to detect faces
and it was taken from the OpenCV repository in GitHub.
