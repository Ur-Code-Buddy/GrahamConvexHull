import tkinter as tk


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


def rescalePoints(points, canvasWidth, canvasHeight):
    def getMinX(p):
        return p[0]

    def getMaxX(p):
        return p[0]

    def getMinY(p):
        return p[1]

    def getMaxY(p):
        return p[1]

    minX = min(points, key= getMinX)[0]
    maxX = max(points, key= getMaxX)[0]
    minY = min(points, key= getMinY)[1]
    maxY = max(points, key= getMaxY)[1]
    scaleX = canvasWidth / (maxX - minX)
    scaleY = canvasHeight / (maxY - minY)
    return [(int((x - minX) * scaleX), int((y - minY) * scaleY)) for x, y in points]


def drawPoints(canvas, points, color):
    for x, y in points:
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color)


def drawLines(canvas, points, color):
    for i in range(len(points) - 1):
        canvas.create_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], fill=color)
    canvas.create_line(points[-1][0], points[-1][1], points[0][0], points[0][1], fill=color)


def displayConvexHull(points):
    points = rescalePoints(points, 400, 400)


    hull = getConvexHull(points)

    #GUI
    root = tk.Tk()
    root.title("Convex Hull")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()


    drawPoints(canvas, points, "blue")
    drawLines(canvas, hull, "red")


    root.mainloop()


def main():
    n = int(input("Enter set size: "))
    points = []
    for i in range(n):
        x, y = map(float, input("Enter point %d: " % (i + 1)).split())
        points.append((x, y))

    displayConvexHull(points)


main()