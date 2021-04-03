import pygame
import math

pygame.init()

WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font  = pygame.font.SysFont('timesnewroman', 25)
font_Points =  pygame.font.SysFont('timesnewroman', 15)
font_Points1 =  pygame.font.SysFont('timesnewroman', 20)

img1 = font.render('sin x', True, (0,0,0))
img2 = font.render('cos x', True, (0,0,0))

y_axis_points = [ font_Points.render('1.00',True,(0,0,0)),font_Points.render('0.75',True,(0,0,0)),font_Points.render('0.50',True,(0,0,0)),font_Points.render('0.25',True,(0,0,0)),font_Points.render('0.00',True,(0,0,0)),font_Points.render('-0.25',True,(0,0,0)),font_Points.render('-0.50',True,(0,0,0)),font_Points.render('-0.75',True,(0,0,0)),font_Points.render('-1.00',True,(0,0,0))  ]

x_axis_points1 = [  font_Points1.render('-3п',True,(0,0,0)),  font_Points1.render('-5п',True,(0,0,0)), font_Points1.render('-2п',True,(0,0,0)), font_Points1.render('-3п',True,(0,0,0)), font_Points1.render('-п',True,(0,0,0)), font_Points1.render('-п',True,(0,0,0)), font_Points1.render('0',True,(0,0,0)), font_Points1.render('п',True,(0,0,0)), font_Points1.render('п',True,(0,0,0)), font_Points1.render('3п',True,(0,0,0)),  font_Points1.render('2п',True,(0,0,0)),   font_Points1.render('5п',True,(0,0,0)),  font_Points1.render('3п',True,(0,0,0)), ]


class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)
def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope *    index    * dash_length)
        end   = origin + (slope * (index + 1) * dash_length)
        pygame.draw.aaline(surf, color, start.get(), end.get(), width)

def draw_dashed_lines(surf, color, points, width, dash_len):
    for i in range(len(points) - 1):
        draw_dashed_line(surf, color, points[i], points[i + 1], width, dash_len)

def get_points(f, xrange, step, kx, ky, center):
    num = math.ceil( (xrange[1] - xrange[0]) / step )
    x_values = (x * step + xrange[0] for x in range(num + 1))
    func = ((kx * x, ky * f(x)) for x in x_values)
    points = tuple(map(lambda x: (x[0] + center[0], -x[1] + center[1]), func))
    return points

