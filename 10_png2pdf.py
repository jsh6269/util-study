from PIL import Image

# img1로 pdf 생성
img1 = Image.open('sample/five.png').convert('RGB')
img1.save('sample/five.pdf')

img2 = Image.open('sample/dasigeum.png').convert('RGB')

# img1, img2, img2 순서로 병합된 pdf가 생성됨
img1.save('sample/combined.pdf', save_all=True, append_images=[img2, img2])

