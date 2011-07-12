# -*- coding: utf-8 -*-


# @author  Yahia Mokli
# @license GNU General Public License (GPL v. 2)
# 
# This file is part of Ankipy.
#
# Ankipy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Ankipy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ankipy.  If not, see <http://www.gnu.org/licenses/>.


"""
Ankipy is a Python Program designed to help students creat lists of multiple
choice questions (MCQ) and memorize them faster using an interactive testing mode.
It may be a useful tool for people who want to learn new languages or to prepare for MCQ exams.
Anki is a Japanese word, it means memorization and learning by heart and Py is from Python.
"""


###########################################     IMPORTS      ################################################################


from string import *        # import all the modules related to string (ex:lower)
import cPickle              # import cpickle data manager
import os                   # os.system('CLS') help me to clean the screen
import time                 # for the entrence logo
import random               # to make random answers 
import ctypes               # for consol colors 

#---------------------- COLORS PACK ----------------------------------------#

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

#---------------------------------------------------------------------------#


############################################  FUNCTIONS  ##################################################################

#---------------------#
# GRAPHICS FUNCTIONS  #
#---------------------#

def longLine ():
    """ prints a full screen long line """
    set_color(0xF3, handle=std_out_handle)
    print u'─'*80,
    set_color(0xF0, handle=std_out_handle)
    print

#--------------------------------------------------------------------------------------------------------------------------#

def Xprint(x):
    """ x = number of empty lines """ 
    n = 0
    while n < x:
        print 
        n += 1 
    return None

#--------------------------------------------------------------------------------------------------------------------------#

def logo1 ():
    """ main logo """
    print
    print
    set_color(0xF3, handle=std_out_handle)
    print u'                                                 █▀▀█ █▀█ █ █  █ █   █▀▀█ █  █ '  
    print u'  DATA MAKER     (C) COPYRIGHT 2011 YAHIA MOKLI  █▄▄█ █ █ █ █▀▀▀ █   █▄▄█ █▄▄█ '
    print u'───────────────────────────────────────────────  █  █ █ █▄█ █▀▀█ █   █    ▄▄▄█ '
    set_color(0xF0, handle=std_out_handle)
    print
    print 

#--------------------------------------------------------------------------------------------------------------------------#

def entrence ():
    """ entrence logo """
    set_color(0xF3, handle=std_out_handle)
    
    print 
    print
    
    print u'         █████████  ██████  ██  ██    ██  ██       █████████  ██     ██ '
    print u'         ██▀▀▀▀▀██  ██▀▀██  ██  ██    ██  ▀▀       ██▀▀▀▀▀██  ██     ██ '  
    print u'         ██     ██  ██  ██  ██  ██▄▄▄▄██  ██       ██     ██  ██     ██ '
    print u'         ██▄▄▄▄▄██  ██  ██  ██  ██▀▀▀▀▀▀  ██       ██▄▄▄▄▄██  ██▄▄▄▄▄██ '     
    print u'         █████████  ██  ██  ██  ██▄▄▄▄▄▄  ██       █████████  █████████ '
    print u'         ██     ██  ██  ██  ██  ██▀▀▀▀██  ██       ██                ██ '
    print u'         ██     ██  ██  ██▄▄██  ██    ██  ██       ██         ▄▄▄▄▄▄▄██ '
    print u'         ██     ██  ██  ██████  ██    ██  ██       ██         █████████ '
    print
    print 
    print u'                                                             DATA MAKER '                            
    print
    print
    print
    print  
    print
    print 
    print
    set_color(0xF8, handle=std_out_handle)  
    print u'  ANKIPY 1.0 '
    print
    set_color(0xF4, handle=std_out_handle)
    print u'  (C) COPYRIGHT 2011 YAHIA MOKLI',
    print ' GNU v2'
    time.sleep (3)
    set_color(0xF0, handle=std_out_handle)
    os.system('CLS')

#------------------------------------------#
#   function show graphics when exit       #
#------------------------------------------#

def putcenter (x):
    """ put x at the center of the page """
    y=len(x)
    print (' '*((80-y)/2)) + x
    return None