k = 2 / 3
xrange = (-3 * math.pi, 3 * math.pi)
step = 0.1
kx = (k * WIDTH) / (6 * math.pi)
ky = (k * HEIGHT) / 2
center = (WIDTH // 2, HEIGHT // 2)

sin_points = get_points(math.sin, xrange, step, kx, ky-33, center)
cos_points = get_points(math.cos, xrange, step, kx, ky-33, center)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw coordinate lines
    start = (1 - k) / 2
    end = (k + (1 - k) / 2)
    pygame.draw.line(screen, (0, 0, 0), (start * WIDTH-33, HEIGHT // 2), (end * WIDTH+33, HEIGHT // 2), 2)
    pygame.draw.line(screen, (0, 0, 0), (WIDTH // 2, start* HEIGHT), (WIDTH // 2, end * HEIGHT), 2)
    '''
    pygame.draw.line(screen,(0,0,0), (start*WIDTH, 300),(end * WIDTH, 300), 1  )
    pygame.draw.line(screen,(0,0,0), (start*WIDTH, 250),(end * WIDTH, 250), 1  )
    pygame.draw.line(screen,(0,0,0), (start*WIDTH, 200),(end * WIDTH, 200), 1  )    
    pygame.draw.line(screen,(0,0,0), (start*WIDTH, 150),(end * WIDTH, 150), 1  )
    '''
    n = 9
    temp = 150
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (start*WIDTH-33, temp),(end * WIDTH+33, temp), 1  )
        n -= 1
        temp += 50
    n = 8
    temp = 175
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (start*WIDTH-33, temp),(start*WIDTH-20, temp), 1  )
        n -= 1
        temp += 50
    n = 8
    temp = 162.5
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (start*WIDTH-33, temp),(start*WIDTH-25, temp), 1  )
        n -= 1
        temp += 50
    n = 8
    temp = 187.5
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (start*WIDTH-33, temp),(start*WIDTH-25, temp), 1  )
        n -= 1
        temp += 50
    
    #--------
    n = 8
    temp = 175
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (end*WIDTH+23, temp),(end*WIDTH+33, temp), 1  )
        n -= 1
        temp += 50
    n = 8
    temp = 162.5
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (end*WIDTH+26, temp),(end*WIDTH+33, temp), 1  )
        n -= 1
        temp += 50
    n = 8
    temp = 187.5
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (end*WIDTH+26, temp),(end*WIDTH+33, temp), 1  )
        n -= 1
        temp += 50
    
    #--------




    n = 7
    temp = 200
    while n > 0:
        if n == 3:
            pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT),(temp, start*HEIGHT+34), 1  )
            pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT+84),(temp, end*HEIGHT), 1  )
            n -= 1
            temp += 133
        else:    
            pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT),(temp, end*HEIGHT), 1  )
            n -= 1
            temp += 133
    
    #--------
    n = 6
    temp = 267
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, end*HEIGHT),(temp, end*HEIGHT-12), 1  )
        n -= 1
        temp += 133
    n = 6
    temp = 234
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, end*HEIGHT),(temp, end*HEIGHT-9), 1  )
        n -= 1
        temp += 133
    n = 6
    temp = 300
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, end*HEIGHT),(temp, end*HEIGHT-9), 1  )
        n -= 1
        temp += 133
    
    n = 12
    temp = 217
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, end*HEIGHT),(temp, end*HEIGHT-5), 1  )
        n -= 1
        temp += 66.5
    n = 12
    temp = 250
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, end*HEIGHT),(temp, end*HEIGHT-5), 1  )
        n -= 1
        temp += 67
    
    #--------
    #pygame.draw.line(screen,(0,0,0), (333, start*HEIGHT),(333, end*HEIGHT), 1  )
    n = 6
    temp = 267
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT),(temp, start*HEIGHT+12), 1  )
        n -= 1
        temp += 133
    n = 6
    temp = 234
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT),(temp, start*HEIGHT+9), 1  )
        n -= 1
        temp += 133
    n = 6
    temp = 300
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT),(temp, start*HEIGHT+9), 1  )
        n -= 1
        temp += 133
    n = 12
    temp = 217
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT),(temp, start*HEIGHT+5), 1  )
        n -= 1
        temp += 66.5
    n = 12
    temp = 250
    while n > 0:
        pygame.draw.line(screen,(0,0,0), (temp, start*HEIGHT),(temp, start*HEIGHT+5), 1  )
        n -= 1
        temp += 67
    


    # Draw bounding box
    bounding_points = ((start * WIDTH-33, start * HEIGHT),
                       (end * WIDTH+33, start * HEIGHT),
                       (end * WIDTH+33, end * HEIGHT),
                       (start * WIDTH-33, end * HEIGHT))
    pygame.draw.lines(screen, (0, 0, 0), True, bounding_points, 2)

    # Draw functions
    draw_dashed_lines(screen, (0, 0, 255), cos_points, 2, 3)
    pygame.draw.aalines(screen, (255, 0, 0), False, sin_points, 2)

    screen.blit(img1, (720, 150))
    screen.blit(img2, (720, 170))
    pygame.draw.line(screen,(255,0,0), (780,168),(810,168)  )
    pygame.draw.line(screen,(0,0,255), (780,185),(788,185)  )
    pygame.draw.line(screen,(0,0,255), (791,185),(799,185)  )
    pygame.draw.line(screen,(0,0,255), (803,185),(810,185)  )

    n = 0
    temp = 140
    while n < 9:
        screen.blit(y_axis_points[n], (125, temp))
        n += 1
        temp+= 50
    
    i = 0
    temp = 177
    screen.blit(x_axis_points1[8], (731, 585))
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render('X',True,(0,0,0)), (593, 625))
    while i < 13:
        if i % 2 != 0:
            pygame.draw.line(screen, (0,0,0), (temp-5,605), (temp+25,605), 1)
        if i == 6:
            screen.blit(x_axis_points1[i], (temp+10, 585))
            i += 1
            temp+= 80
        else:
            screen.blit(x_axis_points1[i], (temp, 585))
            if i ==7:
                screen.blit(pygame.font.SysFont('timesnewroman', 20).render('2',True,(0,0,0)), (temp, 603))
                i += 1
                temp+= 68
            elif i % 2 != 0:
                screen.blit(pygame.font.SysFont('timesnewroman', 20).render('2',True,(0,0,0)), (temp+10, 603))
            i += 1
            temp+= 68
             
    
    # Render everything
    pygame.display.flip()
