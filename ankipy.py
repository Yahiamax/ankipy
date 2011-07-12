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


######################  IMPORTS ############################################################################################


import cPickle          # import pickle data base module
from string import *    # import strings functions
import os               # os.system('CLS') help me to clean the screen
import time             # for the entrance logo
import ctypes           # for colors
import hashlib          # for md5 encoding 


#---------------------- COLORS PACK ----------------------------------------#

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x01      # text color contains blue.
FOREGROUND_GREEN= 0x02      # text color contains green.
FOREGROUND_RED  = 0x04      # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10      # background color contains blue.
BACKGROUND_GREEN= 0x20      # background color contains green.
BACKGROUND_RED  = 0x40      # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


######################  FUNCTIONS   ########################################################################################


#------------------------------------#                     
#  functions of main GRAPHICS        #
#------------------------------------#

def logo1 ():
    """ logo without icons """
    print
    print
    set_color(0xF3, handle=std_out_handle)
    print u'                                                 █▀▀█ █▀█ █ █  █ █   █▀▀█ █  █ '  
    print u'                 (C) COPYRIGHT 2011 YAHIA MOKLI  █▄▄█ █ █ █ █▀▀▀ █   █▄▄█ █▄▄█ '
    print u'───────────────────────────────────────────────  █  █ █ █▄█ █▀▀█ █   █    ▄▄▄█ '
    set_color(0xF0, handle=std_out_handle)
    print
    print 

  
def logo ():
    """ logo with icons """
    print 
    set_color(0xF3, handle=std_out_handle)
    print u'                                                 █▀▀█ █▀█ █ █  █ █   █▀▀█ █  █ '  
    print u'                 (C) COPYRIGHT 2011 YAHIA MOKLI  █▄▄█ █ █ █ █▀▀▀ █   █▄▄█ █▄▄█ '
    print u'───────────────────────────────────────────────  █  █ █ █▄█ █▀▀█ █   █    ▄▄▄█ '     
    print 
    set_color(0xF4, handle=std_out_handle)
    print "           < Q >",
    set_color(0xF8, handle=std_out_handle)
    print " Quit",
    set_color(0xF4, handle=std_out_handle)
    print "     < R >",
    set_color(0xF8, handle=std_out_handle)
    print " Home     ",
    set_color(0xF4, handle=std_out_handle)
    print "< Alt + Enter >",
    set_color(0xF8, handle=std_out_handle)
    print " Full screen   "
    set_color(0xF0, handle=std_out_handle)

 
def longLine ():
    """ print long line (80) """
    set_color(0xF3, handle=std_out_handle)
    print u'─'*80,
    set_color(0xF0, handle=std_out_handle)
    print


def entrance ():
    """ entrance show """
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
    print                             
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
    print ' GNU v2 '
    print 
    time.sleep (3)
    set_color(0xF0, handle=std_out_handle)
    os.system('CLS')

   
def Xprint(x):
    """ print X new line """
    n = 0
    while n < x:
        print 
        n += 1 
    return None



#---------------------------------------------#
#   function show graphism when exit          #
#---------------------------------------------#

def putcenter (x):
    """ put x at the center of the page """
    y = len(x)
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
    putcenter ('YAHIA MOKLI (C) 2011   GNU v2 ')
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
    putcenter ('Please contact us on this e-mail')
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

    
#------------------------------------------------------------------------------------#                     
#  function print graph after each question to give an idea about user's progress    #
#------------------------------------------------------------------------------------#

def print_graph ( R , F , Q ):
    
        V = Q -(R + F)
        set_color(0xF2, handle=std_out_handle)
        graph1 = u'█'*R 
        graph2 = u'░'*F 
        graph3 = u' '*V
        graph = graph1 + graph2 + graph3
        
        graph_F= u'  │ '+graph[:50]+u' │'+'\n'+u'  │ '+ graph[50:]+u' │'
        print u'  ┌────────────────────────────────────────────────────┐\n',
        print graph_F,u' █ True',R,u' ░ False',F
        print u'  └────────────────────────────────────────────────────┘'
        set_color(0xF0, handle=std_out_handle)