def byebye ():
    """ show some graph at the end """
    set_color(0x0F, handle=std_out_handle)
    os.system('CLS')
    
    set_color(0x0F, handle=std_out_handle)
    Xprint (6)
    putcenter ('Thank you for using Ankipy')
    print 
    putcenter ('YAHIA MOKLI (C) 2011 ')
    Xprint(12) 
    set_color(0x04, handle=std_out_handle)  
    print u'  DONATIONS BANK ACCOUNT ' 
    set_color(0x04, handle=std_out_handle)
    print u'  IBAN:  00003 756 007887 77 201 033 '
    print u'  SWIFT: BADR DZAL '
    time.sleep (3)
    set_color(0x0F, handle=std_out_handle)
    os.system('CLS')


    set_color(0x0F, handle=std_out_handle)
    Xprint(6) 
    putcenter ('Help us with your ideas to make this program better')
    print 
    putcenter ('Please contact me on this e-mail')
    print 
    putcenter ('yahiala14@hotmail.fr ')
    Xprint(10)                  
    set_color(0x04, handle=std_out_handle)  
    print u'  DONATIONS BANK ACCOUNT ' 
    set_color(0x04, handle=std_out_handle)
    print u'  IBAN:  00003 756 007887 77 201 033 '
    print u'  SWIFT: BADR DZAL '
    time.sleep (6)
    exit()

#----------------------------#
# main loop control function #
#----------------------------#

def yes_no (strt):
    """ program starter """
   
    while (strt != 'N')&(strt != 'Y'):
        set_color(0xF8, handle=std_out_handle)
        strt = upper ( raw_input("  Answer using <Y> or <N> please : ") )
        set_color(0xF0, handle=std_out_handle)
        
    if strt == ('Y'):
        return strt
    
    else:
        
        print
        set_color(0xF8, handle=std_out_handle)
        raw_input ('  Press <Enter> to return to main menu ')
        set_color(0xF0, handle=std_out_handle)
        return strt
    
#-----------------------------#
# files converting functions  #
#-----------------------------#

def readfile6 ( f_name , q_num ) :
    """ creat cPickle data file for full and random mode """
                                   
    f = open( './DATA/'+f_name ,'r')                # open file of questions 
    G = list(' '* (q_num * 7))      #n!             # creat a general list where we put Qst-ansA... in this order 
    Gtmp = []
    n = 0
    
    Q = list (' '*q_num)
    A = list (' '*q_num)
    B = list (' '*q_num)
    C = list (' '*q_num)
    D = list (' '*q_num)
    E = list (' '*q_num)
    F = list (' '*q_num)            #n!


    # make a temp list 
    for line in f:
        Gtmp.append ( line.replace('\n','') )
        n += 1

    Gtmp.append('')
        
    # put the data in the official G list 
    kj = 0
    while 1 :
        G[kj] = Gtmp[kj]
        kj += 1
        if kj == 700: break


    i = 0
    while i < q_num: #n! 6 for 3qst / 7 for 4qst
        Q[i]=G[0+7*i]
        A[i]=G[1+7*i]
        B[i]=G[2+7*i]
        C[i]=G[3+7*i]
        D[i]=G[4+7*i]
        E[i]=G[5+7*i]
        F[i]=G[6+7*i]
        
        ###### do some graphs
        os.system('CLS')
        logo1 ()
        Xprint(4)
        set_color(0xF2, handle=std_out_handle)
        print ' '*37 + str(i+1)+'%'
        print u'            ┌'+u'─'*50+u'┐'
        print u'            │'+u'█'*((i+1)/2)+' '*(50-((i+1)/2))+u'│'
        print u'            └'+u'─'*50+u'┘'
        set_color(0xF0, handle=std_out_handle)   

        i += 1
    
    f.close()
    
    T = ['','','','','','']
    T[0]= Q
    T[1]= A
    T[2]= B
    T[3]= C
    T[4]= D
    T[5]= E 

    ##### this new file
    file2 = open ( './DATA/'+f_name.replace('.txt','_') ,'w')
    cPickle.dump( T , file2 )
    file2.close ()

    ##### open the cPickle file
    f1 = open ( './MODULE/modules' )
    add_module = cPickle.load( f1 )
    f1.close ()

    # . txt
    # . _data.txt

    if f_name[-9:] == '_data.txt':
        add_module.append( f_name.replace('_data.txt','_') )

    else:
        add_module.append( f_name.replace('.txt','_') )
    
    # save new name in modules file 
    f_add = open ( './MODULE/modules' ,'w')
    cPickle.dump( add_module , f_add )
    f_add.close ()
    
    print
    set_color(0xF4, handle=std_out_handle)
    print "  Done ! File saved correctly in DATA folder "
    set_color(0xF0, handle=std_out_handle)
    print
    return None

