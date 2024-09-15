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
Now open up the second script and run the first 3 cells. After that we will go and tag all of our images on a website called  [makesense.ai](https://www.makesense.ai/).
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








