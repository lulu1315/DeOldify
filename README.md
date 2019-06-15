# this is a simplified version of DeOldify that I modified to be used as a cli.

```console
usage : python3 ImageColorizer.py model render_factor input_image output_image
```

model is an integer :
* 0 : video
* 1 : artistic
* 2 : stable

to generate a video , I usually extract a sequence of .png to a folder , than process each frame and reencode the result sequence with ffmpeg.

```console
#!/bin/bash
start=550
end=650
for i in `seq $start $end`;
    do
    ii=$(printf "%05d" $i)
        echo $ii
        python3 ImageColorizer.py 0 21 originals/ima.$ii.png deoldify/ima.$ii.png
    done 
```