#--------------------------------------------------------------------------------------------------------------------------#

def virgula ( seq ):
    """ return 4 separated words """
    n =len(seq)
    vir = list(' '* 3)
    i = 0    
    k=0
    
    while i<n:
        if seq[i]==',':
            vir[k]=i
            k += 1 
        i=i+1
    
    if k == 0:
        seq1 = seq                  #1sr word
        seq2 = ' '
        seq3 = ' '
        seq4 = ' '
        
    elif  k == 1:
        seq1 = seq[:vir[0]]         #1st word
        seq2 = seq[vir[0]+1:]       #2nd word
        seq3 = ' '
        seq4 = ' '

    elif k == 2:
        seq1 = seq[:vir[0]]         #1st word 
        seq2 = seq[vir[0]+1:vir[1]] #2nd word 
        seq3 = seq[vir[1]+1:]       #3rd word 
        seq4 = ' '

    else:
        seq1 = seq[:vir[0]]         #1st word 
        seq2 = seq[vir[0]+1:vir[1]] #2nd word 
        seq3 = seq[vir[1]+1:vir[2]] #3rd word 
        seq4 = seq[vir[2]+1:]       #4th word

    return seq1,seq2,seq3,seq4

#--------------------------------------------------------------------------------------------------------------------------#

def virgula2 ( Lst ):
    """ return 4 separated words difrece is this return withour empty sapaces """

    wrong=[]
    u=0
    while u < len (Lst):
        seq = Lst[u]
    
        n =len(seq)
        vir = list(' '* 3)
        i = 0    
        k=0
        
        while i<n:
            if seq[i]==',':
                vir[k]=i
                k += 1 
            i=i+1
    
        if k == 0:
            seq1 = seq
            wrong.append(seq1)
            
        elif  k == 1:
            seq1 = seq[:vir[0]]         #1st word
            seq2 = seq[vir[0]+1:]       #2nd word
            wrong.append(seq1)
            wrong.append(seq2)
            
        elif k == 2:
            seq1 = seq[:vir[0]]         #1st word 
            seq2 = seq[vir[0]+1:vir[1]] #2nd word 
            seq3 = seq[vir[1]+1:]       #3rd word 
            wrong.append(seq1)
            wrong.append(seq2)
            wrong.append(seq3)
        else:
            seq1 = seq[:vir[0]]         #1st word 
            seq2 = seq[vir[0]+1:vir[1]] #2nd word 
            seq3 = seq[vir[1]+1:vir[2]] #3rd word 
            seq4 = seq[vir[2]+1:]       #4th word
            wrong.append(seq1)
            wrong.append(seq2)
            wrong.append(seq3)
            wrong.append(seq4)  
        u += 1
        
    return wrong

#--------------------------------------------------------------------------------------------------------------------------#

def emptyCounter ( Lst ) :
    """ count empty items in lists """
    
    i=0
    count = 0
    while i<len(Lst):
        if Lst[i]==' ':
            count += 1
        i += 1
    return count

#--------------------------------------------------------------------------------------------------------------------------#

def fill_in ( correct ,wrongF ) :
    """ fill in empty items """
    
    i = 0
    j = 0
    while i < len(correct):
        if correct[i]==' ':
            correct[i]=wrongF[j]
            j +=1
        i += 1
    return correct

#--------------------------------------------------------------------------------------------------------------------------#

def print_file ( yahia , file_name):
    """ write file : qst / ans A / ans B / ans C /ansD/ crct / empty """
    
    yahiaK = yahia.keys()

    p=0
    while p<len(yahiaK):
        f = open ('./DATA/'+file_name,'a')
        f.write(yahiaK[p]+'\n')
        o=0
        while o < len(yahia[yahiaK[p]]):
            f.write(yahia[yahiaK[p]][o]+'\n')
            o += 1
        f.write('\n')
        f.close ()
        p += 1

#--------------------------------------------------------------------------------------------------------------------------#

