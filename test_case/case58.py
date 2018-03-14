# 题目：画图，学用rectangle画方形。
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111, aspect='equal')
# ax1.add_patch(
#     patches.Rectangle(
#         (0.1, 0.1),   # (x,y)
#         0.5,          # width
#         0.5,          # height
#     )
# )
# fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')
if __name__ == '__main__':
    from tkinter import *
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root,width = 400,height = 400,bg = 'yellow')
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0,y0,x1,y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()