#------------------------------------------------------------------------------------------------------------------#
# function check or add new users to pickle users file and return user type ( new /old / creat ) and user_name     #
#------------------------------------------------------------------------------------------------------------------#

def start_menu ( x ) :
    """ x : users_counter """
        
    if x == 0 :
        # if new user 
        logo1 ()
        set_color(0xF8, handle=std_out_handle)
        print "  Hello new user, Please take a look on Readme file before using this freeware."
        print
        print 
        print "  Creat your account please! "
        set_color(0xF0, handle=std_out_handle)
        print

        # get username 
        new_user_name = lower ( raw_input( "  Enter a username: "  )  )
        while len(new_user_name) > 20 :
            set_color(0xF8, handle=std_out_handle)
            print '  Username length must be less than 20 characters'
            set_color(0xF0, handle=std_out_handle)
            new_user_name = lower ( raw_input( "  Enter a username: "  )  )

        # get pass
        print 
        new_user_pass =  raw_input( "  Enter a password : "  )
        while len(new_user_pass) > 20 :
            set_color(0xF8, handle=std_out_handle)
            print '  Password length must be less than 20 characters'
            set_color(0xF0, handle=std_out_handle)
            new_user_pass =  raw_input( "  Enter a password : "  )

        # encode using MD5
        new_user_pass = hashlib.md5( new_user_pass ).hexdigest() # code the user pass word to md5
        
        os.system('CLS')
        
        usersList = {}
        usersList [new_user_name]= new_user_pass # add new user to the empty dictionary of users
            
        # this add a new user to users list
        users = open ('./USER/users','w')
        cPickle.dump( usersList, users )
        users.close ()

        # these are variables of sessions s_
        s_info = {}
            
        s_num = 0
        s_statue = 0
        s_module = 0
        s_total_question = 0
        s_right_ans = 0
        s_false_ans = 0
        
        s_info [s_num]=[ s_statue, s_module, s_total_question, s_right_ans, s_false_ans ]

               
        # add information to session dictionary 
        user_session_f = open ( './USER/'+new_user_name, 'w')
        cPickle.dump( s_info, user_session_f  )  
        user_session_f.close ( )
        # this will generate a file with the name of the user and contain the main values of sessions
            
        return 'new', new_user_name  # return type of user / name   

    else :
        # for the old user creat or login
        
        logo1 ()
        set_color(0xF8, handle=std_out_handle)
        print '  Hello user! Please take a look on Readme file before using this freeware.'
        set_color(0xF0, handle=std_out_handle)
        
        Xprint(4)
        
        print '  To login type ',
        set_color(0xF4, handle=std_out_handle)
        print '< L > '
        set_color(0xF0, handle=std_out_handle)
        print 
        print '  To creat new user account type ',
        set_color(0xF4, handle=std_out_handle)
        print '< C >'
        set_color(0xF0, handle=std_out_handle)
        
        Xprint(5)
        
        longLine ()
        w = upper ( raw_input ('  Answer: '))
        os.system('CLS')
        
        while w not in ['C','L'] :
            logo1 ()
            w = upper ( raw_input ("  Type < L > to login or < C > to creat new user account: " ) )
            os.system('CLS')
         
        if  w == 'L' :   # if login
            # get users list using cPickle
            users = open ('./USER/users')
            usersList = cPickle.load( users )
            users_f.close ()
                
            # get username and userpass
            logo1 ()
            set_color(0xF8, handle=std_out_handle)
            print '  Enter your Username and Password'
            set_color(0xF0, handle=std_out_handle)
            
            Xprint(2)
            
            old_user_name = lower ( raw_input( "  Username : "  )  )
            print 
            old_user_pass =  raw_input( "  Password  : "  )
            old_user_pass = hashlib.md5( old_user_pass ).hexdigest() # code the user pass word to md5
            os.system('CLS')
            
            while old_user_name not in usersList :
                logo1 ()
                set_color(0xF8, handle=std_out_handle)
                print '  Wrong username or password! Type them again  '
                set_color(0xF0, handle=std_out_handle)
                
                Xprint(2)
                
                old_user_name = lower ( raw_input( "  Username : "  )  )
                print 
                old_user_pass =  raw_input( "  Password  : "  )
                old_user_pass = hashlib.md5( old_user_pass ).hexdigest() # code the user pass word to md5
                os.system('CLS')
                
            while usersList[old_user_name] != old_user_pass :
                logo1 ()
                set_color(0xF8, handle=std_out_handle)
                print '  Wrong username or password! Type them again : '
                set_color(0xF0, handle=std_out_handle)
                
                Xprint(2)
                
                old_user_name = lower ( raw_input( "  Username : "  )  )
                print 
                old_user_pass =  raw_input( "  Password  : "  )
                old_user_pass = hashlib.md5( old_user_pass ).hexdigest() # code the user pass word to md5
                os.system('CLS')
                
            return 'old' , old_user_name 

        elif w == 'C' :
            # get users list using cPickle
            users = open ('./USER/users')
            usersList = cPickle.load( users )
            users.close ()

            # get username and userpass
            logo1 ()
            set_color(0xF8, handle=std_out_handle)
            print '  Enter your Username and Password'
            set_color(0xF0, handle=std_out_handle)
            
            Xprint(2)
            # get username     
            creat_user_name = lower ( raw_input ( "  Username : "  )  )
            while len(creat_user_name) > 20 :
                set_color(0xF8, handle=std_out_handle)
                print '  Username length must be less than 20 characters'
                set_color(0xF0, handle=std_out_handle)
                creat_user_name = lower ( raw_input ( "  Username : "  )  )

            # get pass
            print 
            creat_user_pass =  raw_input ( "  Password  : " )
            while len(creat_user_pass) > 20 :
                set_color(0xF8, handle=std_out_handle)
                print '  Password length must be less than 20 characters'
                set_color(0xF0, handle=std_out_handle)
                creat_user_pass =  raw_input ( "  Password  : " )
                
            creat_user_pass = hashlib.md5( creat_user_pass ).hexdigest() # code the user pass word to md5
            os.system('CLS')
            
            creat_user = {creat_user_name : creat_user_pass }
            
            # this update the values of usersList dictionary 
            usersList.update( creat_user )
                
            # this add the new user's info to users_list
            users = open ('./USER/users','w')
            cPickle.dump( usersList, users )
            users.close ()
            
            # these are variables of sessions s_
            s_info = {}
            
            s_num = 0
            s_statue = 'p'
            s_module = ''
            s_total_question = 0
            s_right_ans = 0
            s_false_ans = 0
                
            s_info [s_num]=[ s_statue, s_module, s_total_question, s_right_ans, s_false_ans ]

                   
            # add information to session dictionary 
            user_session_f = open ( './USER/'+creat_user_name, 'w')
            cPickle.dump( s_info, user_session_f )  
            user_session_f.close ( )
            # this will generate a file with the name of the user and contain the main values of sessions

            return 'new', creat_user_name


        

