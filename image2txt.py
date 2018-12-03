# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:27:38 2018

@author: user
"""
from google.cloud import vision
from google.cloud.vision import types
client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'sss.jpg'
resp = client.document_text_detection(image=image)
print('\n'.join([d.description for d in resp.text_annotations]))


########################
import io
from google.cloud import vision
client = vision.ImageAnnotatorClient()
imageData = 'picture.png'
with io.open(imageData, 'rb') as image_file:
    content = image_file.read()
    texts =client.document_text_detection(imageData,content=content)
    print(texts[0].description)
    
#############################

from google.cloud.vision_v1 import ImageAnnotatorClient
client = ImageAnnotatorClient()
request = {
     'image': {
         'source': {'image_uri': 'https://foo.com/image.jpg'},
     },
 }
response = client.annotate_image(request)
###############  
#import requests 
#import base64
#
#file_name = '/sss.jpg'
#with open(file_name, 'r') as image:
#    image_content = image.read()
#    encoded_content = base64.b64encode(image_content)
#
#data = {
#  "requests":[
#    {
#      "image":{
#      "content": encoded_content
#    },
#  "features":[
#    {
#      "type":"DOCUMENT_TEXT_DETECTION",
#      "maxResults":1
#    }
#   ]
#  }
# ]
#}
#r = requests.post(url=url,json=data)
#x = json.loads(r.text)
#print(x['responses'])
#########################################################
def detect_text_uri(uri):
    
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
def run_uri(args):
    if args.command == 'text-uri':
        detect_text_uri(args.uri)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')
    args = parser.parse_args()

    if 'uri' in args.command:
        run_uri(args)
    else:
        run_local(args)