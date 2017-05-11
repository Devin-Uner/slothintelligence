#!/usr/bin/python
import cgi
import Neural_Network
# from Neural_Network import NN_translator
form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers


print '	<head>'






print '		<link rel="stylesheet" type="text/css" href="myStyleSheet.css">'
print ''
print '		<title> Sloth Intelligence </title>'
print ''
print '	</head>'
print ''
print ''
print '	<body>'
print '		<div class="LOGO">'
print '			<img src = "SlothCo.png" alt = "Sloth Intelligence" align="left" style = " width: 500px; height: 500px;" >'
print '		</div>'
print ''
print '		'
print ''
print '		<!-- Class division: Info --> '
print '		<div class="about" name="about">'
print '			<ul>'
print '			  <li><a href="hello.py#about">About</a></li>'
print '			  <li><a href="hello.py#symptoms">Symptom Checker</a></li>'
print '			  <li><a href="hello.py#how-it-works">How It Works</a></li>'
print '			  <li><a href="hello.py#meet-the-team">Meet the Team</a></li>'
print '			</ul>'
print '			'
print '			<!-- Main title: aligned left--> '
print '			<h1 style="padding-left: 25%;">Welcome To Sloth Intelligence</h1>'
print ''
print '			<!-- Paragraph about us: aligned center -->'
print '			<p style="padding-left: 25%;">Sloth Intelligence is redefining the way data is analyzed in the medical field. Our team works to innovate software capable of tracking illness and diagnosing patients in real time.</p><br>'
print '			<p style = "padding-left: 25%;"> Users may select options based on symptoms they have been or are currently experiencing and gain instantaneous results regarding what the illness might be. Additionally, it can help doctors and researchers track epidemics on a global scale so that they may not only treat, but actively prevent illness before it gets out of control.</p>'
print ''
print '		</div>'
print '		<a id = "symptoms"></a>'
print '		<div class="symptoms" name="symptoms" href="#symptoms">'
print '			<!-- This is how to make checkboxes. Is it possible to make the check boxes larger? -->'
print '			<h1>Symptom Checker</h1>'
print '			<p><center>Type the symptoms you are currently having so we can figure out what the problem might be!</center></p>'
print '			<form action="hello.py#symptoms" method="post">'
print '				<input type="text" name="symptoms" size="80">'
print '				<input type="submit">'
print '			</form>'

