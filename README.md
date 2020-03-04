# Hand-gesture-detection
A Deep Learning Project for hand gesture recognition.


Refer 'HandGestureRecognitionCNN.ipynb' for details on data, training and testing.

The data set is generated using the python script 'get_gestures.py'. It uses Opencv to capture gesture images from laptop webcam.

Usage:
```
  python get_gestures.py --save_path data --gesture_name one --number 200 --test_size 0.2
```

* save_path : represents the folder to save images in.
* gesture_name : represents the inner folder name and the name you want to give to the gesture
* number : number of images to capture
* test_size : percentage of images to label as test images (training images are labelled as 'TR' and testing images as 'TE', this extension is added to the file name)

## References
1. Sourav Johar, [Create a Rock Paper Scissors AI | Keras and OpenCV | Tutorial | Python](https://www.youtube.com/watch?v=0uSA3xyXlwM&feature=youtu.be)
