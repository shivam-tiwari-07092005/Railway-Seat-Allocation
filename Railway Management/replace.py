def fifo(pages, frame_size):
    frames =[]
    page_fault = 0
    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_fault += 1
        print(f"Frames: {frames}")
    return page_fault

def optimal(pages, frame_size):
    frames = []
    page_fault = 0
    for i in range(len(pages)):
        page = pages[i]
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                future_use = []
                for frame in frames:
                    if frame in pages[i + 1::]:
                        future_use.append(pages[i + 1:].index(frame))
                    else:
                        future_use.append(float('inf'))
                frames.pop(future_use.index(max(future_use)))
                frames.append(page)
            page_fault += 1
        print(f"Frames: {frames}")
    return page_fault

def lru(pages, frame_size):
    frames = []
    page_fault = 0
    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_fault += 1
        else:
            frames.remove(page)
            frames.append(page)
        print(f"Frames = {frames}")
    return page_fault

pages = [1, 3, 0, 3, 5, 6, 3]
frame_size = 3
print(f"FIFO page faults: {fifo(pages, frame_size)}")
print(f"Optimal page faults: {optimal(pages, frame_size)}")
print(f"LRU page faults: {lru(pages, frame_size)}")