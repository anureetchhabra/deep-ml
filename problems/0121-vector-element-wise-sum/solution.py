def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	lena = len(a)
	lenb= len(b)
	if lena !=lenb:
		return -1
	else:
		for i in range (lenb):
			a[i]=a[i]+b[i]
		return a
