from matplotlib import pyplot as plt
import cv2 as cv
import easyocr,os,time,random,string
#Version 0.15

class Video_Webcam_Image_OCR:
    def __init__(self):
        print("Tapez sur la touche 's' pour capturer l'image est pour analyser/ touche 'q' pour quitter le programme.")
        print("[+]1:Webcam \n"
              "[+]2:Video path\n"
              "[+]3:Image path")
        try:
            choix = int(input("[+/=\+]: "))
            if choix == 1:
                self.Video_Webcam_OCR(0)
            elif choix == 2:
                video_path_absolut = input("Entrez le chemin COMPLET de votre video: ")
                if os.path.exists(video_path_absolut):
                    self.Video_Webcam_OCR(video_path_absolut)
                else:
                    print("Veuillez vérifier le chemin de votre video.")

            elif choix == 3:
                image_path_absolut = input("Entrez le chemin COMPLET de votre images: ")
                if os.path.exists(image_path_absolut):
                    self.Image_OCR(image_path_absolut)
                else:
                    print("Veuillez vérifier le chemin de votre image.")
            else:
                print("choisissez le menu 1/2 ou 3")

        except ValueError:
            print("Entrez Le menu 1/2 ou 3 ")

    def Video_Webcam_OCR(self,path_or_webcam):
        strings = string.ascii_letters
        compteur = random.randint(1, 11)
        name_path = "".join([random.choice(strings) for n in range(0, compteur)]) + ".jpg"
        video = cv.VideoCapture(path_or_webcam)
        while video.isOpened():
            ret, frame = video.read()
            if ret:
                cv.imshow("Webcam", frame)
                if cv.waitKey(25) & 0xff == ord("s"):
                    cv.imwrite(name_path, frame)
                    print("SCREEN !!")
                    time.sleep(0.2)
                elif cv.waitKey(25) & 0xff == ord("q"):
                    print("QUIT !!")
                    video.release()
                    cv.destroyAllWindows()
            else:
                print("Exiting...")
        if os.path.exists(name_path):
            screen_image = cv.imread(name_path)
            reader = easyocr.Reader(["fr"])
            result = reader.readtext(name_path)
            for detection in result:
                top_left = tuple([int(val) for val in detection[0][0]])
                bottom_right = tuple([int(val) for val in detection[0][2]])
                text = detection[1]
                font = cv.FONT_HERSHEY_SIMPLEX
                img = cv.rectangle(screen_image, top_left, bottom_right, (0, 255, 255, 0), 3)
                img = cv.putText(screen_image, text, top_left, font, 1, (255, 255, 255), 2, cv.LINE_AA)
            plt.imshow(img),plt.xticks([]),plt.yticks([])
            plt.show()

    def Image_OCR(self,path_image):
        img = cv.imread(path_image)
        reader = easyocr.Reader(["fr"])
        result = reader.readtext(path_image)
        for detection in result:
            top_left = tuple([int(val) for val in detection[0][0]])
            bottom_right = tuple([int(val) for val in detection[0][2]])
            text = detection[1]
            font = cv.FONT_HERSHEY_SIMPLEX
            img = cv.rectangle(img,top_left, bottom_right, (0, 255, 255, 0), 3)
            img = cv.putText(img,text,top_left, font, 1, (255, 255, 255), 2, cv.LINE_AA)
        plt.imshow(img),plt.xticks(),plt.yticks()
        plt.show()

if __name__ == "__main__":
    Video_Webcam_Image_OCR()
