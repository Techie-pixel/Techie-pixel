import os

def build_row(title, items, y_offset, anim_class, color):
    # Terminal styled text rows
    row_xml = f"""
    <g class="{anim_class}" transform="translate(0, {y_offset})">
      <text y="0" font-weight="bold" fill="#e6edf3" font-size="15">&gt; {title}</text>
      <text y="25" fill="{color}" font-weight="bold">"""
    
    # Format items like: [ Java ]  [ HTML ]  ...
    text_items = "  ".join([f"[{item}]" for item in items])
    row_xml += text_items + "</text>\n    </g>"
    return row_xml

base_css = """
      .bg { fill: #0d1117; rx: 12px; stroke: #30363d; stroke-width: 1.5px; }
      .header { fill: #161b22; }
      .text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 15px; fill: #8b949e; }
      .glow-green { fill: #39ff14; filter: drop-shadow(0 0 3px rgba(57,255,20,0.8)); font-weight: bold; }
      .glow-blue { fill: #58a6ff; font-weight: bold; }
      .prompt { fill: #79c0ff; font-weight: bold; font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
      .path { fill: #ff7b72; font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
      .cmd { fill: #d2a8ff; font-weight: bold; font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
      
      .t1 { animation: t1 18s infinite; clip-path: inset(0 100% 0 0); white-space:nowrap; overflow:hidden; }
      .p1 { animation: p1 18s infinite; opacity: 0; }
      .succ { animation: succ 18s infinite; opacity: 0; }
      .row1 { animation: row1 18s infinite; opacity: 0; }
      .row2 { animation: row2 18s infinite; opacity: 0; }
      .row3 { animation: row3 18s infinite; opacity: 0; }
      .row4 { animation: row4 18s infinite; opacity: 0; }
      .cursor { animation: blink 1s step-end infinite, cursorShow 18s infinite; opacity: 0; }
      
      @keyframes t1 { 0%,1% { clip-path: inset(0 100% 0 0); } 8%,95% { clip-path: inset(0 0 0 0); } 100% { clip-path: inset(0 100% 0 0); } }
      @keyframes p1 { 0%,15% { opacity: 0; } 16%,95% { opacity: 1; } 100% { opacity: 0; } }
      @keyframes succ { 0%,22% { opacity: 0; } 23%,95% { opacity: 1; } 100% { opacity: 0; } }
      
      @keyframes row1 { 0%,26% { opacity: 0; transform: translate(0, 235px); } 28%,95% { opacity: 1; transform: translate(0, 230px); } 100% { opacity: 0; transform: translate(0, 230px);} }
      @keyframes row2 { 0%,30% { opacity: 0; transform: translate(0, 295px); } 32%,95% { opacity: 1; transform: translate(0, 290px); } 100% { opacity: 0; transform: translate(0, 290px);} }
      @keyframes row3 { 0%,34% { opacity: 0; transform: translate(0, 355px); } 36%,95% { opacity: 1; transform: translate(0, 350px); } 100% { opacity: 0; transform: translate(0, 350px);} }
      @keyframes row4 { 0%,38% { opacity: 0; transform: translate(0, 415px); } 40%,95% { opacity: 1; transform: translate(0, 410px); } 100% { opacity: 0; transform: translate(0, 410px);} }
      
      @keyframes cursorShow { 0%,41% { opacity: 0; } 43%,95% { opacity: 1; } 100% { opacity: 0; } }
      @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
"""

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 510" width="100%" height="510">
  <defs>
    <style>
{base_css}
    </style>
  </defs>
  <rect class="bg" width="850" height="510" />
  <path class="header" d="M0 12 Q 0 0 12 0 L 838 0 Q 850 0 850 12 L 850 35 L 0 35 Z" />
  <circle fill="#ff5f56" cx="20" cy="18" r="6" />
  <circle fill="#ffbd2e" cx="40" cy="18" r="6" />
  <circle fill="#27c93f" cx="60" cy="18" r="6" />
  <text x="360" y="23" font-family="monospace" fill="#8b949e" font-size="13">java@aditya-engine: ~</text>

  <g class="text" transform="translate(20, 70)">
    <g class="t1">
      <text y="0"><tspan class="prompt">aditya@dev</tspan>:<tspan class="path">~/desktop</tspan>$ <tspan class="cmd">java TechStack.class --display</tspan></text>
    </g>
    <g class="p1">
      <text y="35" class="glow-blue" font-weight="bold" xml:space="preserve">    ████████╗███████╗ ██████╗██╗  ██╗    ███████╗████████╗</text>
      <text y="60" class="glow-blue" font-weight="bold" xml:space="preserve">    ╚══██╔══╝██╔════╝██╔════╝██║  ██║    ██╔════╝╚══██╔══╝</text>
      <text y="85" class="glow-blue" font-weight="bold" xml:space="preserve">       ██║   █████╗  ██║     ███████║    ███████╗   ██║   </text>
      <text y="110" class="glow-blue" font-weight="bold" xml:space="preserve">       ██║   ██╔══╝  ██║     ██╔══██║    ╚════██║   ██║   </text>
      <text y="135" class="glow-blue" font-weight="bold" xml:space="preserve">       ██║   ███████╗╚██████╗██║  ██║    ███████║   ██║   </text>
      <text y="160" class="glow-blue" font-weight="bold" xml:space="preserve">       ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚══════╝   ╚═╝   </text>
    </g>
    <g class="succ">
      <text y="195">[<tspan class="glow-green">SUCCESS</tspan>] Libraries loaded.</text>
    </g>
    
{build_row("Languages &amp; Core", ["Java", "C", "JavaScript", "HTML5", "CSS", "XML"], 230, "row1", "#ffa500")}
{build_row("Mobile Development", ["Android", "Android Studio", "Gradle"], 290, "row2", "#3fb950")}
{build_row("Backend &amp; Databases", ["Firebase", "Firestore", "MySQL", "Apache"], 350, "row3", "#ff7b72")}
{build_row("Tools &amp; Platforms", ["GitHub", "Vercel", "VS Code", "Figma"], 410, "row4", "#d2a8ff")}
    
    <g class="cursor">
       <text y="465"><tspan class="prompt">aditya@dev</tspan>:<tspan class="path">~/desktop</tspan>$ <tspan class="glow-green">█</tspan></text>
    </g>
  </g>
</svg>"""

with open("assets/terminal-tech.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
