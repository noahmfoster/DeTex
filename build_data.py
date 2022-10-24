from gen_images import gen_image
from MathScraping import get_equations, walk_pages
import re


links = walk_pages(alphabet='G')[110:200]
pages = [(get_equations(link)) for link in links]

for page in pages:
    if len(page) > 0:
        for i, equation in enumerate(page[1]):
            if len(equation) > 4:
                page_title_num = re.sub(r'\W+', '', page[0][:-12] + str(i))
                gen_image(equation, page_title_num)