def readfile3 ( f_name , q_num ) :
    """ creat cPickle data file for random mode """
    
    f = open( './DATA/'+f_name ,'r')    # open file of questions 
    G = list(' '* (q_num*3))           # creat a general list where we put Qst-ansA... in this order 
    Gtmp = []
    n = 0

    Q = list (' '*q_num)
    A = list (' '*q_num)
    E = list (' '*q_num)

    # make a temp list 
    for line in f:
        Gtmp.append ( line.replace('\n','') )
        n += 1
    Gtmp.append('')
    
    # put the data in the official G list 
    kj = 0
    while 1:
        G[kj] = Gtmp[kj]
        kj += 1
        if kj == 300: break
    
    
    i = 0
    while i < q_num:
        Q[i]=G[0+3*i]
        A[i]=G[1+3*i]
        E[i]=G[2+3*i]
        i += 1
    
    f.close()
    
    T = ['','']
    T[0]= Q
    T[1]= A

    ##### add new file in DATA file
    f = open ( './DATA/'+f_name.replace('.txt','') ,'w')
    cPickle.dump( T , f )
    f.close ()
    
    return None        


#--------------------------------------------------------------#
#                     The new file maker                       #
#--------------------------------------------------------------#

def Xreadfile (f_name , q_num , typ ):
    """ creat data files """
    
    if typ=='full':
        ##### creat our final cpickle file
        readfile6 ( f_name , q_num  )
        
    elif typ=='random':
        ##### creat a temp cPickle file with organized data
        readfile3 ( f_name , q_num )
        
        abc = f_name
        ##### open the cPickle file
        f = open ( './DATA/'+abc.replace('.txt','') )
        T = cPickle.load( f )
        f.close ()
        
        ##### creat lists of words
        japG = T[0]         #list of all the japanese words
        engG = T[1]         #list of all the correct english translations

        engG2 = engG[:]

        m=0
        yahia={}
        while m < len(japG) :
                engList = list( virgula(engG[m]))   #remove ',' to make 4 words
                random.shuffle(engList)             #rondomiz the list of (4) answers
                
                ##### make the correct answer depending on the words positions
                alph = ['A','B','C','D'] 
                crc = '' 
                for w in [0,1,2,3]:
                    if engList[w]!=' ':
                        crc = crc + alph[w]
                        
                ##### add crc to the end of english list        
                engList.append(crc) 
            
                ##### creat wrong list 
                engG2.pop(m)
                wrong = virgula2 ( engG2 )
                
                ##### counting the number of empty spaces 
                count = emptyCounter ( engList )
                
                ##### make new wrong randon list depend on count
                wrongF = random.sample( wrong, count)
                
                ##### fill in the gaps
                engList = fill_in ( engList , wrongF )
                yahia[japG[m]] = engList
          
                ##### empty lists before restarting over 
                wrong = []          
                engG2 = engG[:]
                m += 1
        
        # make the pre-last file of data ( contain : qst + ans + ABC + space ) 
        print_file ( yahia , abc.replace('.txt','_data.txt') )
        
        # make the last file of data using pickle 
        readfile6 ( abc.replace('.txt','_data.txt') , q_num )
        
        # delet files that i don't need 
        os.remove( './DATA/'+abc.replace('.txt',''))
        os.remove( './DATA/'+abc.replace('.txt','_data.txt'))
        os.rename( './DATA/'+abc.replace('.txt','_data_'),'./DATA/'+abc.replace('.txt','_'))


#--------------------------------------------------#
# for all users creat or delet function
#--------------------------------------------------#

def main_menu2():
    
    logo1 ()
    set_color(0xF8, handle=std_out_handle)
    print '  Hello user! Please take a look on Readme file before using this freeware.'
    set_color(0xF0, handle=std_out_handle)
        
    Xprint(4)
        
    print '  To Creat new data file type ',
    set_color(0xF4, handle=std_out_handle)
    print '< C > ' 
    set_color(0xF0, handle=std_out_handle)
    print 
    print '  To Delete data file type ',
    set_color(0xF4, handle=std_out_handle)
    print '< D >'
    set_color(0xF0, handle=std_out_handle)
    print
    print '  To Quit type ',
    set_color(0xF4, handle=std_out_handle)
    print '< Q >'  
    Xprint(3)     
    longLine ()
    
    w = upper ( raw_input ('  Answer: '))
    os.system('CLS')  
    while w not in ['C','D','Q'] :
        logo1 ()
        w = upper ( raw_input ("  Type < C > to creat new, < D > to delete data file or < Q > to quit : " ) )
        os.system('CLS')
        
    if  w == 'C' :  creat_data()
    elif w == 'D' : delete_data()
    elif w == 'Q' : byebye ()


