from coldtype import *

"""
To "solo" the first animation, hit shift+1
To "solo" the second animation, hit shift+2
To unsolo everything, hit shift+0
"""

@animation((1080, 540), timeline=60, bg=0)
def wave(f):
    def styler(g):
        fa = f.adj(-g.i*5)
        return Style(Font.MutatorSans(), 100,
            #wght=f.e("seio", 1),
            wdth=fa.e("seio", 1))

    txt = (Glyphwise("TYPOGRAPHY", styler)
        .align(f.a.r, th=0)
        .f(bw(1)))

    return PS([
        #P().rect(txt.ambit().inset(-20, 1.5)).fssw(-1, 1, 5),
        txt
    ])

@animation((1080,1080), timeline=wave.duration, bg=0, render_bg=1)
def wave_comp(f):
    return PS.Enumerate(range(0, 13), lambda x:
        wave.frame_img(f.i-x.i*3)
            #.blendmode(BlendMode.Lighten)
            .translate(0, -260+x.i*90))