# Base44 badge set for Indica Independent Media.
# Colours measured from Pete's screenshots of app.base44.com/@indica (2026-10-29):
#   orange #FF6A00, card #161616, tile border #3D3C3A, check box #134F25 with #95C6A0 mark,
#   Maker pill green #568F63. Shapes are hand-traced recreations of the badge art on that page.
import os, math

ORANGE="#FF6A00"; CARD="#161616"; TILE="#1B1B1B"; BORDER="#3D3C3A"; CHECK_BG="#134F25"; CHECK_FG="#95C6A0"
WHITE="#F3F3F1"; GREY="#A9A7A3"; PILL="#568F63"; PILL_BG="#1F3A28"
FONT="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
PROFILE="https://app.base44.com/@indica"

BADGES=[
 ("maker-dna","Maker DNA","Can't stop building. Ships fast, iterates faster.","2026-10-05"),
 ("ai-native","AI Native","AI isn't a feature. It's the foundation.","2026-10-28"),
 ("automation-architect","Automation Architect","Builds systems that run themselves.","2026-10-05"),
]

def icon_maker_dna():
    # up arrow split into two halves offset like a twist, with a DNA ladder in the gap
    left ="M46,22 L46,92 L28,92 L28,52 L14,52 Z"
    right="M54,8 L86,38 L72,38 L72,78 L54,78 Z"
    out=[f'<path d="{left}" fill="{ORANGE}"/>',f'<path d="{right}" fill="{ORANGE}"/>']
    out.append(f'<line x1="50" y1="20" x2="50" y2="86" stroke="{WHITE}" stroke-width="2.4"/>')
    rungs=[(26,40,60),(36,36,64),(46,38,62),(56,36,64),(66,40,60),(76,36,64)]
    for y,a,b in rungs:
        out.append(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}" stroke="{WHITE}" stroke-width="2.2"/>')
        out.append(f'<circle cx="{a}" cy="{y}" r="2.9" fill="{WHITE}"/><circle cx="{b}" cy="{y}" r="2.9" fill="{WHITE}"/>')
    return "".join(out)

def icon_ai_native():
    # blocky head in profile facing left, with a network of nodes over the crown
    head="M34,56 L50,36 L68,46 L68,80 Q68,88 60,88 L34,88 L34,70 L28,66 L34,62 Z"
    out=[f'<path d="{head}" fill="{ORANGE}"/>',f'<rect x="44" y="58" width="5.5" height="8.5" fill="{WHITE}"/>']
    nodes=[(50,36),(34,28),(42,12),(62,16),(78,26),(86,46),(24,46)]
    edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,3),(1,6),(0,5),(0,4)]
    for a,b in edges:
        (x1,y1),(x2,y2)=nodes[a],nodes[b]
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{WHITE}" stroke-width="1.6"/>')
    for x,y in nodes: out.append(f'<circle cx="{x}" cy="{y}" r="2.9" fill="{WHITE}"/>')
    return "".join(out)

def icon_automation_architect():
    # six curved orange blades around a white five-point star
    blade='M50,50 L56,30 L68,14 L88,20 L82,38 L62,48 Z'
    out=[f'<path d="{blade}" fill="{ORANGE}" transform="rotate({k*60} 50 50)"/>' for k in range(6)]
    pts=[]
    for i in range(10):
        r=12 if i%2==0 else 5.2; a=-math.pi/2+i*math.pi/5
        pts.append(f"{50+r*math.cos(a):.2f},{50+r*math.sin(a):.2f}")
    out.append(f'<polygon points="{" ".join(pts)}" fill="{WHITE}"/>')
    return "".join(out)

ICONS={"maker-dna":icon_maker_dna,"ai-native":icon_ai_native,"automation-architect":icon_automation_architect}

