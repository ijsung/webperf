for b in bullet mibench parboil parsec sdvbs spec2000 spec2006
do
  sed s/templatesuitename/$b/ template.htm > $b.htm
done
