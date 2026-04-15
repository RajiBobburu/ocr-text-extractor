from PIL import ImageDraw

def extract_text(results, min_conf=30):
    filtered = [(bbox, text, conf) for bbox, text, conf in results if conf * 100 >= min_conf]

    full_text = "\n".join([text for _, text, _ in filtered])

    stats = {
        "words": len(full_text.split()),
        "chars": len(full_text),
        "segments": len(filtered),
        "avg_conf": round(sum(c for _, _, c in filtered) / len(filtered) * 100, 1) if filtered else 0
    }

    return full_text, filtered, stats


def draw_boxes(image, results, min_conf=30):
    draw = ImageDraw.Draw(image)

    for bbox, text, conf in results:
        if conf * 100 >= min_conf:
            points = [tuple(point) for point in bbox]
            draw.polygon(points, outline="red", width=2)

    return image