# Image Generation From Captions

This Zip file contains code for Image Generation using text captions implemented from the paper Reed et al. This network has been trained on flower images and captions from Oxford 102 flowers data. 

It has achieved pretty good generation of images form text captions. 
sample_captions.txt has 3 sentences

* this flower has yellow and purple petals with orange center
* this flower has purple petals with red center
* this flower is yellow with black center

these sentences when fed to the network generated the val_samples and 3 videos
<description\>.avi
Progress of the network was satisfactory. It was trained for 255 epochs with a learning rate of 0.0003.

In the original paper, 600 epochs were used while training. Code can be seen in the IGFT.html file and supporting libraries are individual python files.
Source code was derived from 3 GitHub repos. Although the training, model and generation functions are customized for this use case.

