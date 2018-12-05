from matplotlib import pyplot as plt

def freq_plot(arb_ids, arb_freq, xlabel, ylabel):
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.bar(arb_ids, arb_freq)
	plt.show()

def scrape_arbs():
	data = file.open("./canlog\\ 1532459824.29\\ parseable")
	

freq_plot([0x00, 0x01, 0x02, 0x03], [10, 20, 30, 40], 'Arbitration IDs', 'Number of Packets Received')