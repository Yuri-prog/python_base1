import simple_draw as sd
#sd.resolution = (1200, 600)
N = 10

x_list = []
y_list = []
size_list = []
speed_list = []

#color = ''
colors = {
        'красный':sd.COLOR_RED,
        'оранжевый':sd.COLOR_ORANGE,
        'желтый':sd.COLOR_YELLOW,
        'зеленый':sd.COLOR_GREEN,
        'голубой':sd.COLOR_CYAN,
        'синий':sd.COLOR_BLUE,
        'фиолетовый':sd.COLOR_PURPLE,
        'разный':sd.random_color,
        'фон':sd.background_color,
        'белый':sd.COLOR_WHITE,
         }
cl = colors['красный']

def flake():
     for i in range(0, N):
         k = sd.random_number(0, sd.resolution[0])
         x_list.insert(i, k)
         k = sd.random_number(sd.resolution[1] - 100, sd.resolution[1])
         y_list.insert(i, k)
         k = sd.random_number(10, 100)
         size_list.insert(i, k)
         size = size_list[i]

         sd.snowflake(center=sd.get_point(x=x_list[i], y=y_list[i]), length=size, )

start_point = sd.get_point(300, 50)
def draw_branches(start_point, angle, length):

    start_point_1 = start_point
    start_point_2 = start_point
    angle_1 = angle
    angle_2 = angle
    while length >= 10:
        v1 = sd.get_vector(start_point = start_point_1, angle = angle_1, length = length, width = 1)
        v2 = sd.get_vector(start_point = start_point_2, angle = angle_2, length = length, width = 1)
        length = 0.6*length
        start_point_1 = v1.end_point
        start_point_2 = v2.end_point
        angle_1 += 30
        angle_2 -= 30
        v1.draw()
        v2.draw()

#flake()



# def colore(color):#     cl = colors[1]
#     #snowflak()


#color('желтый')
#snowflak()
sd.pause()