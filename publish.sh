

TARGET=mc.admalledd.com:/var/www/
#TARGET=/home/admalledd/Documents/notes/www
SRC=/home/admalledd/Documents/notes/pelican_test/output

HOMEWWW=/home/admalledd/www
ln -s $HOMEWWW/dl/ $SRC/dl
ln -s $HOMEWWW/mc/ $SRC/mc
ln -s $HOMEWWW/favicon.ico $SRC/
cp $SRC/../htaccess $SRC/.htaccess

rsync -avz --del $SRC/ $TARGET/

#ln -s $TARGET/pages/mc-index.html $TARGET/mc/index.html

