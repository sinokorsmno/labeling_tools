import tkinter as tk
from pycocotools.coco import COCO
from PIL import Image, ImageTk

# COCO 데이터셋 경로와 파일명 설정
dataDir = './test'
dataType = 'test'
annFile = './annotation/_annotations.coco.test.json'
imageDir = 'test'

# COCO 데이터셋 로드
coco = COCO(annFile)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("COCO Dataset Viewer")

####### 여기서 부터는 PycocoTool 적용 하여 그림
def show_image(image_id):
    img_info = coco.loadImgs(image_id)[0]
    image = Image.open(f'{imageDir}/{img_info["file_name"]}')
    tk_image = ImageTk.PhotoImage(image)
    print("file_name : ", img_info["file_name"])

    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    canvas.image = tk_image

    ann_ids = coco.getAnnIds(imgIds=image_id)
    annotations = coco.loadAnns(ann_ids)

    for annotation in annotations:
        bbox = annotation['bbox']
        x, y, w, h = bbox
        canvas.create_rectangle(x, y, x + w, y + h, outline="red", width=2)

# 이미지 표시 Canvas 생성
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# 이미지 목록을 가져와서 첫 번째 이미지 표시
image_ids = coco.getImgIds()
current_image_index = 0
show_image(image_ids[current_image_index])

# 이전 이미지로 이동하는 함수
def prev_image():
    global current_image_index
    if current_image_index > 0:
        current_image_index -= 1
        show_image(image_ids[current_image_index])

# 다음 이미지로 이동하는 함수
def next_image():
    global current_image_index
    if current_image_index < len(image_ids) - 1:
        current_image_index += 1
        show_image(image_ids[current_image_index])

# "이전" 및 "다음" 버튼 추가
prev_button = tk.Button(window, text="이전", command=prev_image)
next_button = tk.Button(window, text="다음", command=next_image)
prev_button.pack()
next_button.pack()

# Tkinter 메인 루프 실행
window.mainloop()