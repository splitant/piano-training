#!/bin/bash

export PDF_CHORDS="resources/300-accords-de-piano-guide-et-dictionnaire-2015.pdf"
export PICTURES_DIRECTORY="../app/resources/pictures"
export LAYOUT_DIRECTORY="$PICTURES_DIRECTORY/layout"
export CHORDS_DIRECTORY="$PICTURES_DIRECTORY/chores"
export SIMPLE_CHORDS_DIRECTORY="$PICTURES_DIRECTORY/simple_chores"
export LAYOUT="1x4"
export CROP_OVERLAP="-30-30"

# Function to create the main directories for chords functionnality
init_chords () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	for directory in $PICTURES_DIRECTORY $LAYOUT_DIRECTORY $CHORDS_DIRECTORY
	do
		if [ ! -d $directory ]
        	then
                	mkdir $directory
		fi
	done
	echo -e "-------   END   -------\n"
}

# Function to remove the extracted chords from all pictures.
reset_chords () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	for directory in $LAYOUT_DIRECTORY $CHORDS_DIRECTORY
	do
		if [ -d $directory ]
        	then
                	rm -rf $directory
		fi
	done
	echo -e "-------   END   -------\n"
}

# Extract pictures from PDF
extract_pictures () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	pdfimages -png -f 9 -l 33 $PDF_CHORDS $PICTURES_DIRECTORY"/"
	echo -e "-------   END   -------\n"
}

# Function to get layouts from pictures
get_layouts_from_pictures () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	for file in $PICTURES_DIRECTORY/*.png
	do
		filename=$(basename -- "$file")
		filename="${filename%.*}"
		filename="${filename#"-"}"
		convert $file -crop $LAYOUT@ +repage +adjoin $LAYOUT_DIRECTORY"/"$filename"_"%d.png
	done
	echo -e "-------   END   -------\n"
}

# Function to split pictures (get chords pictures).
get_chords_from_pictures () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	# Trim overlaps
	for file in $LAYOUT_DIRECTORY/*.png
	do
		convert $file -trim +repage $file
	done

	# Split and crop the raw picture
	for file in $LAYOUT_DIRECTORY/*.png
	do
		filename=$(basename -- "$file")
		filename="${filename%.*}"
		convert $file -crop 3x1-30-30@\! +repage +adjoin $CHORDS_DIRECTORY"/chords_"$filename"_"%d.png
	done

	# Remove edge on each chords pictures
	for file in $CHORDS_DIRECTORY/*.png
	do
		convert $file -fuzz 30% -trim +repage $file
	done
	echo -e "-------   END   -------\n"

	cp $SIMPLE_CHORDS_DIRECTORY/* $CHORDS_DIRECTORY/
}

# Function to get all chords pictures.
get_chords () {
	init_chords
	extract_pictures
	get_layouts_from_pictures
	get_chords_from_pictures
}

get_chords
