# SCAV_Sem3
Last Seminar of the SCAV 2020 subject. 

The objective of this last seminar was to implement python scripts able to create videos with different codecs and compare them to observe the differences a user could percieve if we use one or other.
Also something very interesant task we where asked to do is to implement a little streaming algorithm able to reproduce the video we want giving the ip adress of the destination in our algorithm (Due to lack of time i didn't finish this part). 

In the Project you could find three different .py files, each of them computing some specific task. 

The fist one 'video_conv' is the one dedicated to change the video codecs of the cuts obtained from Lab 2, and used av1, vp8, vp9 and h265 codecs with .mp4, .webm, .webm and .mkv extensions respectevly. In order to have this new videos collected in some specific site, we create different folders where we will store the different codecs videos. 

Once we did that, we will now create a new video allocating 4 videos with the same scale (in our case 360x240) but different codecs, to be able to compare the results we obtain using one codec or other. From this video we can assure that the videos that use vp8 and vp9 codecs are the ones with lowe quality, while the one with the av1 codec is the best in terms of quality (subjective opìnion), but the video with the h265 codec has lower bitrate.

Finally the streaming file is not complete, as we previously said, the object was to create a script able to stream a video providing the ip direction of the source device (this should be located at the same network as us). Using the VLC program, once we computed the script, the idea was to introduce the line 'upd://@:1234' in this program in the network part of VLC (media->open_neteork_ubication->network). Unfortynetly we didn't make this work. 