#--------------------------------------------------------------------------#
#        Main menu choices list differ from new to old users               #
#--------------------------------------------------------------------------#

def main_menu ( x , user_name ) :
    """ x : old_new """
    logo ()
    
    if  x == 'old'  :
        print
        set_color(0xF8, handle=std_out_handle)
        print "  Hello ", user_name,"!"
        set_color(0xF0, handle=std_out_handle)
        
        Xprint(3)
                
        print "  * To start new session type ( N ) "
        print 
        print "  * To complet a session type ( C ) "
        print 
        print "  * To delet a session   type ( D ) "
        
        Xprint(4)
                
        longLine ()
        y = upper ( raw_input ( "  Answer here : " ) )
        os.system('CLS')
        
        while ( y !='N' ) & ( y !='C') & ( y !='D') & ( y !='Q')  :
            logo ()
            print
            set_color(0xF8, handle=std_out_handle)
            print "  Hello ", user_name,"!"
            set_color(0xF0, handle=std_out_handle)
            
            Xprint(3)
                
            print "  * To start new session type ( N ) "
            print 
            print "  * To complet a session type ( C ) "
            print 
            print "  * To delet a session   type ( D ) "
            
            Xprint(4)
                
            longLine ()
            y = upper ( raw_input ( "  Answer again : " ) )
            os.system('CLS')
            
        if   y =='N': start_new_session( x , user_name ) 
        elif y =='C': complet_session ( user_name )   # we don't x cause it's an old user 
        elif y =='D': delet_session ( user_name )  
        elif y =='Q': byebye ()
        

    elif  x == 'new'  :
        print 
        print
        set_color(0xF8, handle=std_out_handle)
        print "  Hello new user !"
        set_color(0xF0, handle=std_out_handle)
        
        Xprint(3)
                
        print "  * To start new session type ( N ) "
        
        Xprint(7)
                
        longLine ()
        y = upper ( raw_input ( "  Answer here : " ) )
        os.system('CLS')
        while ( y !='N' ) & ( y !='Q') :
            logo ()
            
            Xprint(2)
                
            set_color(0xF8, handle=std_out_handle)
            print "  Hello new user !"
            set_color(0xF0, handle=std_out_handle)
            
            Xprint(3)
                 
            print "  * To start new session type ( N ) "
            
            Xprint(7)
                
            longLine ()
            y = upper ( raw_input ( "  Answer again : " ) )
            os.system('CLS')

        if   y =='N': start_new_session( x , user_name ) 
        elif y =='C': complet_session ( user_name )   # we don't x cause it's an old user 
        elif y =='D': delet_session ( user_name )  
        elif y =='Q': byebye ()




