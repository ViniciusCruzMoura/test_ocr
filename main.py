"""
import easyocr

reader = easyocr.Reader(['pt'], gpu=True)

#resultados = reader.readtext('https://media.smooch.io/apps/600f2a17ea7d03000c058d41/conversations/bea2a54e0c760b907c3b8f4f/xVyoRn0BNDaw1D11qjk-XBcd/uyBHJHAYJtjNgm2ixhEvwDr2.jpeg', detail = 0)
#resultados = reader.readtext('https://jeroen.github.io/images/testocr.png', detail = 0)
resultados = reader.readtext('https://jeroen.github.io/images/testocr.png', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://www.mattmahoney.net/ocr/stock_gs200.jpg', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://www.iri.com/blog/wp-content/uploads/2021/12/darkshield-ocr-image-preprocessing-final-skewed-result.png', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://awardspersonalization.org/portals/0/images/magazine/insight-images/June21_Figure%20C%20-%20a%20fireplace%20document.jpg', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://media.smooch.io/apps/600f2a17ea7d03000c058d41/conversations/d6b6f2bcb4a7ed8a71c98ce9/8NXQuloWEfh6n2ZcC6_1w-lz/rVDCLPH6T7SMwn8ncevU3wYU.jpeg', detail = 0)
for resultado in resultados:
    print(resultado)
"""

"""
import threading

import easyocr

LEITOR = easyocr.Reader(['pt'], gpu=True)


def ocerizar(url):
    global LEITOR
    print(LEITOR.readtext(url, detail=0))
    return 1


if __name__ == '__main__':
    vurl = "https://raw.githubusercontent.com/JaidedAI/EasyOCR/master/examples/example.png"
    for i in range(1, 29):
        threading.Thread(target=ocerizar, kwargs={'url': vurl}, daemon=False).start()
"""

"""
import threading

import easyocr

LEITOR = easyocr.Reader(['pt'], gpu=True)

def ocerizar(url):
    global LEITOR
    print("GPU_OCR - ", LEITOR.readtext(url, detail=0))
    return 1

LEITOR_CPU = easyocr.Reader(['pt'], gpu=False)
def ocerizar_cpu(url):
    global LEITOR_CPU
    print("CPU_OCR - ", LEITOR_CPU.readtext(url, detail=0))
    return 1

if __name__ == '__main__':
    vurl = "https://raw.githubusercontent.com/JaidedAI/EasyOCR/master/examples/example.png"
    for i in range(1, 300):
        if i % 2 == 1: #i > 27:
            print("CPU THREAD - ", i)
            threading.Thread(target=ocerizar_cpu, kwargs={'url': vurl}, daemon=False).start()
            #continue
        else:
            print("GPU THREAD - ", i)
            threading.Thread(target=ocerizar, kwargs={'url': vurl}, daemon=False).start()
"""

"""
import threading
import easyocr

LEITOR_GPU = easyocr.Reader(['pt'], gpu=True)
LEITOR_CPU = easyocr.Reader(['pt'], gpu=True)

def get_gpu_memory():
    import subprocess as sp
    import os
    command = "nvidia-smi --query-gpu=memory.free --format=csv"
    memory_free_info = sp.check_output(command.split()).decode('ascii').split('\n')[:-1][1:]
    memory_free_values = [int(x.split()[0]) for i, x in enumerate(memory_free_info)]
    return memory_free_values[0]

def ocerizar(url):
    global LEITOR_GPU
    global LEITOR_CPU
    print("VRAM: ", get_gpu_memory())
    if threading.active_count() != -1:
        return 0
    if get_gpu_memory() < 2000 or (threading.active_count() >= 5 and threading.active_count() <= 20):
        #print("CPU_OCR - ", LEITOR_CPU.readtext(url, detail=0))
        #return LEITOR_CPU.readtext(url, detail=0)
        print("CPU_OCR")
    elif threading.active_count() < 5:
        #print("GPU_OCR - ", LEITOR_GPU.readtext(url, detail=0))
        #return LEITOR_GPU.readtext(url, detail=0)
        print("GPU_OCR")
    return 1

if __name__ == '__main__':
    #vurl = "https://raw.githubusercontent.com/JaidedAI/EasyOCR/master/examples/example.png"
    vurl = "https://media.smooch.io/apps/600f2a17ea7d03000c058d41/conversations/d6b6f2bcb4a7ed8a71c98ce9/8NXQuloWEfh6n2ZcC6_1w-lz/rVDCLPH6T7SMwn8ncevU3wYU.jpeg"
    #print(ocerizar(vurl))
    for i in range(1, 100):
        threading.Thread(target=ocerizar, kwargs={'url': vurl}, daemon=False).start()
"""
