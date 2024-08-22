from jinja2 import Template
from PIL import Image
import base64
from io import BytesIO

def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_base64

def generate_html(image_base64, month, caption, philosophy, to):
    template = Template('''
<!DOCTYPE html>
<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

body {
    font-family: "MedievalSharp";
    background-color: #F8F0E3;
    user-select: none;
    overflow: hidden;
}

.content {
    display: flex;
    align-items: center;
    margin-top: 5%;
    justify-content: center;
    vertical-align: center;
}

.flip-card {
  background-color: transparent;
  width: 800px;
  height: 560px;
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(-180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 800px;
  height: 560px;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.flip-card-front {
  overflow: hidden;
  background-color: antiquewhite;
  color: black;
  img {
    width: 100%;
    height: auto;
    resize: both;
    object-fit: cover;
    object-position: center;
  }
}

.flip-card-back {
  background-color: antiquewhite;
  color: dark-grey;
  transform: rotateY(-180deg);
}

.stars {
  display: flex;
  align-items: center;
  justify-content: center;
}

.signature {
    display: flex;
    align-items: right;
    justify-content: right;
    padding: 0px 10% 0px 10%;
}

</style>
</head>
<body>

<div class="content">
    <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front">
            <img src="data:image/png;base64,{{ image_data }}" 
            alt="Avatar" style="width:840px;height:560px;">
          </div>
          <div class="flip-card-back">
            <h1 style="margin-top: 10%;">{{ month }}</h1> 
            <p>{{ caption }}</p> 
            <div class="stars">
                <svg fill="#000000" width="24px" height="25px" viewBox="0 0 24 24" id="star" data-name="Flat Color" xmlns="http://www.w3.org/2000/svg" class="icon flat-color"><path id="primary" d="M22,9.81a1,1,0,0,0-.83-.69l-5.7-.78L12.88,3.53a1,1,0,0,0-1.76,0L8.57,8.34l-5.7.78a1,1,0,0,0-.82.69,1,1,0,0,0,.28,1l4.09,3.73-1,5.24A1,1,0,0,0,6.88,20.9L12,18.38l5.12,2.52a1,1,0,0,0,.44.1,1,1,0,0,0,1-1.18l-1-5.24,4.09-3.73A1,1,0,0,0,22,9.81Z" style="fill: rgb(0, 0, 0);"></path></svg>
                <svg fill="#000000" width="24px" height="25px" viewBox="0 0 24 24" id="star" data-name="Flat Color" xmlns="http://www.w3.org/2000/svg" class="icon flat-color"><path id="primary" d="M22,9.81a1,1,0,0,0-.83-.69l-5.7-.78L12.88,3.53a1,1,0,0,0-1.76,0L8.57,8.34l-5.7.78a1,1,0,0,0-.82.69,1,1,0,0,0,.28,1l4.09,3.73-1,5.24A1,1,0,0,0,6.88,20.9L12,18.38l5.12,2.52a1,1,0,0,0,.44.1,1,1,0,0,0,1-1.18l-1-5.24,4.09-3.73A1,1,0,0,0,22,9.81Z" style="fill: rgb(0, 0, 0);"></path></svg>
                <svg fill="#000000" width="24px" height="25px" viewBox="0 0 24 24" id="star" data-name="Flat Color" xmlns="http://www.w3.org/2000/svg" class="icon flat-color"><path id="primary" d="M22,9.81a1,1,0,0,0-.83-.69l-5.7-.78L12.88,3.53a1,1,0,0,0-1.76,0L8.57,8.34l-5.7.78a1,1,0,0,0-.82.69,1,1,0,0,0,.28,1l4.09,3.73-1,5.24A1,1,0,0,0,6.88,20.9L12,18.38l5.12,2.52a1,1,0,0,0,.44.1,1,1,0,0,0,1-1.18l-1-5.24,4.09-3.73A1,1,0,0,0,22,9.81Z" style="fill: rgb(0, 0, 0);"></path></svg>
                <svg fill="#000000" width="24px" height="25px" viewBox="0 0 24 24" id="star" data-name="Flat Color" xmlns="http://www.w3.org/2000/svg" class="icon flat-color"><path id="primary" d="M22,9.81a1,1,0,0,0-.83-.69l-5.7-.78L12.88,3.53a1,1,0,0,0-1.76,0L8.57,8.34l-5.7.78a1,1,0,0,0-.82.69,1,1,0,0,0,.28,1l4.09,3.73-1,5.24A1,1,0,0,0,6.88,20.9L12,18.38l5.12,2.52a1,1,0,0,0,.44.1,1,1,0,0,0,1-1.18l-1-5.24,4.09-3.73A1,1,0,0,0,22,9.81Z" style="fill: rgb(0, 0, 0);"></path></svg>
                <svg fill="#000000" width="24px" height="25px" viewBox="0 0 24 24" id="star" data-name="Flat Color" xmlns="http://www.w3.org/2000/svg" class="icon flat-color"><path id="primary" d="M22,9.81a1,1,0,0,0-.83-.69l-5.7-.78L12.88,3.53a1,1,0,0,0-1.76,0L8.57,8.34l-5.7.78a1,1,0,0,0-.82.69,1,1,0,0,0,.28,1l4.09,3.73-1,5.24A1,1,0,0,0,6.88,20.9L12,18.38l5.12,2.52a1,1,0,0,0,.44.1,1,1,0,0,0,1-1.18l-1-5.24,4.09-3.73A1,1,0,0,0,22,9.81Z" style="fill: rgb(0, 0, 0);"></path></svg>
              </div>
            <p>{{ philosophy }}</p>
            <div class="signature">
                <h2>{{ to }}</h2>
            </div>
          </div>
        </div>
      </div>
</div> 


</body>
</html>
    ''')
    return template.render(image_data=image_base64, month=month, caption=caption, philosophy=philosophy, to=to)

image_path = input("Enter file path:")
image_base64 = image_to_base64(image_path)

month = input("Enter month:")
caption = input("Enter caption:")
philosophy = input("Enter philosophy:")
to = input("Enter reciever:")
name = input("Enter postcard name:")

html_content = generate_html(image_base64, month, caption, philosophy, to)

with open(name + ".html", "w") as html_file:
    html_file.write(html_content)

print("HTML file succesfully created!")