#--------------------------------------------------------------------------------------------------------------#   
#  Gets modules list from file modules_list return two list one of modules and second of numbers of moduels     #
#--------------------------------------------------------------------------------------------------------------#

def available_modules ( ) :
    import  modules_list  # get file of modules list to alow importing the function inside this file 
    modulesList = modules_list.modules ( )      # function just show list of modules
    h = len ( modulesList ) 
    hList = range ( 1, h+1 ) 
    i = 0 
    while i < h :
        set_color(0xF8, handle=std_out_handle)
        print ' ',i+1,".",modulesList[ i ].replace('_',' ')
        i = i+1
        set_color(0xF0, handle=std_out_handle)
    return hList, modulesList   # ( 1,2,3)




#------------------------------------------------#
#  Starts new session after doing 'N' choice     # 
#------------------------------------------------#

def start_new_session ( x , user_name ) :
    """ x : old_new """
    logo ()
    print 
    hList , modulesList = available_modules ( ) # this show list of availble modules
    
    Xprint(1)
                
    # Convert hList to list of str
    for n in hList :
            hList[n-1]=str(hList[n-1])
    print         
    print "  * To start type the number of module  "
    print 
    print "  * To return to main menu type ( R ) " 
    
    Xprint(2)
    
    longLine ()
    y2 = upper ( raw_input ( "  Answer here : " ) )
    os.system('CLS')
    
    while ( y2 !='R' ) & ( y2 !='Q') & ( y2 not in hList )  :
        logo ()
        print 
        hList , modulesList = available_modules ( ) # this show list of availble modules
        for n in hList :
            hList[n-1]=str(hList[n-1])
        
        Xprint(1)
                         
        print "  * To start type the number of module  "
        print 
        print "  * To return to main menu type ( R ) " 
        
        Xprint(2)
                 
        longLine ()
        y2 = upper ( raw_input ( "  Answer again :  " ) ) 
        os.system('CLS')
        
    if   y2 =='R': main_menu (x , user_name ) # x : old_new 
    elif y2 =='Q': byebye ()  
    else : start_session ( user_name , modulesList[ int ( y2 ) - 1 ]) 
    return None


#------------------------------------------------------------------#
# function loads questions and shows them befor starts testing     #
#------------------------------------------------------------------#
        
