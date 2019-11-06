# piano-training

## Extract pictures from PDF

```bash
pdfimages -f 9 -l 33 -j 300-accords-de-piano-guide-et-dictionnaire-2015.pdf pictures/
```

## Split a picture to get the whole chores

```bash
convert -013.jpg -crop 3x4@  +repage  +adjoin  013_chores_%d.jpg

# Step 1 : split picture in raw.
convert -013.jpg -crop 1x4@  +repage  +adjoin test_chores/013_chores_%d.jpg

# Step 2 : Trim white space
convert test_chores/013_chores_0.jpg -trim +repage test_chores/output_013_chores_0.jpg

# Step 3 : Split and crop the raw picture
convert test_chores/output_013_chores_0.jpg -crop 3x1-30-30@\!  +repage  +adjoin test_chores/output_2_013_chores_%d.jpg

```

## Divers

```bash
axel@axel-UX303LA[00:46:39]:~/Desktop/projects/piano-training/scripts$ namef="-toto.txt"
axel@axel-UX303LA[00:48:07]:~/Desktop/projects/piano-training/scripts$ mv -- $namef ${namef#"-"}
```
## Classes

ExtractChoresFromCSV
ChoresMode
MajorMinorChoresMode
AdvancedChoresMode
SettingsChores
