o
    ���b0  �                   @   s�   d dl Z d dlZzd dlZW n   e �d� d dlZY dZdZdZdZdZdZ	dZ
d	Zd
Ze �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  eyV   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �
idtonum.py�header   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint%   s
   
�r   c                  C   sr  t ttd t ��} d}ddlm} d}d|  }|� }d|d< d|d	< d
|d< d|d< z
tj|||d�}W n   td� Y |�	� d dkrvtt
d � t ttd t ��}|dkrpt�d� t�d� t�d� t�d� d S t��  d S zttd t |�	� d d  � W n
   ttd � Y zttd t d |�	� d d  � W n
   ttd � Y zttd  t |�	� d d!  � W n
   ttd  � Y zttd" t |�	� d d#  � W n
   ttd" � Y zttd$ t |�	� d d%  � W n
   ttd$ � Y zttd& t |�	� d d'  � W n
   ttd& � Y zttd( t |�	� d d)  � W n
   ttd* � Y zttd+ t |�	� d d,  � W n
   ttd+ � Y zttd- t |�	� d d.  � W n
   ttd/ � Y zttd0 t |�	� d d1  � W n
   ttd0 � Y zttd2 t |�	� d d3  � W n
   ttd2 � Y zttd4 t |�	� d d5  � W n
   ttd4 � Y zttd6 t |�	� d d7  � W n
   ttd8 � Y zttd9 t |�	� d d:  � W n
   ttd9 � Y t ttd t ��}|dk�r3t�d� t�d� t�d� t�d� d S t��  d S );Nz

     Enter Circle ID: Z d29ac47b3ce9de73bb99c1b98dd6159br   )�CaseInsensitiveDictz5https://circle.robi.com.bd/mylife/appapi/appcall.php?z"op=getUserInfobyNickname&nickname=z	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Type)�headers�dataz=
     Your Request Rejected.Please Use VPN or Try Again LeterZrdescz	Not foundz     User Not foundz"

     Press Enter For Again Find � r   z.iDtoNumzpython idtonum.py�   z

     Nickname: r   Znicknamez     Nickname: z     Number: �+Zmsisdnz     Name: �namez     Points: Zpointsz     Followers: Z	followersz     Following: Z	followingz     Shouts: Zupdatesz     Shouts:z     Comments: Zcommentsz     Friends: Zfriendsz     Friends:z     Gender: Zgenderz     Birthday: Zbirthdayz     Lastseen: Z	timestampz     Start Date: Z
start_datez     Start Date:z     End Date: Zend_date)�str�input�green�yellowZrequests.structuresr   �requestsZpost�printZjson�red�cyan�purpler   r   r   r   r   r   �exit)�user�keyr   Zurlr   r   ZrespZenterr   r   r   �main.   s�   



$($$$$$$$$$$$$



r'   )r   r   r   r   ZblueZ	lightbluer!   Zwhiter   r   r"   �endr#   r	   r   r'   �KeyboardInterruptr$   r   r   r   r   �<module>   s2   



	b