def start_session(user_name,module_name): # x : don't mean a lot cause we will read user file and see number of lines
  
    import modules_list
    T = modules_list.import_modules ( module_name ) # T must have 6 values 
    
    qst = [""]+ T[0]
    ansA = [""]+ T[1]
    ansB = [""]+ T[2]
    ansC = [""]+ T[3]
    ansD = [""]+ T[4]
    crct = [""]+ T[5]
    
               
    # get the number of questions in chosen list to save it in session 
    n = 0
    while n < len ( qst ) :
            if ( qst[n]=='' )& ( n!= 0 ) :
                    s_total_question = n
                    n = n+1
            else :
                    n = n + 1
                    s_total_question = n # 100 questions !

                
    ##########################################################################   
    # open session file and get those information
    # --> make the inforamtions in a "listS" and imoport them to this main var
     
    # open the user file to check the session length
    user_session_f = open ( './USER/'+user_name ) 
    ListS = cPickle.load( user_session_f ) # a dictionary list 
    user_session_f.close ()
                
    j = len ( ListS.keys() ) # the length of dictionay
                
    s_num = j   
    s_statue = 'p'
    s_module = module_name
    s_total_question = n-1 
    s_right_ans = 0
    s_false_ans = 0

    ListS [s_num]=[ s_statue, s_module, s_total_question, s_right_ans, s_false_ans ]
      
                   
    # add information to session dictionary 
    user_session_f = open ( './USER/'+user_name , 'w')
    cPickle.dump( ListS , user_session_f )  
    user_session_f.close ( )
        
    ########################################################################################
    x = 'old' # make this user an 'old' so when he come back to main_menu he find new things 
    ########################################################################################

    # print questions list :
    k = 1
    Qlen = len(qst)
    while k < Qlen :
            print
            set_color(0xF8, handle=std_out_handle)
            print "  Question Number",k,":",qst[k]
            set_color(0xF0, handle=std_out_handle)
            k = k + 1

    # print choises
    
    Xprint(3)
                 
    print "  * To start training type ( S )  "
    print 
    print "  * To return to main menu type ( R ) "
    
    Xprint(3)
                
    longLine()
    y3 = upper ( raw_input ( "  Answer here :" ) )
    print 
    os.system('CLS')
    
    while ( y3 !='R' ) & ( y3 !='Q') & ( y3 !='S')  :
            logo ()
            
            Xprint(5)
                
            print "  * To start training type ( S )  "
            print 
            print "  * To return to main menu type ( R ) "
            
            Xprint(6)
                
            longLine()
            y3 = upper ( raw_input ( "  Answer again :" ) )
            os.system('CLS')

    if   y3 =='R': main_menu( x , user_name ) # x : old_new 
    elif y3 =='Q': byebye ( )
    else : testing ( user_name, s_num , qst , ansA , ansB , ansC, ansD , crct  )


    
                
#--------------------------------------------------------------------#
#  Function loads incomplet sessions and links to testing function   #
#--------------------------------------------------------------------#
    
