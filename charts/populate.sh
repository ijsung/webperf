for b in all bullet mibench parboil parsec sdvbs spec2000 spec2006
do
  gm4 -Dtemplatesuitename=$b template.htm > $b.htm
done
