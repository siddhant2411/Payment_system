import cv2
from pyzbar import pyzbar
stop= 0
barcode_value=0
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
        barcode_value=barcode_info
        print(barcode_info)
        stop=1
        #print(stop)

    return frame
def main():

   #1
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

   #    Image Scanning code
   #
   # height = 800
   # width = 600
   # green = (0, 255, 0)
   #
   # image = cv2.imread("abc.jpg")
   #
   # image = cv2.resize(image, (width, height))
   # orig_image = image.copy()
   # frame = read_barcodes(orig_image)
   # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert the image to gray scale
   # blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Add Gaussian blur
   # edged = cv2.Canny(blur, 75, 200)  # Apply the Canny algorithm to find the edges
   #
   #
   # cv2.destroyAllWindows()


#4
if __name__ == '__main__':
    main()