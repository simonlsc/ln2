from manim import *

class Tree:
  def __init__(self,node):
    self.node = node
    self.left = None
    self.right = None

myQueue=[]
def Level_Order_Traversal(root):
  traversed = []
  traversed.append(root)
  if root is None:
    return traversed
  while traversed != []:
    #print(traversed[0].node)
    myQueue.append(traversed[0].node)
    x = traversed.pop(0) 
    if x.left:
      traversed.append(x.left)
    if x.right:
      traversed.append(x.right)

def genTree(a,b,level):
    root = Tree((a,b))
    if level==0:
        return root
    else:
        root.left=genTree(a,(a+b)/2,level-1)
        root.right=genTree((a+b)/2,b,level-1)
        return root

myTree=genTree(1,2,6) # 7 levels, total 255 nodes
Level_Order_Traversal(myTree)
#print(myQueue)

class ln2(Scene):
    def construct(self):
        ax = Axes(
            x_range=[1, 2, 0.5], y_range=[0, 1, 0.5], x_length=6, y_length=6, axis_config={"include_tip": False, "include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        def reciprocal(x):
            return 1/x
        
        oneOverX=ax.plot(reciprocal, color=YELLOW)
        graphLable = ax.get_graph_label(oneOverX,"y=1/x",direction=RIGHT)
        self.add(ax, labels, oneOverX, graphLable)

        def fillArea(a,b,nth):
            if (nth % 2) == 0:
                sign="-"
                graphColor=BLUE
                rectColor=BLACK
                textColor=RED
                def f1(x):
                    if x >= a and x <= b:
                        return 1
                    else:
                        return 0
            else:
                sign="+"
                graphColor=RED
                rectColor=WHITE
                textColor=GREEN
                def f1(x):
                    if x >= a and x <= b:
                        return 2/(a+b)
                    else:
                        return 0

            graph=ax.plot(f1, color=graphColor)
            r = ax.get_riemann_rectangles(graph,x_range=[(a+b)/2, b], dx=(b-a)/2,color=rectColor,fill_opacity=1.0)
            t = Tex("$$"+sign+"\\frac{1}{"+str(nth)+"}$$").set_color(textColor)
            if nth <= 7:
                self.play(FadeIn(r),FadeIn(t))
            else:
                self.add(r,t)
            if nth <= 15:
                self.play(FadeOut(t))
            else:
                if nth <=63:
                    self.wait(duration=0.2)
                else:
                    self.wait(duration=0.1)
                self.remove(t)
            self.add(oneOverX)

        def removeArea(a,b):
            nth=int(round(reciprocal(reciprocal(a)*(b-a)/2)))
            fillArea(a,b,nth)

        def addArea(a,b):
            nth=int(round(reciprocal(reciprocal((b+a)/2)*(b-a)/2)))
            fillArea(a,b,nth)

        def process(a,b):
            #print(a,b)
            removeArea(a,b)
            addArea(a,b)

        def funcOne(x):
            return 1
        graph=ax.plot(funcOne, color=BLUE)
        r = ax.get_riemann_rectangles(graph,x_range=[1, 2], dx=0.5,color=WHITE,fill_opacity=1.0)
        #self.add(r)
        self.play(FadeIn(r))
        self.add(oneOverX)
        t = Tex("1").set_color(GREEN)
        self.play(FadeIn(t))
        self.play(FadeOut(t))

        #print(myQueue)
        for q in myQueue:
            process(*q)

        lines=Tex(
            "$$1-\\frac{1}{2}+\\frac{1}{3}-\\frac{1}{4}\\cdot\\cdot\\cdot$$",
            "$$=\\sum_{n=0}^{\\infty}(-1)^{n}\\frac{1}{n+1}$$",
            "$$=\\int_{1}^{2}\\frac{1}{x}\\mathrm{d} x$$",
            "$$=[\\ln x]_{1}^{2}$$",
            "$$=\\ln 2-\\ln 1$$",
            "$$=\\ln 2$$"
        ).shift(LEFT*5+UP*0.5).scale(0.5)
        for line in lines:
            self.play(FadeIn(line))

        self.wait()

