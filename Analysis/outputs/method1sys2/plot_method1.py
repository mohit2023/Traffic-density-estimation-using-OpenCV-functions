import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def main():
	base_f = "1_out_method1.csv"
	baseline = np.array(pd.read_csv(base_f,header = None))
	q = []
	d = []
	x = []
	t = []
	for i in range(1, 9):
		s=3*(i-1)-1
		if(s==-1):
			s=0
		out_file = str(s+1) + "_out_method1.csv"
		output = np.array(pd.read_csv(out_file,header = None))
		queue_error = 0.0
		dynamic_error = 0.0
		for j in range(len(output)):
			queue = baseline[j][1] - output[j][1]
			queue=queue*queue
			dynamic = baseline[j][2] - output[j][2]
			dynamic=dynamic*dynamic
			queue_error = queue_error+queue
			dynamic_error = dynamic_error+dynamic
		queue_error = queue_error/len(output)
		dynamic_error = dynamic_error/len(output)
		x.append(s+1)
		q.append(queue_error)
		d.append(dynamic_error)
	runtime_file = "runtime_method1.csv"
	runtime = np.array(pd.read_csv(runtime_file,header=None))
	for time in runtime:
		t.append(time[1])
	plt.figure()
	plt.xlabel("Number of frames skipped")
	plt.ylabel("Avgerage squared error")
	plt.plot(x,q,label="Queue Density error")
	plt.plot(x,d,label="Dynamic Density error")
	plt.legend()
	plt.savefig("plot1.png",dpi=200)
	plt.show()
	
	plt.figure()
	plt.xlabel("Number of frames skipped")
	plt.ylabel("Runtime(seconds)")
	plt.plot(x,t)
	plt.savefig("plot2.png",dpi=200)
	plt.show()
	
	out_file1 = str(1) + "_out_method1.csv"
	output1 = np.array(pd.read_csv(out_file1,header = None))
	out_file6 = str(6) + "_out_method1.csv"
	output6 = np.array(pd.read_csv(out_file6,header = None))
	out_file15 = str(15) + "_out_method1.csv"
	output15 = np.array(pd.read_csv(out_file15,header = None))
	xax,yax1,yax2,yax3 = [],[],[],[]
	for i in range (len(output1)):
		xax.append(output1[i][0])
		yax1.append(output1[i][2])
		yax2.append(output6[i][2])
		yax3.append(output15[i][2])
	plt.figure()
	plt.xlabel("Frame number")
	plt.ylabel("Dynamic density")
	plt.plot(xax,yax1,label="Dynamic density when 0 frames skipped")
	plt.plot(xax,yax2,label="Dynamic density when 5 frames skipped")
	plt.plot(xax,yax3,label="Dynamic density when 14 frames skipped")
	plt.legend()
	plt.savefig("plot3.png",dpi=200)
	plt.show()
	
	q = list(map(lambda x:100.0/(1.0+x),q))
	d = list(map(lambda x:100.0/(1.0+x),d))
	plt.figure()
	plt.xlabel("Number of frames skipped")
	plt.ylabel("Utility Percentage")
	plt.plot(x,q,label="Queue Density utility percentage")
	plt.plot(x,d,label="Dynamic Density utility percentage")
	plt.legend()
	plt.savefig("plot4.png",dpi=200)
	plt.show()
	
	plt.figure()
	plt.xlabel("Runtime (seconds)")
	plt.ylabel("Utility Percentage")
	plt.plot(t,q,label="Queue Density utility percentage")
	plt.plot(t,d,label="Dynamic Density utility percentage")
	plt.legend()
	plt.savefig("plot5.png",dpi=200)
	plt.show()
	

if __name__ == "__main__":
	main()
