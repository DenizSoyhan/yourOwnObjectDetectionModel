![Object_Detection_🎯](https://github.com/user-attachments/assets/d3cbb329-fb8d-4616-9a07-bf9885c36ad1)

Creating your own Object Detection Model might seem like a daunting task but FEAR NOT!
With Yolov4 and our guidance through this repo you will get your very own object detection model for any video game in no time. And you might be able to use this model for way more than just video games(spoilers!)
# 0) Preparation:
You will need some tools to get everything working so please get these dependencies figured out before we start:
>* jupyter
>* opencv-python
>* Pillow
>* numpy
>* pywin32
>* pynput


After all the dependencies are set go and clone this repo. Open up the directory on "Jupyter Notebook" by using this command in cmd:

```
jupyter notebook [YOUR_DIRECTORY_PATH]
```
And you are good to go!

# 1) Data Collection
In order to train your model you need to collect vast amount of data. The more data you have the better you can train your model. Most of the time you need to find different data bases that suits your purposes and occasionally these data bases will be behind a pay wall. So why not collect your own? Open up the first script and run it cell by cell.

This script will take screenshots of your screen between every interval you tell it to. The default is 3 seconds in the code and you can change it by altering this parameter in the script:
<p align="center">
<img src="https://github.com/user-attachments/assets/81b910d6-99e6-41a4-8609-7e7bcb163ca1" width="600" />
</p><br>

You can just play your game in fullscreen and collect data. The screenshots are in the directory that is created in the same path as all the files called simply **"images"**


# 2) Refining the Data Set
Now open up the second script and run the first 3 cells. After that we will go and tag all of our images on a website called  [makesense.ai](https://www.makesense.ai/)
Upload all your images to the website and choose object detection when it asks for what you want to do with the files<br>

<p align="center">
<img src="https://github.com/user-attachments/assets/83f95d1f-10ad-4080-845d-1569678b6d72" width="400" />
</p><br>


Then add your labels. In our case we trained a model on the game "Euro Truck Simulator 2". So we added "car" and "roadsign" as our labels. The order of the names are important so take a note please.<br>
<p align="center">
<img src="https://github.com/user-attachments/assets/78562e48-3fa0-43a1-8c0c-6edcb6d50228" width="800" />
</p>
After you are done with the tagging the images export them in YOLO format that we will be working on and also VOC XML format for backup<br><br>

<p align="center">
<img src="https://github.com/user-attachments/assets/83f95d1f-10ad-4080-845d-1569678b6d72" width="400" />
</p><br>

Extract the .txt files from the zip that you got from makesense.ai and then put every .txt into the newly created the **"shuffled_images"**. Then you can keep running the cells. The last cell requires you to write the Object Names in the order of makesense.ai and after running the last cell everything is ready for the next step!

<p align="center">
<img src="https://github.com/user-attachments/assets/2b8af1ac-fd5a-427c-b3ef-9d3f47840f1c" width="400" />
</p><br>

# 3 )Training

Upload the **"yolov4-tiny"** to your Google Drive directly. Then open up [Google Collab](https://colab.research.google.com/)
Upload the the third script on your Google Collab as a notebook. From the top left change the **"Runtime Type"**  to T4 GPU. 

<p align="center">
<img src="https://github.com/user-attachments/assets/15223032-ed98-493a-b06c-2533fb16cb84" width="800" />
</p><br>

A problem we encountered is that the training was taking a long time and Google Collab thinks we are idle and terminates the training. Because of that the training would not finish or wouldn't be enough. 2 solutions that we find to there problem were:
### 1) DON'T BE AFK:
If you just play with Collab page and do some clicking or editing once in a while from the start the termination was significantly delayed but always prematurely ended. So we finally gave in and did the second thing. 
### 2) Just Buy Premium:
The standart premium Collab package was surprisingly really cheap for our local currency so we just bought it. The 13 hours for us to train the model was finished and we only used 20 GB of our 100 GB
server access.<br>
When you start the training the output cell should look like this and also give you an aproximate time left between epochs.<br><br>
<p align="center">
<img src="https://github.com/user-attachments/assets/f9feb794-f264-4dac-b329-cf5639399dce" width="700" />
</p><br>

And every once in a while the trained model will be saved onto your Drive in the yolo-v4 under the **"training"** directory. When the process is finished you want to use the one that is named **"yolov4-tiny-custom_last.weights"**. And you are done! Congrats! If you want to try out your model you can go to the 4th script.

# 4) Try It Out
Download **"yolov4-tiny-custom_last.weights"** and put it in the same directory as the 4th script. Open it up in the Jupyter Notebook. Change the window name parameter in the script to the window of your game. And when you run, it will start capturing and detecting a certain part of your screen. You can see our model's and detection in the game "Euro Truck Simulator 2". There should be a repo on this profile where you can find our trained model too if you wanna try it out.


<p align="center">
<img src="https://github.com/user-attachments/assets/c99b3823-6baa-4ab6-9303-26bdc272cf75" width="500" />
</p><br>
<p align="center">
<img src="https://github.com/user-attachments/assets/774f5feb-201d-4037-b4ad-2e22af05d871" width="" />
</p><br>
<p align="center">
<img src="https://github.com/user-attachments/assets/211ee8b9-3a88-4b3e-afa1-e55b9af55c87" width="" />
</p><br>

The model even works with real life traffic footage 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<p align="center">
<img src="https://github.com/user-attachments/assets/58eea4b2-eaa7-450d-9e82-bc18b92bdc9c" width="600" />
</p><br>

So even if you are starting to train your model for a video game there are a lot of potential for real life use of "You Only Look Once" models!
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<p align="center">
<img src="https://github.com/user-attachments/assets/3c6b9fce-1359-43bf-a29a-72f7fa3c460f" width="600" />
</p><br>

<b><p align="center">
**Thank you for following through!**
</p><b>





