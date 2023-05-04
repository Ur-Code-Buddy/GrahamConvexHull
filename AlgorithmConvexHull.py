import tkinter as tk
import random


def getConvexHull(points):
    def sortPoints(p):
        return (p[1], p[0])

    start = min(points, key=sortPoints)
    hull = [start]  #Start with the leftmost

    while True:
        end = points[0]
        for p in points[1:]:
            if p == hull[-1]:
                continue
            cross = (p[0] - hull[-1][0]) * (end[1] - hull[-1][1]) - (p[1] - hull[-1][1]) * (end[0] - hull[-1][0])
            if end == hull[-1] or cross < 0:
                end = p  #Update the endpoint

        if end == start:  #complete
            break
        hull.append(end)

    return hull



def drawPoints(canvas, points, color):
    for x, y in points:
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color)


def drawLines(canvas, points, color):
    for i in range(len(points) - 1):
        canvas.create_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], fill=color)
    canvas.create_line(points[-1][0], points[-1][1], points[0][0], points[0][1], fill=color)


def displayConvexHull(points):

    hull = getConvexHull(points)


    min_x = points[0][0]
    for p in points:
        if p[0] < min_x:
            min_x = p[0]

    max_x = points[0][0]
    for p in points:
        if p[0] > max_x:
            max_x = p[0]

    min_y = points[0][1]
    for p in points:
        if p[1] < min_y:
            min_y = p[1]

    max_y = points[0][1]
    for p in points:
        if p[1] > max_y:
            max_y = p[1]

    width = max_x - min_x
    height = max_y - min_y
    padding = max(width, height) * 0.1
    canvas_width = int((width + padding * 2) * 10)
    canvas_height = int((height + padding * 2) * 10)
    scale = 5

    root = tk.Tk()
    root.title("Convex Hull")
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    for x, y in points:
        canvas.create_oval((x - min_x + padding) * scale - 3, (y - min_y + padding) * scale - 3,
                            (x - min_x + padding) * scale + 3, (y - min_y + padding) * scale + 3, fill="blue")

    for i in range(len(hull) - 1):
        canvas.create_line((hull[i][0] - min_x + padding) * scale, (hull[i][1] - min_y + padding) * scale,
                           (hull[i+1][0] - min_x + padding) * scale, (hull[i+1][1] - min_y + padding) * scale,
                           fill="red")

    canvas.create_line((hull[-1][0] - min_x + padding) * scale, (hull[-1][1] - min_y + padding) * scale,
                       (hull[0][0] - min_x + padding) * scale, (hull[0][1] - min_y + padding) * scale,
                       fill="red")

    root.mainloop()



def main():

    #n = int(input("Enter set size: "))
    n = random.randint(4,30)
    print(n)
    points = []
    for i in range(n):
        x = random.randint(5,100)
        y =  random.randint(5,100)
        print("point:",i,"x:",x,"y",y)
        #x, y = map(float, input("Enter point %d: " % (i + 1)).split())
        points.append((x, y))

    displayConvexHull(points)


main()