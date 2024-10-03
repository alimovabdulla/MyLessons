#Python'da şərt operatorları aşağıda verilmişdir. Bu operatorlar, şərti ifadələr yaratmaq və qiymətləndirmək üçün istifadə olunur.

# 1. if
# Şərt doğru olduqda icra ediləcək kod bloku.
if şərt:
    # icra ediləcək kod

# 2. elif
# İlk if şərti doğru olmadıqda əlavə şərtləri yoxlayır.
elif şərt:
    # icra ediləcək kod

# 3. else
# Əgər əvvəlki if və elif şərtləri doğru deyilsə, icra ediləcək kod.
else:
    # icra ediləcək kod

# 4. and
# İki və ya daha çox şərtin eyni anda doğru olub olmadığını yoxlayır.
if şərt1 and şərt2:
    # icra ediləcək kod

# 5. or
# İki və ya daha çox şərtdən ən azı birinin doğru olub olmadığını yoxlayır.
if şərt1 or şərt2:
    # icra ediləcək kod

# 6. not
# Şərtin əksini qiymətləndirir; əgər şərt doğru olarsa, False, əks halda True.
if not şərt:
    # icra ediləcək kod

# 7. in
# Bir elementin kolleksiyada (siyahı, tuple və s.) olub-olmadığını yoxlayır.
if element in kolleksiya:
    # icra ediləcək kod

# 8. is
# İki obyektin eyni olub olmadığını yoxlayır (obyekt identifikasiyası).
if obyekt1 is obyekt2:
    # icra ediləcək kod