def complet_session ( user_name )  :
    
    # open the user file to print incomplet sessions
    user_session_f = open ( './USER/'+user_name ) 
    ListS = cPickle.load( user_session_f ) # a dictionary list 
    user_session_f.close ()
    
    ses = ListS.keys()      # save the key list ( s_num ) in new list 
    ses_len = len(ses)      # calculate the number of sessions 
    lm = 1                  # counter
    ctr = 1
    ctr <=10
    ses2 = ['','','','','','','','','','']
    k = 0
    print 
    print
    
    while ( lm < ses_len ) and ctr <=10 :
        sesL = ListS[ses[lm]]
        if sesL[0]=='p':
            set_color(0xF8, handle=std_out_handle)
            print '  Session:',ses[lm],'   ','Module:',sesL[1].replace('_',' ')
            set_color(0xF8, handle=std_out_handle)
            ses2[k] = ses[lm] 
            lm += 1
            ctr += 1
            k +=1    
        else: lm += 1
    
    Xprint(2)
                
    waw2 = "  * To complet type number of session" 
    if ses2[0]== '' : waw2 = ''

    print waw2
    print 
    print "  * To return to main menu type ( R ) "
    
    Xprint(2)
                
    ai = 0
    ses3 = ['','','','','','','','','','']
    for n in ses2 :
        ses3[ai]=str(ses2[ai])
        ai += 1
    
    longLine()
    yC = upper ( raw_input ( "  Answer here : " ) )
    os.system('CLS')

    sesFK = ses3+['R','Q']
    
    while  ( yC not in sesFK ) or ( yC==''):
        
        logo()
        Xprint(2)
        set_color(0xF8, handle=std_out_handle)
        print '  Sessions: ',
        H = 0
        while H < len(ses2):
            print ses2[H],
            H += 1
            
        set_color(0xF8, handle=std_out_handle)
        Xprint(2)  
        print waw2
        print 
        print "  * To return to main menu type ( R ) "
        Xprint(7)
        
        longLine()
        yC = upper ( raw_input ( "  Answer again : " ) )
        os.system('CLS')
        
        
    if   yC =='R': main_menu ( 'old' , user_name ) # x : old_new 
    elif yC =='Q': byebye ()    
    else :
        
        sesF = ListS[int(yC)]
        module_name = sesF[1]
        s_num = int(yC)
        
        # check if module name excist or not ?
        yaya = open('./MODULE/modules')
        mod_list = cPickle.load (yaya)
        yaya.close()

        if module_name not in mod_list:
            os.system('CLS')
            logo()
            Xprint(4)
            print '  ',module_name,"doesn't exist in DATA folder ! Please delete this session"
            print
            print           
            time.sleep(4)
            os.system('CLS')
            
            delet_session ( user_name )
                
        else:
            import modules_list
            T = modules_list.import_modules ( module_name )
            
            qst = [""]+ T[0]
            ansA = [""]+ T[1]
            ansB = [""]+ T[2]
            ansC = [""]+ T[3]
            ansD = [""]+ T[4]
            crct = [""]+ T[5]
            
            testing ( user_name, s_num , qst , ansA , ansB , ansC ,ansD , crct  )

            
                                           
#--------------------------------------------------------------#
#   Function shows all sessions and allow user to delet them   #   
#--------------------------------------------------------------#
        
def delet_session ( user_name ):
    
    # open the user file to print incomplet sessions
    user_session_f = open ( './USER/'+user_name ) 
    ListS = cPickle.load( user_session_f ) # a dictionary list 
    user_session_f.close ()
    
    ses = ListS.keys()
    ses2 = ses[1:]
    ses3 = list(' '* len(ses2))
    z= 0

    for j in ses2:
        ses3[z]=str(j)
        z += 1
        
    ses4 = ses3 +['R','Q']
    
    # print full list of sessions 
    ses_len = len(ses)      
    lm = 1                 
   
    while lm < ses_len :
        print 
        sesL = ListS[ses[lm]]
        set_color(0xF8, handle=std_out_handle)
        print '  Session:',ses[lm],'   ','Module:',sesL[1].replace('_',' ')
        set_color(0xF0, handle=std_out_handle)
        lm += 1

    Xprint(2)
    while 1:
        Xprint(2)

        ses5 = ListS.keys()
        ses6 = ses5[1:]
        set_color(0xF8, handle=std_out_handle)
        print '  Sessions: ',
        H = 0
        while H < len(ses6):
            print ses6[H],
            H += 1
        set_color(0xF0, handle=std_out_handle)        
        waw = "\n\n  * Type the number of session to delet" 
        if len(ses4)<= 2: waw = ''
        
        # print choises
        print 
        print waw
        print 
        print "  * Type ( R ) to return to main menu  "
        Xprint(4)
        longLine()
        
        # get choises
        yD = upper ( raw_input ( "  Answer here :" ) )
        os.system('CLS')
        
        while yD not in ses4:
            logo ()
            Xprint(2)
            print '  Sessions: ',
            H = 0
            while H < len(ses6): #continue 
                print ses6[H],
                H += 1
            print
            print waw
            print 
            print "  * Type ( R ) to return to main menu  "
            Xprint(6)
            longLine()
            yD = upper ( raw_input ( "  Answer again : " ) )
            os.system('CLS')
            
        if yD == 'R':
            main_menu ( 'old' , user_name ) # x : old_new 
            break
        elif yD == 'Q':
            byebye () 
            break
        else :
            Dl = yD
            ListS.pop(int(Dl))
            ses4.remove(Dl)

            # to save changes in session file
            user_session_f = open ( './USER/'+user_name, 'w')
            cPickle.dump( ListS , user_session_f )  
            user_session_f.close ( )       


     
