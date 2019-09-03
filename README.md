# piano-training

## Extract pictures from PDF

```bash
pdfimages -f 1 -l 33 -j 300-accords-de-piano-guide-et-dictionnaire-2015.pdf pictures/
```

## Split a picture to get the whole chores

```bash
convert -013.jpg -crop 3x4@  +repage  +adjoin  card_%d.jpg
```

## Divers

```bash
axel@axel-UX303LA[00:46:39]:~/Desktop/projects/piano-training/scripts$ namef="-toto.txt"
axel@axel-UX303LA[00:48:07]:~/Desktop/projects/piano-training/scripts$ mv -- $namef ${namef#"-"}
```
