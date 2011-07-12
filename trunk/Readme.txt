This is Ankipy version 1.0  
--------------------------          
 Copyright (c) 2011 Yahia Mokli.
 All rights reserved.


License information
-------------------
 GNU General Public License (GPL v. 2)
 See the file "LICENSE" for information on terms & conditions 
 for usage, and a DISCLAIMER OF ALL WARRANTIES.


What is Ankipy?
---------------
  Ankipy is an Open Source program, designed to help students create lists of 
  multiple choice questions (MCQ), and memorize them faster using an interactive 
  testing mode. It may be a useful tool for people who are learning new languages 
  or to prepare for MCQ exams.

  You can find a DATA base for JLPT N5 test vocabulary in romaji ( cause Ankipy 1.0 
  is a console, and doesn't allow the use of Japanese characters ),other data files 
  will be implemented as soon as possible.

  - Ankipy 1.0 is console programe, it doesn't allow Japanese characters  
  - Anki is a Japanese word, it means memorization and learning by heart. 
  - Py is from Python, a famous and amazing programing language.
    	 
How to use Ankipy?
------------------

  --------------------------------------------------------------------------------
  In this section you will find all the instructions that you will need to start  
  using Ankipy, to test and learn new Japanese words or to make your own questions
  in your favorite field of studies.    
  --------------------------------------------------------------------------------

  There are two parts of this Ankipy software. Each part depends on the other.  

  1- Ankipy : ( or the main program ) 
  -----------------------------------
  - Gives the chance to pass testing sessions using modules ( data files ). 
    Actually Ankipy contains about 600 questions related to one topic which is 
    preparation for JLPT (Japanese Language Proficiency Test ) N5 
  - Each test contains 100 questions with one or more true responds.  
  - Ankipy allows you to create unlimited multiple password protected accounts
    so you can use it with your friends or family members without any worries.
  - You can stop at any time and continue your tests from the last taken question.
  - You can also Delete sessions while or after finishing.

  2- Ankipy DATA Maker :
  ----------------------
    It will help you to easily make database files. After that you can use the
    Ankipy main program to start testing sessions using those files.
    To build your data files the right way.

    Main steps to make new data files :
    1- Creat a text data file with all the questions and answers.
    2- Put this text file in DATA folder. 
    3- Start Ankipy DATA Maker and upload the text file.
    4- Start Ankipy main program to start test sessions. 

    please follow instructions in the next manual:


************************************************************************************
		      ANKIPY DATA MAKER MANUAL 
************************************************************************************
			
		      -------------------------	   			       
	 	      IMAGE AND REAL DATA files  
		      -------------------------

  1-Text DATA files (ends with .txt ): 
    Made and uploaded by the user before converting 
    them to real DATA files using Ankipy DATA Maker.    

  2-Real DATA files (ends with _ / or _ followed by a number): 
    Used by Ankipy to start tests.
    Files that end with _ : are made by normal user  
    Files that end with _ followed by a number (Japanese_1) are original DATA files
   	
  Text files are images of real DATA files. The user puts them manually 
  in this folder and converts them to real DATA files using Ankipy DATA Maker.
  The result will be Real DATA files that Ankipy uses to start tests sessions.

  Examples : ( you can find those two files in DATA folder )
  full.txt is the image of full_    
  random.txt is the image of random_ 

 ------------------------- IMPORTANT NOTES ------------------------------------

  1. Please don't change name of generated or original DATA files.
  2. Don't delete DATA files manually, please use Ankipy DATA Maker to do this.

 ------------------------------------------------------------------------------  

		   --------------------------------
 		   HOW CAN I MAKE MY OWN DATA FILES
	           --------------------------------
 		      RANDOM AND FULL DATA FILES 
  		     ----------------------------

1- Full DATA files :
********************

  Definition : ( Open full.txt file to take an idea about how it looks like.)	
    Full DATA files Contain 100 Blocks of questions and (False and True) Answers 
    chosen by user. So user have to build a correct text DATA files 
    before converting them.   


  How to make a Full DATA file:
    Use any text editor and write Blocks of Questions and Answers.  
    Each Block must be built in this way :

    1st Line :  Question 	( What is the capital of France?	)
    2nd Line :  Answer A 	( Alger 				)
    3rd Line :  Answer B 	( Paris 				)
    4th Line :  Answer C 	( Tokyo 				)
    5th Line :  Answer D 	( London 				)
    6th Line :  Correct Answer  ( B 					)
    7th Line :  Empty line	(           				)	 
    8th Line :  Question   	( What are the Japanese writing systems?)
    9th Line :  Answer A   	( Kanji 				)
    10th Line : Answer B 	( Kimono 				)
    11th Line : Answer C 	( Hiragana 				)
    12th Line : Answer D	( Katakana 				)
    13th Line : Correct Answer  ( ACD					)
    14th Line : Empty line 	(					)
    .
    .
    .
    700th (last ) Line :         (Empty line)


  ------------------------- IMPORTANT NOTES ------------------------------------

  1. Text Files must be saved in ANSI or UTF-8 format only 
  2. Full files Always starts with a question and ends with an empty line.
  3. Correct Answer must :
	- Contain these Characters only : A B C and D
   	- Letters Must be written in CAPITAL Characters 
	- Letters Must be sorted from A to D : ex ACD / BC / AD...
  4. Empty spaces at the start of Questions and Answers Line are not allowed.
  5. Put this data text file in DATA folder and start Ankipy DATA Maker. 
  6. DATA maker will analyse it, detect mistakes in your block's constructions 
     and convert it to Real full file. It only takes a few seconds, you can
     find changes in the main program right at the end of conversion process.
  7. Don't repeat questions in the same file.
  8. You can only put 100 Block.  
	 
     Check full.txt to get an idea about how to build your own full DATA files.
        IF YOU FIND ANY PROBLEMS WHILE RUNNING THE PROGRAM CONTACT ME PLEASE
			   yahiala14@hotmail.fr	
  ------------------------------------------------------------------------------  

2- Random DATA files :
**********************

  Definition : (Open random.txt file to take an idea about how it looks like.)	
    Random  DATA files also contain 100 Blocks of questions but ONLY True Answers.
    After Converting this file using Ankipy DATA Maker False Responds will be 
    generated AUTOMATICALLY. This makes building new DATA files easier.    
 
  
  How to make a Full DATA file:
    Use any text editor and write Blocks of Questions and Answers.  
    Each Block must be built in this way :

    1st Line :  Question 	( What the meaning of Ryuu (Japanese)?)
    2nd Line :  Correct Answer	( Dragon,Axe,Style of  		      )
    3rd Line :  Empty line	(           		              )
    4th Line :  Question 	( What is the capital of France?      )
    5th Line :  Correct Answer	( Paris  			      )
    6th Line :  Empty line	(           			      )
    .
    .
    .
    300th (Last) Line : Empty line


  -------------------------- IMPORTANT NOTES ------------------------------------

  1. Text Files must be saved in ANSI or UTF-8 format only 
  2. Random files Always starts with a question and ends with an empty line.
  3. Correct Answer must :
	- Contain one or many responds separated by comma (,) in one line 
   	- Spaces are not allowed after (,)  example ( car,bus,train ) 
  4. Empty spaces at the start of Questions and Answers Line are not allowed. 
  5. Put this data text file in DATA folder and start Ankipy DATA Maker. 
  6. DATA maker will analyse it, detect mistakes in your block's constructions 
     and convert it to Real random file. It only takes a few seconds, you can
     find changes in the main program right at the end of conversion process.
  7. Don't repeat questions in the same file. 
  8. You can only put 100 Block.  

  Check random.txt to get an idea about how to build your own random DATA files.
        IF YOU FIND ANY PROBLEMS WHILE RUNNING THE PROGRAM CONTACT ME PLEASE
			   yahiala14@hotmail.fr	
  -------------------------------------------------------------------------------  	


Release                               
-------
 02/07/2011 - 1.0 Ankipy / Ankipy DATA Maker / JLPT N5 VOCABULARY DATABASE   


Author 
------                               
 name : Yahia Mokli
 email: yahiala14@hotmail.fr