#--------------------------------------------------#
#       Menu to Creat data                         #
#--------------------------------------------------#

def creat_data ():
    strt ='Y'

    while (strt == 'Y'):
        # 1. Some informations about how to use this program
        logo1 ()
        set_color(0xF3, handle=std_out_handle)
        print "  ANKIPY DATA MAKER MANUAL  "
        set_color(0xF0, handle=std_out_handle)
        print "  This program generate DATA files from your ANSI / UTF-8 text files "
        print "  Just put your files in DATA folder and start this program "
        print 
        set_color(0xF9, handle=std_out_handle)
        print "  1- MAKING",
        set_color(0xF4, handle=std_out_handle)
        print "FULL",
        set_color(0xF9, handle=std_out_handle)
        print "DATA FILES"
        set_color(0xF0, handle=std_out_handle)
        print "    You prepare the full 100 questions blocks like that :  "
        print "    1st Line :  Question ( What is the capital of France? ) "
        print "    2nd Line :  Answer A ( Alger )"
        print "    3rd Line :  Answer B ( Paris )"
        print "    4th Line :  Answer C ( Tokyo )"
        print "    5th Line :  Answer D ( London )"
        print "    6th Line :  Correct Answer ( B )"
        print "    7th Line :  Empty line "
        print "    ... etc."
        print
        
        print "  Click",
        set_color(0xF4, handle=std_out_handle)
        print "< enter >",
        set_color(0xF0, handle=std_out_handle)
        print "to continue..."
        gh = raw_input (' '*12)
        os.system('CLS')

        # 2. some informations about how to use this program 
        logo1 ()
        Xprint(1)
        set_color(0xF9, handle=std_out_handle)
        print "  IMPORTANT NOTES ABOUT FULL DATA FILES OF 100 BLOCKS"
        set_color(0xF0, handle=std_out_handle)
        print
        set_color(0xF9, handle=std_out_handle)
        print "  1.",
        set_color(0xF0, handle=std_out_handle)
        print " Files Always starts with a question and ends with an empty line"
        set_color(0xF9, handle=std_out_handle)
        print "  2.",
        set_color(0xF0, handle=std_out_handle)
        print " Correct Answer must :\n         Contain these Characters only : A B C and D\n         Letters Must be written in CAPITAL Characters\n         Letters Must be ordred from A to D : ex ACD / BC / AD...  "
        set_color(0xF9, handle=std_out_handle)
        print "  3.",
        set_color(0xF0, handle=std_out_handle)
        print " Empty spaces at the start of Questions and Answers Line are not allowed "
        set_color(0xF9, handle=std_out_handle)
        print "  4.",
        set_color(0xF0, handle=std_out_handle)
        print " After writing a Text full file convert it to Real random file \n      using ankipy DATA Maker "
        Xprint(2) 
        print "  Check full.txt to take an idea about how to build your own random DATA files."
        print
        
        set_color(0xF0, handle=std_out_handle)
        print "  Click",
        set_color(0xF4, handle=std_out_handle)
        print "< enter >",
        set_color(0xF0, handle=std_out_handle)
        print "to continue..."
        gh = raw_input (' '*12)
        os.system('CLS')

        # 3. some informations about how to use this program
        logo1 ()
        Xprint(1)
        set_color(0xF9, handle=std_out_handle)
        print "  2- MAKING",
        set_color(0xF4, handle=std_out_handle)
        print "RANDOM",
        set_color(0xF9, handle=std_out_handle)
        print "DATA FILES "
        print 
        set_color(0xF0, handle=std_out_handle)
        print "    Ankipy helps you to generate random answers to your questions, you only "
        print "    need to put the 100 questions and the right answer like that :  "
        print 
        print "    1st Line :  Question       ( What the meaning of Ryuu (Japanese)?) "
        print "    2nd Line :  Correct Answer ( Dragon,Axe,Style of )"
        print "    3rd Line :  Empty line     "
        print "    4th Line :  Question ( What is the capital of France? )"
        print "    5th Line :  Correct Answer ( Paris ) "
        print "    6th Line :  Empty line     "
        print "    ... ect. "
        Xprint(2)
        
        print "  Click",
        set_color(0xF4, handle=std_out_handle)
        print "< enter >",
        set_color(0xF0, handle=std_out_handle)
        print "to continue..."
        gh = raw_input (' '*12)
        os.system('CLS')
        
        # 4. some informations about how to use this program 
        logo1 ()
        Xprint(1)
        set_color(0xF9, handle=std_out_handle)
        print "  IMPORTANT NOTES ABOUT RANDOM DATA FILES 100 BLOCKS "
        set_color(0xF0, handle=std_out_handle)
        print
        set_color(0xF9, handle=std_out_handle)
        print "  1.",
        set_color(0xF0, handle=std_out_handle)
        print " Random files Always starts with a question and ends with an empty line. "
        set_color(0xF9, handle=std_out_handle)
        print "  2.",
        set_color(0xF0, handle=std_out_handle)
        print " Correct Answer must :\n         Contain one or many responds separated by coma(,) in one line\n         Spaces are not allowed after (,)"
        set_color(0xF9, handle=std_out_handle)
        print "  3.",
        set_color(0xF0, handle=std_out_handle)
        print " Empty spaces at the start of Questions and Answers Line are not allowed "
        set_color(0xF9, handle=std_out_handle)
        print "  4.",
        set_color(0xF0, handle=std_out_handle)
        print " After writing a Text random file convert it to Real random file\n      using ankipy DATA Maker "
        Xprint(2) 
        print "  Check random.txt to take an idea about how to build your own random DATA files"
        Xprint(1)
        
        set_color(0xF0, handle=std_out_handle)
        print "  Click",
        set_color(0xF4, handle=std_out_handle)
        print "< enter >",
        set_color(0xF0, handle=std_out_handle)
        print "to continue..."
        gh = raw_input (' '*12)

        os.system('CLS')

        # getting data file info
        logo1 ()
        Xprint(2)
        set_color(0xF8, handle=std_out_handle)
        print "  Put the Text file in DATA folder, Ankipy will convert it in few seconds.\n  You will find a new Module in Ankipy Tester just after this step."
        set_color(0xF0, handle=std_out_handle)
        Xprint(2) 
        f_name = raw_input("  Enter file name : ")
        f_name = f_name + '.txt'
        
    
        while ( os.path.exists('./DATA/'+f_name) == False ) or ( os.path.exists('./DATA/'+f_name.replace('.txt','_')) == True )  :
            os.system('CLS')
            logo1 ()
            Xprint(4)
            set_color(0xF8, handle=std_out_handle)
            print "  File name error ! "
            set_color(0xF0, handle=std_out_handle)
            f_name = raw_input("  Enter file name again : ")
            f_name = f_name + '.txt'
       
        print
        q_num,typ,msg,good = f_checker (f_name)
        
        if good == False:
            set_color(0xF8, handle=std_out_handle)
            print msg
            print
            mk = upper ( raw_input('  Type ( R ) to back to main menu     ( Q ) to quit  : ') )
            set_color(0xF0, handle=std_out_handle)
            while ( mk != 'R')&( mk != 'Q'):
                set_color(0xF8, handle=std_out_handle)
                mk = upper ( raw_input('  Type ( R ) to back to main menu     ( Q ) to quit  : ') )
                set_color(0xF0, handle=std_out_handle)
                
            if mk =='R':
                os.system('CLS')
                main_menu2()
                
            else:
                byebye ()
                
        elif good == True :
            
            os.system('CLS')
            # starts data converter : creat new cPickle file with same name
            logo1 ()
            Xprint(4)
            # change (remove) : readfile ( f_name , q_num , base )
            Xreadfile (f_name , int(q_num) , typ )

        ###### LOOP TEST  ##################
        
        set_color(0xF9, handle=std_out_handle)
        strt = upper( raw_input("  Do you like to make more files? (Y,N): ") )
        set_color(0xF0, handle=std_out_handle)
        strt = yes_no(strt)
        os.system('CLS')
     
    main_menu2 ()




