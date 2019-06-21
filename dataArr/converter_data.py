# converting bulletin data for hypoDD

fileinput = 'station.txt'
fileoutput = 'stationout.pha'

file = open(fileinput,'r')
baris = file.readlines()
for i in range(len(baris)):
	baris[i]=baris[i].split()
file.close()
file = open(fileoutput,'w')

i = 0
event =0
while i < len(baris):
	if len(baris[i])>0 and baris[i][0]=='EventID:':
		event = event+1
		eventid = baris[i][1][3::]
		tahun = baris[i+2][0].split('-')[0]
		bulan = baris[i+2][0].split('-')[1].zfill(2)
		tanggal = baris[i+2][0].split('-')[2].zfill(2)
		jam = baris[i+2][1].split(':')[0].zfill(2)
		menit = baris[i+2][1].split(':')[1].zfill(2)
		detik = (('%.1f')%float(baris[i+2][1].split(':')[2])).zfill(4)
		lintang = (('%.2f')%float(baris[i+2][2])).zfill(6)
		bujur = (('%.2f')%float(baris[i+2][3])).zfill(6)
		depth = ('%.1f')%float(baris[i+2][4])
		mag = ('%.1f')%float(baris[i+2][5])
		unknown = '0.0'
		rms = ('%.3f')%float(baris[i+2][10])
		time0 = float(detik)+float(menit)*60+float(jam)*60*60+float(tanggal)*60*60*24
		file.write('#'+tahun.rjust(5)+bulan.rjust(3)+tanggal.rjust(3)+jam.rjust(3)+
			menit.rjust(3)+detik.rjust(5)+lintang.rjust(8)+bujur.rjust(10)+
			depth.rjust(9)+mag.rjust(5)+unknown.rjust(6)+unknown.rjust(6)+
			rms.rjust(8)+str(event).rjust(10)+'\n')
	if len(baris[i])>0 and baris[i][0]=='Net':
		try:
			j=0
			while j<1:
				i=i+1
				try:
					idSta = baris[i][1]
					phase = baris[i][2]
					tanggal = baris[i][3].split('-')[2]
					jam = baris[i][4].split(':')[0]
					menit = baris[i][4].split(':')[1]
					detik = baris[i][4].split(':')[2]
					time1 = float(detik)+float(menit)*60+float(jam)*60*60+float(tanggal)*60*60*24
					deltatime = ('%.2f')%(time1-time0)
					unknown = '1.000'
					file.write(idSta.rjust(5)+deltatime.rjust(12)+unknown.rjust(8)+phase.rjust(4)+'\n')
				except:
					break					
		except:
			break
	i = i+1
file.close()


