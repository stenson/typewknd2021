from coldtype import *

@animation((1080, 540), timeline=30, bg=hsl(0.35, 0.7, 0.6))
def gw2(f):
    def styler(g):
        fa = f.adj(-g.i*3)
        return [
            Style(Font.MutatorSans(), 100),
            dict(wght=fa.e("seio", 1))
        ]
    
    return (Glyphwise("TYPOGRAPHY", styler)
        .align(f.a.r, th=0)
        .f(1))