#--------------------------------------------------#
# file checker function
#--------------------------------------------------#

def f_checker (f_name):
    """ data file checker """
    i=0
    typ = ''
    
    f = open ('./DATA/'+f_name,'r')
    G=[]
    for line in f:
        G.append( line.replace('\n',''))
    G.append ('') #important to avoid crash 
    
    if G[6]=='':
        i = 0
        while (G[0+7*i]!='')&(G[1+7*i]!='')&(G[2+7*i]!='')&(G[3+7*i]!='')&(G[4+7*i]!='')&(G[5+7*i]!='')&(G[6+7*i]==''):
            i += 1
            if i == 100 : break
        
        if i==100 :
            msg = '  Type of file : Full\n\n  Number of questions in this file : '+str(i)
            typ ='full'
            good = True   
        else : 
            msg = '  Error! check this question bloc : '+G[0+7*i]
            good = False
                
    elif G[2]=='':
        i = 0
        while (G[0+3*i]!='')&(G[1+3*i]!='')&(G[2+3*i]==''):
            i += 1
            if i == 100 : break
        if i==100 :
            typ='random'
            msg = '  Type of file : Random\n\n  Number of questions in this file : '+ str(i)
            good = True   
        else :
            msg = '  Error! check this question bloc : '+G[0+3*i]
            good = False
                
    else:
        msg = '  There is an error in your data file '
        good = False 
        
    return i,typ,msg,good 
    
