''' NIM/Nama  : 13517137/Vincent Budianto
	Nama file : Kit.py
	Topik     : Kit Asisten
	Tanggal   : 17 Maret 2019
	Deskripsi : Program untuk unzip hasil kerjaan praktikan dan mengecek hasil pekerjaan praktikan '''

import os
import re
import subprocess
import sys
import zipfile

#Inisialisasi Variabel Global
global cek1
global cek2
global dir_name
global nim
global nim_fakultas
global prefix
global substring
global year

#Inisialisasi Variabel
input1 = 0
input2 = 0
input3 = 0
cek1 = True
cek2 = True
dir_name = 'C:\\Users\\vincent VB\\Desktop\\IF\\Asisten'
fakultas = ['fitb', 'fmipa']
nim = []
nim_fakultas = ['163', '160']
prefix = ['B0', 'PB0']
substring = ['Praktikum', 'PR']
year = ''

#Fungsi dan Prosedur
def unzip_files(a):
	global dir_name
	global prefix

	if (a == '1'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				try:
					if (filename.startswith(prefix[0]) and filename.endswith('.zip')):
						# get path of files
						abs_file_path = os.path.join(path, filename)
						# get path of zip files
						zip_path = os.path.split(abs_file_path)[0]
						# create object extracted
						zip_obj = zipfile.ZipFile(abs_file_path, 'r')
						# extract file to dir
						zip_obj.extractall(zip_path)
						# close zip file
						zip_obj.close()
						print(filename, 'unzipped')
						# delete zipped file
						#os.remove(abs_file_path)
				except:
					print('Error Code 0x01110000')
	if (a == '2'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				try:
					if (filename.startswith(prefix[1]) and filename.endswith('.zip')):
						# get path of files
						abs_file_path = os.path.join(path, filename)
						# get path of zip files
						zip_path = os.path.split(abs_file_path)[0]
						# create object extracted
						zip_obj = zipfile.ZipFile(abs_file_path, 'r')
						# extract file to dir
						zip_obj.extractall(zip_path)
						# close zip file
						zip_obj.close()
						print(filename, 'unzipped')
						# delete zipped file
						#os.remove(abs_file_path)
				except:
					print('Error Code 0x01110000')

def unzip(a, b, c):
	global dir_name
	global nim
	global nim_fakultas
	global prefix
	global substring
	global year

	if (a == '1'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				try:
					if (filename.startswith(fakultas[c]) and filename.endswith('.zip') and ((substring[0] + ' ' + b) in filename) and (not(substring[1] in filename))):
						abs_file_path = os.path.join(path, filename)
						zip_path = os.path.split(abs_file_path)[0]
						zip_obj = zipfile.ZipFile(abs_file_path, 'r')
						file_list = zip_obj.namelist()
						file_list.sort()
						print()
						print(os.path.split(abs_file_path)[1], 'unzipped')
						print()
						input('--- Press Any Key To Continue ---')
						print()

						for file_name in file_list:
							i = 0
							found = False

							while ((i < len(nim)) and (not(found))):
								if ((nim_fakultas[c] + year + nim[i]) in file_name):
									found = True
								else:
									i += 1

							if (found):
								zip_obj.extract(file_name, zip_path)
								print(file_name, 'unzipped')

						zip_obj.close()
				except:
					print('Error Code 0x01110011')
	elif (a == '2'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				try:
					if (filename.startswith(fakultas[c]) and filename.endswith('.zip') and ((substring[1] + ' ' + substring[0] + ' ' + b) in filename)):
						abs_file_path = os.path.join(path, filename)
						zip_path = os.path.split(abs_file_path)[0]
						zip_obj = zipfile.ZipFile(abs_file_path, 'r')
						file_list = zip_obj.namelist()
						file_list.sort()
						print()
						print(os.path.split(abs_file_path)[1], 'unzipped')
						print()
						input('--- Press Any Key To Continue ---')
						print()

						for file_name in file_list:
							i = 0
							found = False

							while ((i < len(nim)) and (not(found))):
								if ((nim_fakultas[c] + year + nim[i]) in file_name):
									found = True
								else:
									i += 1

							if (found):
								zip_obj.extract(file_name, zip_path)
								print(file_name, 'unzipped')

						zip_obj.close()
				except:
					print('Error Code 0x01110012')

	print()
	input('--- Press Any Key To Continue ---')
	print()
	unzip_files(a)
	print()
	input('--- FINISHED ---')

def runCPP(a, b):
	global dir_name
	global nim
	global nim_fakultas
	global prefix
	global substring
	global year

	if (a == '1'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				os.system('cls')

				try:
					if (filename.startswith(prefix[0] + b) and filename.endswith('.cpp')):
						NIM = ''
						No = ''
						zipname = ''
						splitFileName = re.split('', filename)

						for i in range(5, 13):
							NIM += splitFileName[i]

						for j in range(14, 16):
							No += splitFileName[j]

						for zippath, zipdir_list, zipfilelist in os.walk(path):
							for zipfilename in zipfilelist:
								if (zipfilename.startswith(prefix[0] + b) and zipfilename.endswith('.zip')):
									abs_file_path = os.path.join(path, zipfilename)
									zipname = zipfilename

						print('Soal', No)
						print('NIM           :', NIM)
						print('Nama File     :', filename)
						print('Nama ZIP File :', zipname)
						print()
						success = False

						try:
							os.chdir(path)
							os.system('g++ -o ' + filename.split('.cpp')[0] + ' ' + filename)
							success = True
						except IOError:
							print(filename, 'Not Found')
						except:
							print('Compile Error')

						if (success):
							try:
								os.chdir(path)
								print(filename + ' Compiled')
								print()

								if (cek1):
									print('Source Code :')
									print()
									f = open(filename,'r')
									print(f.read())
									f.close()
									print()

								print('Hasil       :')
								print()

								if ('1' in No):
									if (cek2):
										print('Testcase 1:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input1.txt')
										print()
										print()
										print('Testcase 2:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input1a.txt')
									else:
										os.system(filename.split('.cpp')[0])
								elif ('2' in No):
									if (cek2):
										print('Testcase 1:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input2.txt')
										print()
										print()
										print('Testcase 2:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input2a.txt')
									else:
										os.system(filename.split('.cpp')[0])
							except IOError:
								print(filename.split('.cpp')[0], 'Not Found')
							except:
								print('Run Error')

						print()
						print()
						input('--- Next Answer ---')
						print()
				except:
					print('Error Code 0x01110022')
	elif (a == '2'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				os.system('cls')

				try:
					if (filename.startswith(prefix[1] + b) and filename.endswith('.cpp')):
						NIM = ''
						No = ''
						zipname = ''
						splitFileName = re.split('', filename)

						for i in range(6, 14):
							NIM += splitFileName[i]

						for j in range(15, 17):
							No += splitFileName[j]

						for zippath, zipdir_list, zipfilelist in os.walk(path):
							for zipfilename in zipfilelist:
								if (zipfilename.startswith(prefix[1] + b) and zipfilename.endswith('.zip')):
									abs_file_path = os.path.join(path, zipfilename)
									zipname = zipfilename

						print('Soal', No)
						print('NIM           :', NIM)
						print('Nama File     :', filename)
						print('Nama ZIP File :', zipname)
						print()
						success = False

						try:
							os.chdir(path)
							os.system('g++ -o ' + filename.split('.cpp')[0] + ' ' + filename)
							success = True
						except IOError:
							print(filename, 'Not Found')
						except:
							print('Compile Error')

						if (success):
							os.chdir(path)
							print(filename + ' Compiled')
							print()

							if (cek1):
								print('Source Code :')
								print()
								f = open(filename,'r')
								print(f.read())
								f.close()
								print()

							print('Hasil       :')
							print()

							try:
								if ('1' in No):
									if (cek2):
										print('Testcase 1:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input1.txt')
										print()
										print()
										print('Testcase 2:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input1a.txt')
									else:
										os.system(filename.split('.cpp')[0])
								elif ('2' in No):
									if (cek2):
										print('Testcase 1:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input2.txt')
										print()
										print()
										print('Testcase 2:')
										os.system(filename.split('.cpp')[0] + ' < ../../../input2a.txt')
									else:
										os.system(filename.split('.cpp')[0])
							except IOError:
								print(filename.split('.cpp')[0], 'Not Found')
							except:
								print('Run Error')

						print()
						print()
						input('--- Next Answer ---')
						print()
				except:
					print('Error Code 0x01110022')

def runPYTHON(a, b):
	global dir_name
	global nim
	global nim_fakultas
	global prefix
	global year

	if (a == '1'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				os.system('cls')

				try:
					if (filename.startswith(prefix[0] + b) and filename.endswith('.py')):
						NIM = ''
						No = ''
						zipname = ''
						splitFileName = re.split('', filename)

						for i in range(5, 13):
							NIM += splitFileName[i]

						for j in range(14, 16):
							No += splitFileName[j]

						for zippath, zipdir_list, zipfilelist in os.walk(path):
							for zipfilename in zipfilelist:
								if (zipfilename.startswith(prefix[0] + b) and zipfilename.endswith('.zip')):
									abs_file_path = os.path.join(path, zipfilename)
									zipname = zipfilename

						print('Soal', No)
						print('NIM           :', NIM)
						print('Nama File     :', filename)
						print('Nama ZIP File :', zipname)
						print()
						success = False

						try:
							os.chdir(path)
							os.system('python -m py_compile ' + filename)
							success = True
						except IOError:
							print(filename, 'Not Found')
						except:
							print('Compile Error')

						if (success):
							os.chdir(path)
							print(filename + ' Compiled')
							print()

							if (cek1):
								print('Source Code :')
								print()
								f = open(filename,'r')
								print(f.read())
								f.close()
								print()

							print('Hasil       :')
							print()

							try:
								if ('1' in No):
									if (cek2):
										os.system('python ' + filename + ' < ../../../input1.txt')
									else:
										os.system('python ' + filename)
								elif ('2' in No):
									if (cek2):
										os.system('python ' + filename + ' < ../../../input2.txt')
									else:
										os.system('python ' + filename)
							except IOError:
								print(filename, 'Not Found')
							except:
								print('Run Error')

						print()
						print()
						input('--- Next Answer ---')
						print()
				except:
					print('Error Code 0x01110022')
	elif (a == '2'):
		for path, dir_list, filelist in os.walk(dir_name):
			for filename in filelist:
				os.system('cls')

				try:
					if (filename.startswith(prefix[1] + b) and filename.endswith('.py')):
						NIM = ''
						No = ''
						zipname = ''
						splitFileName = re.split('', filename)

						for i in range(6, 14):
							NIM += splitFileName[i]

						for j in range(15, 17):
							No += splitFileName[j]

						for zippath, zipdir_list, zipfilelist in os.walk(path):
							for zipfilename in zipfilelist:
								if (zipfilename.startswith(prefix[1] + b) and zipfilename.endswith('.zip')):
									abs_file_path = os.path.join(path, zipfilename)
									zipname = zipfilename

						print('Soal', No)
						print('NIM           :', NIM)
						print('Nama File     :', filename)
						print('Nama ZIP File :', zipname)
						print()
						success = False

						try:
							os.chdir(path)
							os.system('python -m py_compile ' + filename)
							success = True
						except IOError:
							print(filename, 'Not Found')
						except:
							print('Compile Error')

						if (success):
							try:
								os.chdir(path)
								print(filename + ' Compiled')
								print()

								if (cek1):
									print('Source Code :')
									print()
									f = open(filename,'r')
									print(f.read())
									f.close()
									print()

								print('Hasil       :')
								print()

								if ('1' in No):
									if (cek2):
										os.system('python ' + filename + ' < ../../../input1.txt')
									else:
										os.system('python ' + filename)
								elif ('2' in No):
									if (cek2):
										os.system('python ' + filename + ' < ../../../input2.txt')
									else:
										os.system('python ' + filename)
							except IOError:
								print(filename, 'Not Found')
							except:
								print('Compile Error')

						print()
						print()
						input('--- Next Answer ---')
						print()
				except:
					print('Error Code 0x01110022')

def menuUNZIP(a):
	b = 0

	while ((b != '3') or (b != '4')):
		os.system('cls')
		print('Menu', a, ':')
		print('1. Praktikum')
		print('2. PR')
		print('3. Back')
		print('4. Exit')
		b = input('>> ')

		if (b == '1'):
			N = input('Praktikum ke : ')
			unzip(b, N, a)
		elif (b == '2'):
			N = input('PR ke : ')
			unzip(b, N, a)
		elif (b == '3'):
			break
		elif (b == '4'):
			exit()

def setNIM():
	global nim

	os.system('cls')
	print('NIM saat ini:', nim)
	nim.clear()
	x = int(input('NIM awal    : '))

	if (x == 0):
		pass
	else:
		y = int(input('NIM akhir   : '))

		for z in range(x, (y + 1)):
			nim.append(str(z))

	print('NIM         :', nim)
	input('--- Finished ---')

def setYear():
	global year

	os.system('cls')
	print('Angkatan saat ini:', year)
	year = input('Angkatan         : ')

	if (year == 'x'):
		year = ''

	input('--- Finished ---')

def setCek1():
	global cek1

	a = ''
	b = True

	while (b):
		print('Status: ', end = '')
		os.system('cls')

		if (cek1):
			print('on')
		else:
			print('off')

		print()
		a = input('Change status? (Y/N) ')

		if ((a == 'Y') or (a == 'y') or (a == 'N') or (a == 'n')):
			b = False

	print()
	print('Status: ', end = '')

	if ((a == 'Y') or (a == 'y')):
		if (cek1):
			cek1 = False
			print('Show source code turned off')
		else:
			cek1 = True
			print('Show source code turned on')
	else:
		if (cek1):
			print('Show source code turned on')
		else:
			print('Show source code turned off')

	print()
	input('--- Finished ---')

def setCek2():
	global cek2

	a = ''
	b = True

	while (b):
		print('Status: ', end = '')
		os.system('cls')

		if (cek2):
			print('on')
		else:
			print('off')

		print()
		a = input('Change status? (Y/N) ')

		if ((a == 'Y') or (a == 'y') or (a == 'N') or (a == 'n')):
			b = False

	print()
	print('Status: ', end = '')

	if ((a == 'Y') or (a == 'y')):
		if (cek2):
			cek2 = False
			print('Auto input turned off')
		else:
			cek2 = True
			print('Auto input turned on')
	else:
		if (cek2):
			print('Auto input turned on')
		else:
			print('Auto input turned off')

	print()
	input('--- Finished ---')

#Program Utama
if (__name__ == "__main__"):
	while (input1 != '7'):
		os.chdir(dir_name)
		os.system('cls')
		print('Menu:')
		print('1. UNZIP Files')
		print('2. Test Files')
		print('3. Set NIM')
		print('4. Set Year')
		print('5. Set Show Source Code')
		print('6. Set Auto Input')
		print('7. Exit')
		input1 = input('>> ')

		if (input1 == '1'):
			while ((input2 != '3') or (input2 != '4')):
				os.system('cls')
				print('Menu UNZIP:')
				print('1.', fakultas[0])
				print('2.', fakultas[1])
				print('3. Back')
				print('4. Exit')
				input2 = input('>> ')

				if (input2 == '1'):
					if (not(nim)):
						input('--- NIM empty ---')
						input2 = '3'
					elif (year == ''):
						input('--- Year invalid ---')
						input2 = '3'
					else:
						menuUNZIP(0)
				elif (input2 == '2'):
					if (not(nim)):
						input('--- NIM empty ---')
						input2 = '3'
					elif (year == ''):
						input('--- Year invalid ---')
						input2 = '3'
					else:
						menuUNZIP(1)
				elif (input2 == '3'):
					break
				elif (input2 == '4'):
					exit()
		elif (input1 == '2'):
			while ((input2 != '3') or (input2 != '4')):
				os.system('cls')
				print('Menu Test:')
				print('1. C++')
				print('2. Python')
				print('3. Back')
				print('4. Exit')
				input2 = input('>> ')

				if (input2 == '1'):
					while ((input3 != '3') or (input3 != '4')):
						os.system('cls')
						print('Menu C++:')
						print('1. Praktikum')
						print('2. PR')
						print('3. Back')
						print('4. Exit')
						input3 = input('>> ')

						if (input3 == '1'):
							if (year == ''):
								input('--- Year invalid ---')
								input2 = '3'
								input3 = '3'
							else:
								N = input('Praktikum ke : ')
								runCPP(input3, N)
						elif (input3 == '2'):
							if (year == ''):
								input('--- Year invalid ---')
								input2 = '3'
								input3 = '3'
							else:
								N = input('PR ke : ')
								runCPP(input3, N)
						elif (input3 == '3'):
							break
						elif (input3 == '4'):
							exit()
				if (input2 == '2'):
					while ((input3 != '3') or (input3 != '4')):
						os.system('cls')
						print('Menu Python:')
						print('1. Praktikum')
						print('2. PR')
						print('3. Back')
						print('4. Exit')
						input3 = input('>> ')

						if (input3 == '1'):
							if (year == ''):
								input('--- Year invalid ---')
								input2 = '3'
								input3 = '3'
							else:
								N = input('Praktikum ke : ')
								runPYTHON(input3, N)
						elif (input3 == '2'):
							if (year == ''):
								input('--- Year invalid ---')
								input2 = '3'
								input3 = '3'
							else:
								N = input('PR ke : ')
								runPYTHON(input3, N)
						elif (input3 == '3'):
							break
						elif (input3 == '4'):
							exit()
				elif (input2 == '3'):
					break
				elif (input2 == '4'):
					exit()
		elif (input1 == '3'):
			setNIM()
		elif (input1 == '4'):
			setYear()
		elif (input1 == '5'):
			setCek1()
		elif (input1 == '6'):
			setCek2()
		elif (input1 == '7'):
			exit()

