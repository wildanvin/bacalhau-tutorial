# Bacalhau demo with OpenCV

This is a tutorial on how to use Bacalhau with OpenCV. Read the full tutorial here:

> clone/fork:

```bash
git clone https://github.com/wildanvin/bacalhau-tutorial.git
```

## Install numpy:

- Install: `pip install numpy`
- Check if it is installed: `python3 -m pip show numpy`

## Install OpenCV:

We will install the headless version since we wont be using the imshow command to display images. This is better for making a lighter docker image too.

- Install: `pip install opencv-python-headless`
- Check if it is installed (in a terminal):
  1. `python3`
  2. `import cv2`
  3. `cv2.__version__`

You should see the version of OpenCV installed.

## Run the scripts

1. Run the script locally:

```bash
cd 1-working-locally
python3 color-seg.py
```

Feel free to change the input image in line 4 and see different results

2. Make a docker image:

## Color segmentation algorithm

- I borrowed heavily from this color segmentation [tutorial](https://realpython.com/python-opencv-color-spaces/). Feel free to check it out if you want to better understand the algorithm and visualize it step by step. This is the
  [github repo](https://github.com/realpython/materials/blob/master/opencv-color-spaces/finding-nemo.py).
