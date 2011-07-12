
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

###########################################      MAIN     ##################################################################

def modules ( )  :
        """ List of available modules """

        import cPickle
        f = open ('./MODULE/modules')
	mdl_lst = cPickle.load (f) # add 'new_file' like this : mdl_lst = ['japanese 1','new_file']
        f.close () 
	return mdl_lst 



def import_modules ( x ) :
        """ Importe module x """
        import cPickle 
        f = open ( './DATA/'+x )
        T = cPickle.load( f )
        f.close ()        
	return T

	
