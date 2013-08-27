
echo "publishing files to the site..."



TARGET=mc.admalledd.com:/var/www/
#TARGET=/home/admalledd/Documents/notes/www
SRC=/home/admalledd/Documents/notes/pelican_test/output

echo "first, clean and regenerate the output files"
make clean
make html

echo "now setting up symlinks"
HOMEWWW=/home/admalledd/www
ln -s $HOMEWWW/dl/ $SRC/dl
ln -s $HOMEWWW/mc/ $SRC/mc
ln -s $HOMEWWW/favicon.ico $SRC/
cp $SRC/../htaccess $SRC/.htaccess
echo "transferring files..."
rsync -avz --del $SRC/ $TARGET/

#ln -s $TARGET/pages/mc-index.html $TARGET/mc/index.html

