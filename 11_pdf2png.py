import fitz

# pdf의 0번째, 1번째 페이지를 이미지 파일로 저장
doc = fitz.open('sample/combined.pdf')
wanted = [0, 1]
for i, page in enumerate(doc):
    if i in wanted:
        img = page.get_pixmap()
        img.save(f"sample/res_{i}.png")