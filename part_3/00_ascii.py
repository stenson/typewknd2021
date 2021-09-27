from coldtype import *

from coldtype.time.nle.ascii import AsciiTimeline

at = AsciiTimeline(2, 24, """
                                <
    [A              ]
        [B          ]
            [C      ]
                    [W        ]
""")

@animation((1080, 540), timeline=at, bg=hsl(0.45))
def ascii(f):
    def styler(g):
        return Style(Font.MutatorSans(), 200,
            wdth=at[g.c].io2(f.i, 8, "eeio"),
            wght=at["W"].io2(f.i, 8, "eeio"))

    return (Glyphwise("ABC", styler)
        .align(f.a.r)
        .f(1))