#--------------------------------------------------#
#                Menu to Delet data                #
#--------------------------------------------------#

def delete_data ():
    
    logo1 ()
    #### load  data file names from modules using pickle
    
    ##### open the cPickle file
    f = open ( './MODULE/modules' )
    show_module = cPickle.load( f )
    f.close ()

    #### print the list of all the non original file (original files don't end with _) and creat new list of non orig. modules 
    numlist = ['R','Q']
    newlist = []
    k = 1
    for i in show_module:
        if i[-1:]=='_':
            numlist.append(str(k))
            newlist.append(i)
            set_color(0xF8, handle=std_out_handle)
            print '  ',k,'.',i
            set_color(0xF0, handle=std_out_handle)
            k += 1

    print        
    waw = "  Type the number of data file to delet" 
    if len(newlist)== 0: waw = ''

    # print choises
    print 
    print waw
    print 
    print "  Type",
    set_color(0xF4, handle=std_out_handle)
    print "< R >",
    set_color(0xF0, handle=std_out_handle)
    print "to return to main menu  "
    print
    print "  Type",
    set_color(0xF4, handle=std_out_handle)
    print "< Q >",
    set_color(0xF0, handle=std_out_handle)
    print "to exit  "
    print
    print
        
    longLine()
    # get choises
    yD = upper ( raw_input ( "  Answer here :" ) )
    os.system('CLS')
        
    while yD not in numlist:
        logo1()
        Xprint(2)
        #### print the list of all the non original file (original files don't end with _)
        #### and creat new list of non orig. modules 
        numlist = ['R','Q']
        newlist = []
        k = 1
        for i in show_module:
            if i[-1:]=='_':
                numlist.append(str(k))
                newlist.append(i)
                set_color(0xF8, handle=std_out_handle)
                print '  ',k,'.',i
                set_color(0xF0, handle=std_out_handle)
                k += 1

        print        
        waw = "  Type the number of data file to delet" 
        if len(newlist)== 0: waw = ''

        # print choises
        print 
        print waw
        print 
        print "  Type",
        set_color(0xF4, handle=std_out_handle)
        print "< R >",
        set_color(0xF0, handle=std_out_handle)
        print "to return to main menu  "
        print
        print "  Type",
        set_color(0xF4, handle=std_out_handle)
        print "< Q >",
        set_color(0xF0, handle=std_out_handle)
        print "to exit  "
        print
        print
        longLine()
        
        # get choises
        yD = upper ( raw_input ( "  Answer here :" ) )
        os.system('CLS')

    if yD == 'R':
        main_menu2 () 
        
    elif yD == 'Q':
        byebye () 
        
    else :
        mokli = yD
        word_remove = newlist[ int(mokli)-1 ]
        show_module.remove(word_remove)
        
        # to save changes in modules file
        fx = open ( './MODULE/modules','w' )
        cPickle.dump( show_module , fx )  
        fx.close ( )

        # remove file name from DATA folder
        os.remove('./DATA/'+word_remove)

        # back to delet menu
        delete_data ()


#################################################     MAIN     #############################################################


#---------------------------------#
#  Entrence logo and inforamtions #
#---------------------------------#

set_color(0xF0, handle=std_out_handle)  # change colors 
os.system('CLS')                        # clear screen 

entrence ()

main_menu2 ()

byebye ()
