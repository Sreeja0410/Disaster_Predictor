<h1 align="center">Disaster Predictor</h1>

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Technologies Used](#technologies-used)

## Overview
This [repository](https://github.com/Sreeja0410/Disaster_Predictor) was to create a solution that can accurately classify images into four types of disasters: cyclones, earthquakes, floods, and wildfires. This project can contribute to environmental conservation and disaster management efforts. By accurately detecting different types of disasters, this system aims to assist various stakeholders, including emergency response teams, government agencies, and individuals living in disaster-prone areas. This solution can aid in timely response, resource allocation, and decision-making, ultimately helping to minimize the impact of disasters and save lives.

The proposed project, a disaster detection system based on AI technologies, aims to address the societal challenge of efficient disaster management and response. By accurately classifying images into different types of disasters, such as cyclones, earthquakes, floods, and wildfires, the system can contribute to timely and informed decision-making, resource allocation, and response coordination.

The basic approach I used to solve the problem is to develop a solution using computer vision which can generalize among the four major types of disasters. I used transfer learning, fine-tuned VGG-16 which is a state of the art convolutional neural network. I used tensorflow, a popular deep learning package to implement the fine-tuning algorithm to train the model. I have collected the data from a publicly available database by an individual. The project has three parts: 
- Data arrangement,
- Training the model,
- Deploying the model.

## Installation
To run my app on your local machine, do the following steps.
> **Step 1** : 
   - I have written the Code with Python 3.7.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/release/python-377/).
   - If you are using a lower version of Python you can upgrade using the pip package, kindly ensure that you have the latest version of pip.
> **Step 2** :
   - If you want the current version of my repository to be in your github, you can do forking my repository by clicking as shown in the picture below.
   
   
   - Clone my repository to your local machine by running the following command. Before doing this, you have to install git on your machine and make sure you are having proper internet connection.
      - For **Windows OS** user, open *git bash* and run the following command.
      ```bash
      git clone https://github.com/Sreeja0410/Disaster_Predictor.git
      ```
      
      - For **Linus OS** user, open *Terminal* and run the following command.
      ```bash
      git clone https://github.com/Sreeja0410/Disaster_Predictor.git
      ```
   
   - If you don't want to mess up with all these things, you can just download the *zip* file of my GitHub repository by clicking [here](https://github.com/Sreeja0410/Disaster_Predictor/archive/refs/heads/main.zip) and extract it to any file location as your wish and then use it.
   - Now we have done with the downloading of my whole project.

> **Step 3** :
   - After downloading the whole repo, get into the main folder by hit the following command in git bash for Windows OS users and Terminal for Linux OS users.
   ```bash
   cd Desktop
   ```

> **Step 4** :
   - Now we are going to install all the dependency libraries for this project. Before that you must have Python 3.7.7 and latest version of pip.
   - To install tensorflow and PIL packages, run the following command.
   
   ```bash
    pip install tensorflow
    pip install Pillow
   ```
   
> **Step 5** :
   - After installing all the dependency libraries, you are ready to run my app on your local machine.
   - To test the model, run the following command on custom images by entering image address in the code, images should be imported into the repo folder. Output will be the probability of the disaster type.
   ```bash
   python disaster_detector.py 
   ```
> **Step 6** :
   - To train the model, data should be downloaded from [here](https://drive.google.com/file/d/1NvTyhUsrFbL91E10EPm38IjoCg6E2c6q/view), the data folder should be inside the repo folder, first run following command. After downloading dataset rename the folder as Disaster then import it into repo folder. This empty folder must be created before running the following command.
   ```bash
python data_arrange.py
   ```

> **Step 7** :
   - Then run the following command to train the model on dataset. Model will be saved in CNN_Model folder.
   ```bash
python CNN_train.py
   ```

## Directory Tree

```bash
Disaster-Predictor
|__Disaster (dataset folder)
     |__Cyclone
     |__Earthquake
     |__Flood
     |__Wildfire
|__CNN_Model
     |_vgg16_dd.h5
|__FineData (this empty folder must be created before running data_arrange.py)
|__Disaster_detector.py
|__Data_arrange.py
|__CNN_train.py
|__vgg16.multiclassifier.h5 (For model training)
|__Test images
```
## Technologies Used

- Python
- Tensorflow
- Deep Learning
