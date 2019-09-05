#!/bin/bash

export PICTURES_DIRECTORY="pictures"
export LAYOUT_DIRECTORY="$PICTURES_DIRECTORY/layout"
export CHORES_DIRECTORY="$PICTURES_DIRECTORY/chores"
export LAYOUT="1x4"
export CROP_OVERLAP="-30-30"

init_chores () {
	for directory in $PICTURES_DIRECTORY $LAYOUT_DIRECTORY $CHORES_DIRECTORY
	do
		if [ ! -d $directory ]
        	then
                	mkdir $directory
		fi
	done
}

# Function to remove the extracted chores from all pictures.
reset_chores () {
	echo "------------------"
	echo $(pwd)

	if [ -d $PICTURES_DIRECTORY ]
        then
                rm -rf $PICTURES_DIRECTORY
        fi
}

# Extract pictures from PDF
extract_pictures () {
	pdfimages -f 9 -l 33 -j 300-accords-de-piano-guide-et-dictionnaire-2015.pdf $PICTURES_DIRECTORY
}

# Function to get layouts from pictures
get_layouts_from_pictures () {
	for file in *.jpg
	do
		filename="${file%.*}"
		filename="${filename#"-"}"
		convert $file -crop $LAYOUT@ +repage +adjoin $LAYOUT_DIRECTORY"/"$filename_%d.jpg
	done
}

# Function to split pictures (get chores pictures).
get_chores_from_pictures () {
	# Trim overlaps
	for file in $LAYOUT_DIRECTORY/*.jpg
	do
		convert $LAYOUT_DIRECTORY/$file -trim +repage $LAYOUT_DIRECTORY/$file
	done

	# Split and crop the raw picture
	for file in $LAYOUT_DIRECTORY/*.jpg
        do
		filename="${file%.*}"
                convert $LAYOUT_DIRECTORY/$file -crop 3x1-30-30@\! +repage +adjoin $CHORES_DIRECTORY/$filename"_chores_"%d.jpg
        done
}

# Function to get all chores pictures.
get_chores () {
	init_chores
	extract_picture
	get_layouts_from_pictures
	get_chores_from_pictures
}

