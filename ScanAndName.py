import cv2
import requests
from bs4 import BeautifulSoup
from pyzbar import pyzbar
stop=0
barcode_value=0
product_name=''
def read_barcodes(frame):

    barcodes = pyzbar.decode(frame)


    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1

        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        # 3
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
        global stop
        global barcode_value
        barcode_value = (barcode_info)
        print(barcode_info)
        global product_name
        product=nameSearch(barcode_info)

        if product!=None:
            product_name = product
            print(product)
        stop=1
        #print(stop)

    return frame

def nameSearch(id):
    barcode = id
    URL = 'https://api.upcitemdb.com/prod/trial/lookup?upc=' + ''.join(barcode)
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    description = soup.prettify()
    a = description.find('title')
    error = description.find('INVALID_UPC')
    if (description.find('INVALID_UPC') == -1):
        start = description.find("title") + 8
        # print(start)
        if (description.find('"items":[]') == -1):
            # print(description.find('"total": 0'))
            end = description.find('"', 76)
            # print(end)
            product = description[start:end]
            return product
        else:
            print("Product Not Found")
    else:
        print("Invalid Barcode")

    
def main():
    # 1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    done=""
    global stop
    while ret and stop==0:
        ret, frame = camera.read()
        frame= read_barcodes(frame)

        cv2.imshow('Barcode/QR code reader', frame)
        #done= barcode.data.decode('utf-8')
        if cv2.waitKey(1) & 0xFF == 27:
            break
       # if done!="":
           # print("end of loop")

    #3
    camera.release()
    cv2.destroyAllWindows()
    height = 800
    width = 600
    green = (0, 255, 0)
    #
    # image = cv2.imread("abc.jpg")
    #
    # image = cv2.resize(image, (width, height))
    # orig_image = image.copy()
    # frame = read_barcodes(orig_image)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert the image to gray scale
    # blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Add Gaussian blur
    # edged = cv2.Canny(blur, 75, 200)  # Apply the Canny algorithm to find the edges

    # Show the image and the edges
    # cv2.imshow('Original image:', image)
    # cv2.imshow('Edged:', edged)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()



#4
if __name__ == '__main__':
    main()