def svg(w,h,body,title,desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc>{body}</svg>')

def icon_svg(key,title,desc):
    return svg(100,100,ICONS[key](),f"Base44 badge icon: {title}",desc)

def check_box(x,y,s=24):
    return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="4" fill="{CHECK_BG}" stroke="#1F6B33" stroke-width="1"/>'
            f'<polyline points="{x+6},{y+s/2} {x+s*0.42},{y+s-7} {x+s-6},{y+7}" fill="none" stroke="{CHECK_FG}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')

def card_svg(key,title,desc,claimed):
    # full card, same proportions as the profile page card (523 x 312)
    body=[f'<rect x="0.5" y="0.5" width="523" height="311" rx="10" fill="{CARD}" stroke="{BORDER}"/>',
          f'<rect x="16.5" y="16.5" width="491" height="207" rx="8" fill="{TILE}" stroke="{BORDER}"/>',
          check_box(464,28),
          f'<g transform="translate(200 70) scale(1.24)">{ICONS[key]()}</g>',
          f'<text x="262" y="258" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" fill="{WHITE}">{title}</text>',
          f'<text x="262" y="284" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{GREY}">{desc}</text>']
    return svg(524,312,"".join(body),f"Base44 badge: {title}",f"{desc} Earned by Indica Independent Media on Base44, claimed {claimed}.")

def maker_pill(w=96,h=26,one_percent=True):
    out=[f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="6" fill="{PILL_BG}" stroke="{PILL}"/>',
         f'<rect x="12" y="{h/2-3}" width="6" height="6" fill="{PILL}"/>',
         f'<text x="{w/2+4}" y="{h/2+5}" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" letter-spacing="1" fill="#CDE8D3">MAKER</text>']
    if one_percent:
        out.append(f'<g transform="translate({w-14} -8)"><rect x="0" y="0" width="30" height="16" rx="8" fill="{ORANGE}"/>'
                   f'<text x="15" y="11.5" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="700" fill="#161616">1%</text></g>')
    return "".join(out)

def panel_svg():
    # README panel: bordered box, MAKER pill centred on top, three mini badges with names, small label
    W,H=720,250
    body=[f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{CARD}" stroke="{BORDER}"/>',
          f'<g transform="translate({W/2-48} 22)">{maker_pill()}</g>']
    cols=[120,360,600]
    for (key,title,desc,claimed),cx in zip(BADGES,cols):
        body.append(f'<rect x="{cx-70}" y="66" width="140" height="112" rx="8" fill="{TILE}" stroke="{BORDER}"/>')
        body.append(check_box(cx+46,74,18))
        body.append(f'<g transform="translate({cx-40} 76) scale(0.86)">{ICONS[key]()}</g>')
        body.append(f'<text x="{cx}" y="206" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="700" fill="{WHITE}">{title}</text>')
    body.append(f'<text x="{W-16}" y="{H-12}" text-anchor="end" font-family="{FONT}" font-size="11" fill="{GREY}">Base44 badges</text>')
    body.append(f'<text x="16" y="{H-12}" font-family="{FONT}" font-size="11" fill="{GREY}">app.base44.com/@indica</text>')
    return svg(W,H,"".join(body),"Base44 badges earned by Indica Independent Media","Maker, with the Maker DNA, AI Native and Automation Architect badges. Links to the Base44 profile.")

if __name__=="__main__":
    os.makedirs("out/icons",exist_ok=True); os.makedirs("out/cards",exist_ok=True)
    for key,title,desc,claimed in BADGES:
        open(f"out/icons/{key}.svg","w").write(icon_svg(key,title,desc))
        open(f"out/cards/{key}.svg","w").write(card_svg(key,title,desc,claimed))
    open("out/maker-pill.svg","w").write(svg(110,36,f'<g transform="translate(7 8)">{maker_pill()}</g>',"Base44 Maker","Maker tier on Base44, with the 1% mark."))
    open("out/base44-badges-panel.svg","w").write(panel_svg())
    print("written:",sorted(os.listdir("out")),sorted(os.listdir("out/icons")),sorted(os.listdir("out/cards")))