try:
	x = form["symptoms"]
	myNN = Neural_Network.NN_translator([156,44], ['rectal pain', 'rectal bleeding', 'urine', 'blisters', 'vision problems', 'irritable', 'bleeding gums', 'coughing blood', 'frequent peeing', 'neck pounding', 'rash', 'muscle cramps', 'loss of consciousness', 'no sensation', 'breast size changes', 'oral thrush', 'fungal nails', 'nipple inversion', 'fast heart rate', 'heavy periods', 'chest pain', 'weight loss', 'sore throat', 'nausea', 'unable to pass gas', 'viginal bleeding', 'memory problems', 'dizziness', 'breast lump', 'constipation', 'burning sensation', 'abdominal pain', 'self-loathing', 'vaginal bleeding', 'andominal pain', 'frequent urination', 'helpless', 'pale', 'absence of menstrual cycle', 'high blood pressure', 'bleed between periods', 'irritability', 'mood changes', 'heart failure', 'no sweat', 'pelvic pain', 'stool', 'leg swelling', 'itchy and watery eyes', 'jaundice', 'low appetite', 'sweating', 'vaginal infections', 'confusion', 'dark poop', 'voice change', 'seizure', 'sleep problems', 'eyes pain', 'coma', 'cough', 'weight gain', 'nipple pain', 'lightheaded', 'numbness', 'mouth sores', 'paralysis', 'scrotal pain', 'hopeless', 'breast swelling', 'jaw pain', 'chills', 'body pain', 'darkened areolas', 'earache', 'skin inflammation', 'bone pain', 'flank pain', 'no menstruation', 'nosebleeds', 'urinary problems', 'tingling', 'swollen lymph nodes', 'dry mouth', 'sneezing', 'slow healing', 'brain problems', 'red skin', 'ear pain', 'watery eyes', 'frequent urinary', 'fainting', 'warmth', 'groin swelling', 'headache', 'muscle aches', 'no interest', 'abdominal swelling', 'mood swings', 'painful intercourse', 'hearing changes', 'stress', 'feel worthless', 'easy bruising', 'personality changes', 'low appitite', 'difficulty swallowing', 'passing gas', 'breast pain', 'vaginal discharge', 'missed menstrual cycle', 'guilt', 'testicular pain', 'speech problems', 'congestion', 'face pain', 'thirsty', 'suicide thoughts', 'joint pain', 'hungry', 'palpitations', 'muscle pain', 'larger spleen', 'pallor', 'increased urination', 'unusual bleeding', 'trouble breathing', 'diarrhea', 'no muscle control', 'nose bleed', 'bloody nipple', 'easily get infected', 'stuffy nose', 'urinary urgency', 'larger liver', 'fever', 'implantation bleeding', 'back pain', 'painful urination', 'trouble concentate', 'itchy skin', 'fatigue', 'numb', 'skin hemorrhages', 'seizures', 'skin changes', 'breast skin problems', 'bloating', 'bleed after sex', 'tissue masses', 'white Tongue', 'face swollen', "can't balance", 'Vaginal irritation', 'vaginal irritation', 'bowel habit changes'], ['Irritable Bowel Syndrome (IBS)', 'Urinary Tract Infection', 'lyme disease', 'Heart attacks', 'Colon Cancer', 'Hyperthermia', 'Appendicitis', 'Vaginal Yeast Infection', 'Flu(Infuenza)', 'HIV', 'Bladder Infection', 'Leukemia', 'lung cancer', 'Brain Tumor', 'Menopause', 'Multiple Sclerosis', 'Breast Cancer', 'Herpes', 'Cervical Cancer', 'Diabetes', 'Anxiety', 'Swine flu', 'Early pregnancy', 'Pneumonia', 'malaise', 'High Blood Pressure (Hypertension)', 'Blood Clot', 'Pancreatic cancer', 'lupus', 'Prostate cancer', 'Cancer', 'Ovarian cancer', 'mono', 'Allergy', 'stroke', 'Kidney stone', 'Sinus Infection', 'Ulcer', 'Pregnancy', 'Dengue', 'Cold', 'Anemia', 'Strep Throat', 'Depression'])
	myknowlege = {'Irritable Bowel Syndrome (IBS)': ['abdominal pain', 'bowel habit changes', 'bloating', 'stool', 'passing gas'], 'Urinary Tract Infection': ['fever', 'urine'], 'lyme disease': ['skin inflammation', 'rash', 'fever', 'chills', 'headache', 'muscle pain', 'swollen lymph nodes'], 'Heart attacks': ['chest pain', 'heart failure', 'high blood pressure'], 'Colon Cancer': ['rectal bleeding', 'constipation', 'diarrhea', 'stool', 'weight loss', 'fatigue', 'trouble breathing'], 'Hyperthermia': ['coma', 'confusion', 'dizziness', 'fast heart rate', 'fainting', 'fever', 'headache', 'muscle cramps', 'nausea', 'no sweat', 'rash', 'red skin', 'seizures', 'fatigue'], 'Appendicitis': ['abdominal pain', 'abdominal swelling', 'back pain', 'constipation', 'diarrhea', 'fever', 'unable to pass gas', 'low appetite', 'nausea', 'painful urination', 'rectal pain'], 'Vaginal Yeast Infection': ['Vaginal irritation', 'vaginal discharge'], 'Flu(Infuenza)': ['fever', 'chills', 'cough', 'headache', 'nausea', 'muscle pain', 'fatigue', 'sore throat', 'diarrhea'], 'HIV': ['diarrhea', 'fatigue', 'fever', 'fungal nails', 'groin swelling', 'white Tongue', 'mouth sores', 'oral thrush', 'rash', 'sore throat', 'sweating', 'swollen lymph nodes', 'weight loss'], 'Bladder Infection': ['urine', 'abdominal pain', 'rectal pain', 'frequent urinary', 'urinary urgency'], 'Leukemia': ['bleeding gums', 'bone pain', 'confusion', 'easy bruising', 'larger liver', 'larger spleen', 'fatigue', 'fever', 'headache', 'joint pain', 'no muscle control', 'nausea', 'sweating', 'seizure', 'swollen lymph nodes', 'weight loss'], 'lung cancer': ['trouble breathing', 'chest pain', 'coughing blood', 'difficulty swallowing'], 'Brain Tumor': ["can't balance", 'headache', 'hearing changes', 'memory problems', 'nausea', 'numb', 'personality changes', 'tingling', 'trouble concentate', 'vision problems', 'fatigue'], 'Menopause': ['vaginal bleeding', 'absence of menstrual cycle', 'sweating', 'vaginal irritation'], 'Multiple Sclerosis': ['vision problems', 'tingling', 'numbness', 'speech problems', 'brain problems'], 'Breast Cancer': ['breast lump', 'breast pain', 'breast swelling', 'breast size changes', 'breast skin problems', 'bloody nipple', 'nipple pain', 'nipple inversion'], 'Herpes': ['blisters', 'burning sensation', 'fever', 'itchy skin', 'rash', 'swollen lymph nodes', 'tingling'], 'Cervical Cancer': ['viginal bleeding', 'bleed after sex', 'bleed between periods', 'heavy periods', 'painful intercourse', 'pelvic pain', 'vaginal discharge'], 'Diabetes': ['vision problems', 'dry mouth', 'fatigue', 'frequent peeing', 'hungry', 'easily get infected', 'thirsty', 'itchy skin', 'nausea', 'slow healing', 'vaginal infections', 'weight gain', 'weight loss'], 'Anxiety': ['palpitations', 'sweating', 'irritability', 'stress'], 'Swine flu': ['fever', 'cough', 'stuffy nose', 'fatigue', 'headache'], 'Early pregnancy': ['no menstruation', 'weight gain', 'mood changes', 'increased urination', 'back pain', 'headache', 'darkened areolas', 'fatigue', 'nausea', 'implantation bleeding'], 'Pneumonia': ['sore throat', 'stuffy nose', 'cough', 'fever', 'chills', 'chest pain', 'fatigue', 'headache'], 'malaise': ['fatigue'], 'High Blood Pressure (Hypertension)': ['urine', 'vision problems', 'chest pain', 'dizziness', 'headache', 'leg swelling', 'nosebleeds', 'neck pounding', 'trouble breathing'], 'Blood Clot': ['abdominal pain', 'chest pain', 'confusion', 'diarrhea', 'dizziness', 'headache', 'no sensation', 'brain problems', 'numb', 'pallor', 'paralysis', 'trouble breathing', 'speech problems', 'vision problems', 'warmth', 'fatigue'], 'Pancreatic cancer': ['jaundice', 'nausea', 'weight loss', 'itchy skin', 'low appitite', 'back pain'], 'lupus': ['fever', 'joint pain', 'rash', 'nausea', 'muscle pain', 'fatigue'], 'Prostate cancer': ['urinary problems', 'weight loss', 'bone pain'], 'Cancer': ['fatigue', 'weight loss', 'skin changes', 'stool', 'urine', 'unusual bleeding', 'cough', 'voice change', 'fever', 'tissue masses'], 'Ovarian cancer': ['abdominal swelling', 'low appitite', 'trouble breathing'], 'mono': ['fatigue', 'low appetite', 'chills', 'sore throat', 'fever', 'swollen lymph nodes'], 'Allergy': ['congestion', 'itchy and watery eyes'], 'stroke': ['numbness', 'fatigue', 'tingling', 'vision problems', 'confusion', 'loss of consciousness', 'speech problems', 'nausea'], 'Kidney stone': ['andominal pain', 'urine', 'flank pain', 'back pain', 'nausea', 'scrotal pain', 'sweating', 'testicular pain'], 'Sinus Infection': ['face swollen', 'face pain', 'earache', 'jaw pain', 'cough', 'fever', 'trouble breathing', 'sneezing', 'ear pain'], 'Ulcer': ['low appetite', 'abdominal pain', 'dark poop'], 'Pregnancy': ['missed menstrual cycle', 'breast pain', 'nausea', 'fatigue', 'mood swings', 'headache', 'frequent urination'], 'Dengue': ['abdominal pain', 'bleeding gums', 'bone pain', 'trouble breathing', 'easy bruising', 'fever', 'headache', 'joint pain', 'back pain', 'muscle pain', 'nose bleed', 'eyes pain', 'rash', 'skin hemorrhages', 'swollen lymph nodes', 'nausea'], 'Cold': ['cough', 'stuffy nose', 'sore throat', 'sneezing', 'fever', 'watery eyes', 'headache', 'fatigue', 'body pain'], 'Anemia': ['lightheaded', 'fatigue', 'pale', 'fast heart rate', 'trouble breathing'], 'Strep Throat': ['sore throat', 'difficulty swallowing', 'fever', 'chills', 'muscle aches', 'swollen lymph nodes', 'rash'], 'Depression': ['feel worthless', 'hopeless', 'helpless', 'guilt', 'no interest', 'irritable', 'low appetite', 'sleep problems', 'self-loathing', 'suicide thoughts'], "cold": ["sneezing"], "cold":["headache", "runny noes", "sneezing", "coughing"]}
	for i in range(0, 1):
		for key in myknowlege.keys():
			myNN.train(myknowlege[key], key)
	myNN.neural_net.save_data()
	print 'your top three most likely diseases are...'
	print myNN.get_best_three(x.value)
except:
	print 'no data entered'

print '<div class="neural_network_output">'
print '	</div>'
print ''
print '		</div>'
print '		<div class = "how-it-works" id="information" name = "how-it-works">'
print '			<h1> How It Works</h1>'
print '			<p>The solution to worldwide illness is simple. Sloth Intelligence utilizes a neural network. Over time, the neural network is able to learn and diagnose. If it is incorrect it will adapt, receive new data, and learn. Each time a page is loaded the neural network gets slightly more accurate. Each computer using Sloth Intelligence will help to strengthen the network. Every time the page is loaded the neural network gets a little bit more accurate. Over time, with each connected device the potential of this software becomes limitless. <br>'
print '			 <br>'
print '			<br></p>'
print '		</div>'
print '	</body>'
