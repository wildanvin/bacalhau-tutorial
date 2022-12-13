# Bacalhau demo with OpenCV

This is a tutorial on how to use Bacalhau with OpenCV. Read the full tutorial [here](https://mysterious-beaufort-cca.notion.site/Using-Bacalhau-with-OpenCV-2b3e473de89a41548a5fb77c4f2fd073).

> clone/fork this repo:

```bash
git clone https://github.com/wildanvin/bacalhau-tutorial.git
```

## 1. Run the script locally:

### Install numpy:

- Install: `pip install numpy`
- Check if it is installed: `python3 -m pip show numpy`

### Install OpenCV:

We will install the headless version since we wont be using the imshow command to display images. This is better for making a lighter docker image too.

- Install: `pip install opencv-python-headless`
- Check if it is installed (in a terminal):
  1. `python3`
  2. `import cv2`
  3. `cv2.__version__`

You should see the version of OpenCV installed.

> run the script:

```bash
cd 1-working-locally
python3 color-seg.py
```

Feel free to change the input image in line 4 and see different results.

### Color segmentation algorithm

- I borrowed heavily from this color segmentation [tutorial](https://realpython.com/python-opencv-color-spaces/). Feel free to check it out if you want to better understand the algorithm and visualize it step by step. This is the
  [github repo](https://github.com/realpython/materials/blob/master/opencv-color-spaces/finding-nemo.py).

## 2. Make a docker image:

### Install docker:

- Install: Depending of you OS check this [link](https://docs.docker.com/get-docker/). If you are using linux check this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
- Check if it is installed: docker info

> log into docker hub:

```bash
sudo docker login --username <your_username>
```

> create your image and upload it to docker hub:

```bash
cd 2-docker-image
export IMAGE=<your_dockerhub_username/your_image_name>
sudo docker build -t ${IMAGE} .
sudo docker image push ${IMAGE}
```

## 3. Upload to IPFS

Lots of great resources:

- [web3storage](https://web3.storage/)
- [nft.storage](https://nft.storage/docs/quickstart/)
- [pinata](https://app.pinata.cloud/)
- [IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop/)

## 4. Run Bacalhau

- Install:

  ```bash
  curl -sL https://get.bacalhau.org/install.sh | bash

  ```

- Check if it is installed:

  ```bash
  bacalhau version
  ```

Run Bacalhau with the Docker image and CID that you created:

```bash
bacalhau docker run \
-v <the_CID_of_the_folder_uploaded_to_IPFS>:/inputs \
<name_of_your_image_on_docker_hub> \
-- sh -c 'python3 color-seg.py ./inputs/dron2.jpg'
```

Look for an example in the [tutorial](https://mysterious-beaufort-cca.notion.site/Using-Bacalhau-with-OpenCV-2b3e473de89a41548a5fb77c4f2fd073).
