from coldtype import *
from coldtype.fx.skia import phototype
from coldtype.fx.motion import filmjitter

midi = Programs.Midi("media/drums.mid", text=0)
drums = midi.t[0]

@animation(timeline=midi.t, bg=0, render_bg=1)
def anim(f):
    def de(n, pre=3, post=20, rng=(0, 1)):
        return drums.fv(f.i, [n], (pre, post)).ease(rng=rng)
    
    grvts = [
        de(36, 5, 50),
        de(37, 3, 20),
        de(38, 3, 30),
        de(42, 3, 30),
        de(50, 3, 50),
        de(43, 3, 30),
        de(45, 3, 30),
        de(47, 3, 30),
    ]

    return (Glyphwise("MIDI\nTYPE", lambda g: [
        Style(Font.Find("CheeeV"), 450, tu=50, wdth=0, wght=1, ro=1),
        dict(
            yest=1-grvts[g.i],
            grvt=1-grvts[g.i],
            temp=1-grvts[g.i])])
        .track(30, v=1)
        .xalign(f.a.r, th=0)
        .align(f.a.r, th=0)
        #.translate(0, 25)
        .fssw(-1, 1, 7)
        .layer(
            lambda p: p
                .ch(filmjitter(f.e("l"), 10, speed=(5, 10), scale=(1, 2)))
                .ch(phototype(f.a.r, blur=20, cut=90, cutw=90, fill=hsl(0.9, 1, 0.75))),
            lambda p: p
                .ch(filmjitter(f.e("l"), 5, speed=(5, 10), scale=(1, 2)))
                .ch(phototype(f.a.r, blur=3, cut=90, cutw=20, fill=hsl(0.3, 1, 0.75)))
                #.blendmode(BlendMode.Cycle(67))
        ))

release = anim.export("h264",
    loops=8,
    audio="media/drums_and_keys.wav",
    audio_loops=4,
    vf="eq=brightness=0.0:saturation=1.5")