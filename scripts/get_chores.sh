#!/bin/bash

export PICTURES_DIRECTORY="pictures"
export LAYOUT_DIRECTORY="$PICTURES_DIRECTORY/layout"
export CHORES_DIRECTORY="$PICTURES_DIRECTORY/chores"
export LAYOUT="1x4"
export CROP_OVERLAP="-30-30"

# Function to create the main directories for chores functionnality
init_chores () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	for directory in $PICTURES_DIRECTORY $LAYOUT_DIRECTORY $CHORES_DIRECTORY
	do
		if [ ! -d $directory ]
        	then
                	mkdir $directory
		fi
	done
	echo -e "-------   END   -------\n"
}

# Function to remove the extracted chores from all pictures.
reset_chores () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	if [ -d $PICTURES_DIRECTORY ]
        then
                rm -rf $PICTURES_DIRECTORY
        fi
	echo -e "-------   END   -------\n"
}

# Extract pictures from PDF
extract_pictures () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	pdfimages -f 9 -l 33 -j 300-accords-de-piano-guide-et-dictionnaire-2015.pdf $PICTURES_DIRECTORY"/"
	echo -e "-------   END   -------\n"
}

# Function to get layouts from pictures
get_layouts_from_pictures () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	for file in $PICTURES_DIRECTORY/*.jpg
	do
		filename=$(basename -- "$file")
		filename="${filename%.*}"
		filename="${filename#"-"}"
		convert $file -crop $LAYOUT@ +repage +adjoin $LAYOUT_DIRECTORY"/"$filename"_"%d.jpg
	done
	echo -e "-------   END   -------\n"
}

# Function to split pictures (get chores pictures).
get_chores_from_pictures () {
	echo -e "\n---- ${FUNCNAME[0]}  ----"
	# Trim overlaps
	for file in $LAYOUT_DIRECTORY/*.jpg
	do
		convert $file -trim +repage $file
	done

	# Split and crop the raw picture
	for file in $LAYOUT_DIRECTORY/*.jpg
        do
		filename=$(basename -- "$file")
		filename="${filename%.*}"
                convert $file -crop 3x1-30-30@\! +repage +adjoin $CHORES_DIRECTORY"/chores_"$filename"_"%d.jpg
        done
	echo -e "-------   END   -------\n"
}

# Function to get all chores pictures.
get_chores () {
	init_chores
	extract_pictures
	get_layouts_from_pictures
	get_chores_from_pictures
}

