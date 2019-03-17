import cv2
import glob

files = glob.glob("./img_60/*")
files = sorted(files)
for file in files:
	print(file)
	# 画像ファイルの読み込み
	img = cv2.imread(file)
	
	# ORB (Oriented FAST and Rotated BRIEF)
	#detector = cv2.ORB_create()
	#detector = cv2.AKAZE_create()
	#detector = cv2.AgastFeatureDetector_create()
	detector = cv2.FastFeatureDetector_create()
	# 特徴検出
	keypoints = detector.detect(img)
	print(len(keypoints))

