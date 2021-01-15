from bs4 import BeautifulSoup
import requests
import os
from PIL import Image
# Interface
import tkinter as tk

window = tk.Tk()
# Set Window title, size, and color
window.title('Images Crawler')
window.geometry('800x600')
window.configure(background='white')

def get_image():
    input_image = image_entry.get()
    response = requests.get(f"https://unsplash.com/s/photos/{input_image}")
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.find_all("img", {"class": "_2UpQX"}, limit=3)
    image_links = [result.get("src") for result in results]  # 取得圖片來源連結
    for i, link in enumerate(image_links):
        if not os.path.exists("images"):
            os.mkdir("images")  # 建立資料夾
 
        img = requests.get(link)  # 下載圖片
        with open("images/" + input_image + str(i+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼

        im = Image.open("images/" + input_image + str(i+1) + ".jpg")
        print(im.size)
        if im.size[0] >= 1000 and im.size[1] >= 1000 :
            if not os.path.exists("images/high_images"):
                os.mkdir("images/high_images")
            im.save("images/high_images/" + input_image + str(i+1) + ".jpg")
        else:
            if not os.path.exists("images/low_images"):
                os.mkdir("images/low_images")
            im.save("images/low_images/" + input_image + str(i+1) + ".jpg") 
        feedback_label.configure(text='Finish! Images had in the images folder.')


header_label = tk.Label( window, text='Images Crawler')
header_label.pack()

# Input image group
image_frame = tk.Frame(window)
image_frame.pack(side=tk.TOP)
image_label = tk.Label(image_frame, text='Image')
image_label.pack(side=tk.LEFT)
image_entry = tk.Entry(image_frame)
image_entry.pack(side=tk.LEFT)

# button
catch_button = tk.Button(window, text='Catch', command=get_image)
catch_button.pack()

# feedback 
feedback_label = tk.Label(window)
feedback_label.pack()

window.mainloop()