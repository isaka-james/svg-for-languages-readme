import random
import sys

def get_programming_languages():
    number_lang = int(input("How many programming languages do you know: "))

    if number_lang>15:
        print("\n\tOnly 15 programming languages are allowed for this version!!")
        sys.exit()

    all_languages = []
    for i in range(number_lang):
        lang = input("Language name: ")
        conf = float(input("Confidence Percent: "))
        all_languages.append({"name": lang, "confidence": conf})

    return all_languages

def assign_random_colors(languages_list, color_list):
    used_colors = set()
    for language_dict in languages_list:
        while True:
            random_color = random.choice(color_list)
            if random_color not in used_colors:
                used_colors.add(random_color)
                language_dict["color"] = random_color
                break
    return languages_list

color_list = [
    "#FF6347",  # Vivid Sunset Orange
    "#FFC0CB",  # Soft Blush Pink
    "#ADD8E6",  # Tranquil Light Blue
    "#90EE90",  # Serene Spring Green
    "#F0E68C",  # Warm Sunshine Yellow
    "#E0FFFF",  # Calming Sky Blue
    "#AFEEEE",  # Refreshing Mint Green
    "#D3959B",  # Delicate Lavender
    "#F4C2C2",  # Elegant Dusty Rose
    "#98FB98",  # Calming Seafoam Green
    "#FFA500",  # Energetic Orange
    "#800080",  # Deep Purple
    "#C71585",  # Bold Magenta
    "#00CED1",  # Soothing Turquoise
    "#FFFF00",  # Bright Yellow
    "#DC143C",  # Deep Crimson Red
    "#000000",  # Classic Black
    "#FFFFFF",  # Pure White
    "#A52A2A",  # Earthy Brown
    "#7FFFD4"   # Gentle Aqua Blue
]

header = input("Choose Your Header!\nDefault :: My Programming Languages' Confidence\n\tHeader: ")
if header=="":
    header="My Programming Languages' Confidence"


print("\n\n")
print(f"Header: {header}")
all_languages = get_programming_languages()

final_languages = assign_random_colors(all_languages, color_list)

sum=0.0

for lang in final_languages:
    sum+=lang["confidence"]

for overall in final_languages:
    overall["overall"]=(overall["confidence"]/sum)*100

progress = """"""
# The progress
for progress_lang in final_languages:
    progress+=f"""<span style="background-color: {progress_lang["color"]};width: {progress_lang["overall"]}%;" class="progress-item"></span>"""


each_full=""""""
init_num=0
# Each Language
for each_lang in final_languages:
    each_full+=f"""


<li style="animation-delay: {init_num}ms;">
<svg xmlns="http://www.w3.org/2000/svg" class="octicon" style="fill:{each_lang["color"]};" viewBox="0 0 16 16" version="1.1" width="16" height="16"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"/></svg>
<span class="lang">{each_lang["name"]}</span>
<span class="percent">{each_lang["confidence"]}%</span>
</li>


    """
    init_num+=150




svg = f"""
<svg id="gh-dark-mode-only" width="380" height="230" xmlns="http://www.w3.org/2000/svg">
<style>
svg {{
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji;
  font-size: 14px;
  line-height: 21px;
}}

#background {{
  width: calc(100% - 10px);
  height: calc(100% - 10px);
  fill: white;
  stroke: rgb(225, 228, 232);
  stroke-width: 1px;
  rx: 6px;
  ry: 6px;
}}

#gh-dark-mode-only:target #background {{
  fill: #0d1117;
  stroke-width: 0.5px;
}}

foreignObject {{
  width: calc(100% - 10px - 32px);
  height: calc(100% - 10px - 24px);
}}

h2 {{
  margin-top: 0;
  margin-bottom: 0.75em;
  line-height: 24px;
  font-size: 16px;
  font-weight: 600;
  color: rgb(36, 41, 46);
  fill: rgb(36, 41, 46);
}}

#gh-dark-mode-only:target h2 {{
  color: #c9d1d9;
  fill: #c9d1d9;
}}

ul {{
  list-style: none;
  padding-left: 0;
  margin-top: 0;
  margin-bottom: 0;
}}

li {{
  display: inline-flex;
  font-size: 12px;
  margin-right: 2ch;
  align-items: center;
  flex-wrap: nowrap;
  transform: translateX(-500%);
  animation: slideIn 2s ease-in-out forwards;
}}

@keyframes slideIn {{
  to {{
    transform: translateX(0);
  }}
}}

div.ellipsis {{
  height: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
}}

.octicon {{
  fill: rgb(88, 96, 105);
  margin-right: 0.5ch;
  vertical-align: top;
}}

#gh-dark-mode-only:target .octicon {{
  color: #8b949e;
  fill: #8b949e;
}}

.progress {{
  display: flex;
  height: 8px;
  overflow: hidden;
  background-color: rgb(225, 228, 232);
  border-radius: 6px;
  outline: 1px solid transparent;
  margin-bottom: 1em;
}}

#gh-dark-mode-only:target .progress {{
  background-color: rgba(110, 118, 129, 0.4);
}}

.progress-item {{
  outline: 2px solid rgb(225, 228, 232);
  border-collapse: collapse;
}}

#gh-dark-mode-only:target .progress-item {{
  outline: 2px solid #393f47;
}}

.lang {{
  font-weight: 600;
  margin-right: 4px;
  color: rgb(36, 41, 46);
}}

#gh-dark-mode-only:target .lang {{
  color: #c9d1d9;
}}

.percent {{
  color: rgb(88, 96, 105)
}}

#gh-dark-mode-only:target .percent {{
  color: #8b949e;
}}
</style>
<g>
<rect x="5" y="5" id="background"/>
<g>
<foreignObject x="21" y="17" width="318" height="176">
<div xmlns="http://www.w3.org/1999/xhtml" class="ellipsis">

<h2>{header}</h2>

<div>
<span class="progress">
{progress}
</span>
</div>

<ul>

{each_full}


</ul>

</div>
</foreignObject>
</g>
</g>
</svg>

"""


# Open the file in write mode ("w")
with open("lang.svg", "w") as file:
  # Write the first line
  file.write(svg)

print("done")

