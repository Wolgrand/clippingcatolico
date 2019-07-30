#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import datetime



def postar_fotos(media, captionText):
    #media = [{
            # 'type': 'photo',
            # 'file': 'Images/post-1.jpg',  # Path to the photo file.
            # },
            # {
            # 'type': 'photo',
            # 'file': 'Images/post-2.jpg',  # Path to the photo file.
            # },
            #  {
            # 'type': 'photo',
            # 'file': 'Images/post-3.jpg',  # Path to the photo file.
            # },
            #  {
            # 'type': 'photo',
            # 'file': 'Images/post-4.jpg',  # Path to the photo file.
            # },
            #  {
            # 'type': 'photo',
            # 'file': 'Images/post-5.jpg',  # Path to the photo file.
            # }]
   
        # {
        #    'type'     : 'video',
        #    'file'     : '/path/to/your/video.mp4', # Path to the video file.
        #    'thumbnail': '/path/to/your/thumbnail.jpg'
        # }
        
    
# Uploading a timeline album (aka carousel aka sidecar).

    if(len(media)>=2):
        ig = InstagramAPI("gaudiumexpress", "neto1234")
        ig.login()
        ig.uploadAlbum(media, caption=captionText)
    else:
        ig = InstagramAPI("gaudiumexpress", "neto1234")
        ig.login()
        ig.uploadPhoto('Images/post-1.jpg', caption=captionText)
        
