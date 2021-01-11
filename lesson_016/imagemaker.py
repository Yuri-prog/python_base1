import datetime
import cv2
from PIL import Image
import os

class ImageMaker:
    def __init__(self):
        self.text = ''

    def viewimage(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def card(self, print_date, pr_text, cloud_cover):
        background = cv2.imread('python_snippets/external_data/probe1.jpg')
        picture = cv2.imread('')
        picture_1 = cv2.imread('')
        for x in range(1024):
            yellow = (255 - (x // 4), 255, 255)
            light_blue = (255, 335 - (x // 4), 315 - (x // 4))
            blue = (255, 255 - (x // 4), 255 - (x // 4))
            gray = (295 - (x // 4), 295 - (x // 4), 295 - (x // 4))
            if 'Снег' in cloud_cover or 'снег' in cloud_cover:
                card_color = light_blue
                picture = Image.open('python_snippets/external_data/weather_img/snow.jpg')
                if 'Облачно' in cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
                elif 'Ясно' in cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/sun.jpg')
            elif 'Дождь' in cloud_cover or 'дождь' in cloud_cover:
                card_color = blue
                picture = Image.open('python_snippets/external_data/weather_img/rain.jpg')
                if 'Облачно' in cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
                elif 'Ясно' in cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/sun.jpg')
            elif 'Ясно' in cloud_cover:
                card_color = yellow
                picture = Image.open('python_snippets/external_data/weather_img/sun.jpg')
            elif 'Переменная облачность' in cloud_cover:
                card_color = yellow
                picture = Image.open('python_snippets/external_data/weather_img/sun.jpg')
                picture_1 = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
            else:
                card_color = gray
                picture = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
            print_card = cv2.line(background, (x, 0), (x, 512), card_color, 10)
        y = 220
        print_card = cv2.putText(print_card, print_date, (3, y), cv2.FONT_HERSHEY_COMPLEX,
                                 0.7, (0, 0, 200), 1, cv2.LINE_AA)
        for string in pr_text.split('  '):
            print_card = cv2.putText(print_card, string, (3, y + 40), cv2.FONT_HERSHEY_COMPLEX,
                                     0.5, (0, 55, 0), 1, cv2.LINE_AA)
            y += 20

        # у вас получается несколько сохранений идёт?
        # зачем сохранять изображение до того, как оно будет готово?
        # До сохранения print_card -объект cv2, с ним paste не работает. А после сохранения это уже открытая
        # картинка, тогда все вставляется.
        cv2.imwrite('Card.jpg', print_card)
        print_card = Image.open('Card.jpg')
        print_card.paste(picture, (25, 25))
        if picture_1:
            print_card.paste(picture_1, (125, 25))
        path = "Cards"
        if not os.path.exists(path):
            os.mkdir(path)
        print_card.save(f"Cards\{print_date[-11:-1]}.jpg")
        result = cv2.imread(f'Cards\{print_date[-11:-1]}.jpg')
        cv2.imshow('window', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def test():
    imagemaker = ImageMaker()
    today = datetime.datetime.today()
    imagemaker.card(f'Прогноз погоды на {today.date()}:', 'test  test', 'Ясно')

#test()
