
echo "publishing files to the site..."



TARGET=mc.admalledd.com:/var/www/
#TARGET=/home/admalledd/Documents/notes/www
SRC=/home/admalledd/Documents/notes/pelican_test/output

echo "first, clean and regenerate the output files"
make clean
make html

echo "now setting up symlinks"
#relative to the DESTINATION/PRODUCTION server
HOMEWWW=/home/admalledd/www
#custom downloads
ln -s $HOMEWWW/dl/ $SRC/dl
#custom minecraft stuffs (map render ect)
ln -s $HOMEWWW/mc/ $SRC/mc
#favicon
ln -s $HOMEWWW/favicon.ico $SRC/
#php stuffs, eg forum.
ln -s $HOMEWWW/php/ $SRC/php

cp $SRC/../htaccess $SRC/.htaccess
echo "transferring files..."
rsync -avz --del $SRC/ $TARGET/

#ln -s $TARGET/pages/mc-index.html $TARGET/mc/index.html