#--------------------------------------------------------------------------#
# function of testing section it contains the main loop of the program     #
#--------------------------------------------------------------------------#
       
def testing ( user_name, s_num , qst , ansA , ansB , ansC , ansD , crct  ) : #n! == location we have to change if we want to make more than just ABCD choices  
    
    # open the user file to get informations about the last changes of session 
    user_session_f = open ( './USER/'+user_name ) 
    ListS = cPickle.load( user_session_f ) # a dictionary list 
    user_session_f.close ()

    s_statue = ListS [s_num][0]   
    s_module = ListS [s_num][1]   
    s_total_question = ( ListS [s_num][2] )     
    s_right_ans = ListS [s_num][3]   
    s_false_ans = ListS [s_num][4]   

                      
    n = ( s_right_ans + s_false_ans )+1
    while n <= s_total_question :
        logo ()
         
        # white / green / red
        print_graph ( s_right_ans , s_false_ans , s_total_question )
        
        print
        set_color(0xF8, handle=std_out_handle)
        print "  Question Number",n,":",
        set_color(0xF4, handle=std_out_handle)
        print qst[n]
        set_color(0xF0, handle=std_out_handle)
        print 
        print "  A. ",ansA[n]
        print 
        print "  B. ",ansB[n]
        print 
        print "  C. ",ansC[n]
        print
        print "  D. ",ansD[n] #n!
        print
        longLine () 
        y4 = upper ( raw_input ( "  Enter your answer here : " ) )+' '
        os.system('CLS')
        
        while ( y4[0] not in ['R','Q','A','B','C','D']) or ( len(y4) > 5 ) :            #n!
            logo ()
            # white / green / red
            print_graph ( s_right_ans , s_false_ans , s_total_question )
            print
            set_color(0xF8, handle=std_out_handle)
            print "  Question Number",n,":",
            set_color(0xF4, handle=std_out_handle)
            print qst[n]
            set_color(0xF0, handle=std_out_handle)
            print 
            print "  A. ",ansA[n]
            print 
            print "  B. ",ansB[n]
            print 
            print "  C. ",ansC[n]
            print
            print "  D. ",ansD[n]               #n!
            print
            longLine () 
            y4 = upper ( raw_input ( "  Enter your choice again : " ) )+' '
            os.system('CLS')
            
                                 
        if y4 =='R ' : main_menu ( 'old' , user_name )
        elif y4 =='Q ' : byebye()
        else :
            # reorder the list
            u = list(y4)
            u1=list ( ' '* (5- (u.count(' '))))             #n! (4 for 3 / 5 for 4 ... etc )  
            T=0
            while T < len (u):
                if u[T]=='A':
                    u1[0]=u[T]
                    T = T + 1
                    
                elif u[T]=='B':
                    u1[1]=u[T]
                    T += 1
        
                elif u[T]=='C':
                    u1[2]=u[T]
                    T += 1
                elif u[T]=='D':                             #n!
                    u1[3]=u[T]
                    T += 1
                    
                else :
                    T = T + 1

            if u1[0]==' ':u1[0]=''
            if u1[1]==' ':u1[1]=''
            if u1[2]==' ':u1[2]=''
            if u1[3]==' ':u1[3]=''
            
            bm = u1[0]+u1[1]+u1[2]+u1[3]            #n! 

            if bm == crct[n]:
                logo ()
                print_graph ( s_right_ans , s_false_ans , s_total_question )
                print
                set_color(0xF2, handle=std_out_handle)
                print '  Correct! The true answer is :'
                
                
                for o in crct[n] :
                    if o =='A':
                        print 
                        print '  A.',ansA[n]
                        
                    elif o=='B':
                        print 
                        print '  B.',ansB[n]
                        
                    elif o=='C':
                        print 
                        print '  C.',ansC[n]
                        
                    elif o=='D':
                        print 
                        print '  D.',ansD[n]    
                set_color(0xF0, handle=std_out_handle)
                
                s_right_ans = s_right_ans + 1   # add changes to session file 
                                              
            elif bm != crct[n]:
                logo ()
                
                print_graph ( s_right_ans , s_false_ans , s_total_question )
                print
                
                set_color(0xF4, handle=std_out_handle)
                print '  False! The true answer is :'
                
                
                for o in crct[n] :
                    if o =='A':
                        print 
                        print '  A.',ansA[n]
                    elif o=='B':
                        print 
                        print '  B.',ansB[n]
                    elif o=='C':
                        print 
                        print '  C.',ansC[n]
                    elif o=='D':
                        print 
                        print '  D.',ansD[n]    

                set_color(0xF0, handle=std_out_handle)
                
                s_false_ans = s_false_ans + 1 
                                              
            Xprint(2)
            longLine ()
            set_color(0xF8, handle=std_out_handle)
            raw_input ( "  press < enter > for the next question " )
            set_color(0xF0, handle=std_out_handle)
            os.system('CLS')
            
        # update the session informations          
        ListS [s_num]=[ s_statue, s_module, s_total_question, s_right_ans, s_false_ans ]
        
        # add information to session dictionary 
        user_session_f = open ( './USER/'+user_name, 'w')
        cPickle.dump( ListS , user_session_f )  
        user_session_f.close ( )

        n = n + 1
           
    s_statue = 'c' # we will need it in complet session menu and show list sessions 
    ListS [s_num]=[ s_statue, s_module, s_total_question, s_right_ans, s_false_ans ]
    
    user_session_f = open ( './USER/'+user_name, 'w')
    cPickle.dump( ListS , user_session_f  )  
    user_session_f.close ( )
              
    logo ()
    set_color(0xF3, handle=std_out_handle)
    print_graph ( s_right_ans , s_false_ans , s_total_question )
    print
    print "   Congratualtion! you finished this session  "
    set_color(0xF0, handle=std_out_handle)
    Xprint(2)
    print "  * Type ( R ) to return to main menu  "
    print 
    print "  * Type ( Q ) to exit  "
    Xprint(2)
    longLine ()
    
    y5 = upper ( raw_input ( "  enter your answer here : " ) )
    os.system('CLS')
    
    while ( y5 !='R' ) & ( y5 !='Q') :
        logo ()
        Xprint(3)
        print_graph ( s_right_ans , s_false_ans , s_total_question )
        Xprint(2) 
        print "  * Type ( R ) to return to main menu  "
        print 
        print "  * Type ( Q ) to exit  "
        Xprint(2)
        longLine ()
        y5 = upper ( raw_input ( "  enter your choice again : " ) )
        os.system('CLS')
        
    if   y5 =='R': main_menu ( 'old' , user_name ) # x : old_new 
    elif y5 =='Q': byebye()  






################################################     MAIN   ###############################################################

set_color(0xF0, handle=std_out_handle)
os.system('CLS')

#---------------------------------#
# entrance logo and inforamtions  #
#---------------------------------#

entrance ()

#---------------------------------#
# check the users file, load it   #
#---------------------------------#

users_list ={}    
users_f = open ('./USER/users') 
users_list = cPickle.load( users_f )
users_f.close ()

users_counter = len (users_list)
old_new, user_name = start_menu ( users_counter )
main_menu ( old_new, user_name ) 



byebye ()


                         
