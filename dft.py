def dft_1(vals):    # preforms dft on an input list -- vals -- as well as corresponding frequency (including negative ones)
	transformed=[]
	coeff=0
	N=len(vals)
	if N % 2==0:
		for k in range(int((-N/2) +1),int(N/2 +1)):
			coeff=0
			for n in range(0,N):
				coeff+=(vals[n]*(np.exp(-2*np.pi*1j*k*n*1/N)))
			transformed.append([coeff,k])
	else:
		for k in range(int(-(N-1)/2),int((N-1)/2)):
			for n in range(0,N):
				coeff+=(vals[n]*(np.exp(-2*np.pi*1j*k*n*1/N)))
			transformed.append([coeff,k])
	return transformed


